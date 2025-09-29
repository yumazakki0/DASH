# app.py
# Inicializa o Dash app e exporta app e server para serem usados em index.py
# Aqui definimos estilos globais via Bootstrap e configuramos o server Flask
import dash
import dash_bootstrap_components as dbc

# Escolha de tema Bootstrap apenas para facilitar componentes; o CSS customizado em /assets/style.css sobrepõe esse tema
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
server = app.server

# Pequeno helper global (pode ser importado em outros módulos)
def register_layout(layout):
    """
    Use essa função para garantir que o layout seja compatível com o app.
    Chamamos isso em index.py ao setar app.layout.
    """
    app.layout = layout


