# layouts/home_layout.py
# Layout principal (dashboard) com links para cadastro, movimentação, lista e gráficos.
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from callbacks.common import carregar_produtos

def small_kpi(title, value, id_value):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H6(title, className="card-title"),
                html.H3(id=id_value, children=value, className="card-value")
            ]
        ),
        className="kpi-card"
    )

def build_home_layout(usuario=None):
    df = carregar_produtos()

    # gráfico demonstrativo
    try:
        fig = px.bar(df, x='Nome', y='Quantidade em estoque', color='Categoria', title='Estoque por Produto')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    except Exception:
        fig = {}

    total_produtos = len(df)
    total_itens = int(df['Quantidade em estoque'].sum()) if not df.empty else 0

    layout = dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Dashboard", className="gothic-title"), width=8),
            dbc.Col(dbc.Button("Sair", href='/login', color="danger"), width=4, className="text-end")
        ], className="mt-3"),
        dbc.Row([
            dbc.Col(small_kpi("Produtos Cadastrados", total_produtos, "kpi-total-prod"), md=4),
            dbc.Col(small_kpi("Itens em Estoque", total_itens, "kpi-total-itens"), md=4),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Ações rápidas"),
                    dbc.Button("Cadastrar Produto", href="/cadastro", color="primary", className="me-2"),
                    dbc.Button("Movimentação", href="/movimentacao", color="secondary", className="me-2"),
                    dbc.Button("Listar Produtos", href="/lista", color="light")
                ])
            ], className="kpi-card"), md=4)
        ], className="mt-3"),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig), md=12)
        ], className="mt-4"),
        html.Hr(),
        dbc.Row([
            dbc.Col(html.Div([
                html.H5("Bem vindo, " + (usuario or "usuário")),
                html.P("Use o menu acima para navegar entre cadastro, movimentação e lista.")
            ]))
        ])
    ], fluid=True)
    return layout
