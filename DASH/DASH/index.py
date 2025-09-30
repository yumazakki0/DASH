# index.py
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import os

from app import register_layout, app, server
from layouts.landing_layout import build_landing_layout
from layouts.login_layout import build_login_layout
from layouts.home_layout import build_home_layout
from layouts.cadastro_layout import build_cadastro_layout
from layouts.movimentacao_layout import build_movimentacao_layout
from layouts.lista_layout import build_lista_layout
from callbacks.login_callbacks import validar_login, criar_usuario_se_nao_existe
from callbacks.common import garantir_data_files, USUARIOS_CSV

# 1️⃣ Garante estrutura de pastas e CSV
garantir_data_files()
criar_usuario_se_nao_existe()

# 2️⃣ Layout principal
register_layout(html.Div([
    dcc.Location(id='url', refresh=False),  # <--- remove o True
    dcc.Store(id='session-store', data={'logado': False, 'usuario': None}),
    #miojo heeheh
    html.Div(id='page-content', className="page-fade")
]))


# 3️⃣ Callback que monta página conforme URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    State('session-store', 'data')
)
def display_page(pathname, session):
    logado = session.get('logado') if session else False
    usuario = session.get('usuario') if session else None

    if pathname in ['/', '/inicio']:
        return build_landing_layout()

    if pathname == '/login':
        alert_msg = None
        if session and session.get('logado') is False:
            alert_msg = "Usuário ou senha incorretos."
        return build_login_layout(alert_text=alert_msg)

    # 🔒 Páginas protegidas
    protected_pages = {
        '/home': lambda: build_home_layout(usuario),
        '/cadastro': lambda: build_cadastro_layout(),
        '/movimentacao': lambda: build_movimentacao_layout(),
        '/lista': lambda: build_lista_layout()
    }

    if pathname in protected_pages:
        if logado:
            page_func = protected_pages[pathname]
            return page_func()  # garante que a função seja chamada
        else:
            return build_login_layout(alert_text="Faça login primeiro.")

    # Página 404
    return html.Div([
        dbc.Container([
            html.H1("404 - Página não encontrada", className="gothic-title"),
            dbc.Button("Voltar ao Login", href='/login', color="dark")
        ], className="text-center mt-5")
    ])


# 4️⃣ Callback de login
@app.callback(
    Output('session-store', 'data'),
    Output('url', 'pathname'),
    Input('login-submit', 'n_clicks'),
    State('login-username', 'value'),
    State('login-password', 'value'),
    prevent_initial_call=True
)
def handle_login(n_clicks, username, password):
    if not username or not password:
        return {'logado': False, 'usuario': None}, '/login'

    if validar_login(username, password):
        return {'logado': True, 'usuario': username}, '/home'

    return {'logado': False, 'usuario': None}, '/login'


# 5️⃣ Executa o servidor
if __name__ == '__main__':
    app.run(debug=True, port=8050)
