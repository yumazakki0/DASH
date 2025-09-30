# app.py
# Inicializa o Dash app e exporta app e server para serem usados em index.py
# Aqui definimos estilos globais via Bootstrap e configuramos o server Flask
import dash
import dash_bootstrap_components as dbc

# Escolha de tema Bootstrap apenas para facilitar componentes; o CSS customizado em /assets/style.css sobrepõe esse tema
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True
)
server = app.server

# Pequeno helper global
def register_layout(layout):
    """
    Use essa função para garantir que o layout seja compatível com o app.
    Chamamos isso em index.py ao setar app.layout.
    """
    app.layout = layout

# 🔑 IMPORTA CALLBACKS AQUI (depois que app foi criado)
# Isso garante que todos @app.callback sejam registrados
import callbacks.cadastro_callbacks
import callbacks.movimentacao_callbacks
import callbacks.lista_callbacks
import callbacks.login_callbacks  # adicionado para autenticação

# ⚠️ Opcional: criar usuário padrão 'admin' se não existir
from callbacks.login_callbacks import criar_usuario_se_nao_existe
criar_usuario_se_nao_existe()
