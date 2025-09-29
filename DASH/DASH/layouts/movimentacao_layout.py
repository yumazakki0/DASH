# layouts/movimentacao_layout.py
# Formulário para entrada/saída de estoque e histórico rápido
from dash import html, dcc
import dash_bootstrap_components as dbc

def build_movimentacao_layout():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H2("Movimentação de Estoque", className="gothic-title"), width=12)),
        dbc.Row([
            dbc.Col([
                dbc.Label("ID do produto"),
                dbc.Input(id="mov-id", type="text", placeholder="Informe o ID do produto"),
                dbc.Label("Quantidade"),
                dbc.Input(id="mov-quantidade", type="number", min=1, value=1),
                html.Div(className="mt-3", children=[
                    dbc.Button("Entrada", id="mov-entrada", color="success", className="me-2"),
                    dbc.Button("Saída", id="mov-saida", color="danger"),
                    dbc.Button("Voltar", href="/home", color="secondary", className="ms-2")
                ]),
                html.Div(id="mov-feedback", className="mt-3")
            ], width=6),
            dbc.Col([
                html.H5("Histórico recente"),
                html.Div(id="mov-historico")
            ], width=6)
        ])
    ], fluid=True)
    return layout
