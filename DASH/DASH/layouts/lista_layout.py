# layouts/lista_layout.py
# Tabela com listagem dos produtos e filtros simples
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from callbacks.common import carregar_produtos

def build_lista_layout():
    df = carregar_produtos()
    # converter para html table simples (pode ser substituído por dash_table.DataTable futuramente)
    table_header = [
        html.Thead(html.Tr([html.Th(c) for c in df.columns]))
    ]
    table_body = []
    for _, row in df.iterrows():
        table_body.append(html.Tr([html.Td(row[c]) for c in df.columns]))
    table = dbc.Table(table_header + [html.Tbody(table_body)], bordered=True, dark=True, hover=True, responsive=True, striped=True)

    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H2("Lista de Produtos", className="gothic-title"), width=12)),
        dbc.Row(dbc.Col(table, width=12)),
        dbc.Row(dbc.Col(dbc.Button("Voltar", href="/home", color="secondary"), width=12, className="mt-3"))
    ], fluid=True)
    return layout
