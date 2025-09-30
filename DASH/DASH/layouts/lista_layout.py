from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table
from callbacks.common import carregar_produtos

def build_lista_layout():
    df = carregar_produtos()
    table = dash_table.DataTable(
        id='produtos-tabela',
        columns=[{"name": c, "id": c} for c in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_header={'backgroundColor': '#1a1a1a', 'color': 'white'},
        style_cell={'backgroundColor': '#333', 'color': 'white', 'textAlign': 'left'},
        filter_action='native',
        sort_action='native',
        page_size=10
    )

    return dbc.Container([
        dbc.Row(dbc.Col(html.H2("Lista de Produtos", className="gothic-title mb-3"), width=12)),
        dbc.Row(dbc.Col(table, width=12)),
        dbc.Row(dbc.Col(dbc.Button("Voltar", href="/home", color="secondary", className="mt-3"), width=12))
    ], fluid=True)
