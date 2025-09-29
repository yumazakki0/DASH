# index.py
# Ponto de entrada do sistema. Inicializa a página e controla navegação básica.

from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import register_layout, app, server
from layouts.landing_layout import build_landing_layout
from layouts.login_layout import build_login_layout
from layouts.home_layout import build_home_layout
from callbacks.login_callbacks import validar_login, criar_usuario_se_nao_existe
from callbacks.common import garantir_data_files

# Garante que CSV/DB básicos existam (cria estrutura inicial)
garantir_data_files()

# Layout principal da aplicação
register_layout(html.Div([
    dcc.Location(id='url', refresh=True),  # Força atualização visual ao navegar
    dcc.Store(id='session-store', data={'logado': False, 'usuario': None}),
    html.Div(id='page-content')
]))

# Callback que monta a página conforme a URL e o estado de sessão
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    State('session-store', 'data')
)
def display_page(pathname, session):

    print(f"URL: {pathname}, Sessão: {session}")

    if pathname in ['/', '/inicio']:
        return build_landing_layout()

    if pathname == '/login':
        return build_login_layout()

    if pathname == '/home':
        if not session.get('logado'):
            return build_login_layout(alert_text="Você precisa fazer login para acessar o painel.")
        return build_home_layout(session.get('usuario'))

    if pathname == '/cadastro':
        if not session.get('logado'):
            return build_login_layout(alert_text="Faça login primeiro.")
        from layouts.cadastro_layout import build_cadastro_layout
        return build_cadastro_layout()

    if pathname == '/movimentacao':
        if not session.get('logado'):
            return build_login_layout(alert_text="Faça login primeiro.")
        from layouts.movimentacao_layout import build_movimentacao_layout
        return build_movimentacao_layout()

    if pathname == '/lista':
        if not session.get('logado'):
            return build_login_layout(alert_text="Faça login primeiro.")
        from layouts.lista_layout import build_lista_layout
        return build_lista_layout()

    # Página 404
    return html.Div([
        dbc.Container([
            html.H1("404 - Página não encontrada", className="gothic-title"),
            dbc.Button("Voltar ao Login", href='/login', color="dark")
        ], className="text-center mt-5")
    ])

# Callback de login: atualiza sessão e redireciona
@app.callback(
    Output('session-store', 'data'),
    Output('url', 'pathname'),
    Input('login-submit', 'n_clicks'),
    State('login-username', 'value'),
    State('login-password', 'value'),
    prevent_initial_call=True
)
def handle_login(n_clicks, username, password):
    print(f"Login clicado: {n_clicks}, usuário: {username}, senha: {password}")
    criar_usuario_se_nao_existe()

    # Modo de desenvolvimento: aceita qualquer login
    return {'logado': True, 'usuario': username}, '/home'

    # Se quiser validar de verdade, use:
    # if validar_login(username, password):
    #     return {'logado': True, 'usuario': username}, '/home'
    # return {'logado': False, 'usuario': None}, '/login'

# Executa o servidor
if __name__ == '__main__':
    app.run(debug=True, port=8050)
