from dash import html, dcc
import dash_bootstrap_components as dbc

def build_login_layout(alert_text=None):
    alert = None
    if alert_text:
        alert = dbc.Alert(alert_text, color="danger", dismissable=True, className="mt-3")

    layout = dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        [
                            html.Div(className="gothic-header", children=[
                                html.H1("NOCTIS INVENTORY"),
                                html.P("Controle de Estoque – Painel")
                            ]),
                            dbc.CardBody(
                                [
                                    dbc.Label("Usuário", className="text-white"),
                                    dbc.Input(id="login-username", placeholder="nome de usuário", type="text", className="mb-2"),
                                    dbc.Label("Senha", className="text-white"),
                                    dbc.Input(id="login-password", placeholder="senha", type="password", className="mb-3"),
                                    dbc.Button("Entrar", id="login-submit", color="dark", className="me-2"),
                                    dbc.Button("Ir ao Cadastro (dev)", href="/cadastro", color="secondary"),
                                    html.Div(id="login-feedback", children=alert)
                                ]
                            )
                        ],
                        className="login-card"
                    ),
                    width={"size": 6, "offset": 3}
                )
            )
        ],
        fluid=True,
        className="login-container"
    )
    return layout
