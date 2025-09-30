from dash import html
import dash_bootstrap_components as dbc

def build_cadastro_layout():
    layout = dbc.Container([
        dbc.Row(dbc.Col(html.H2("Cadastrar Produto", className="gothic-title"), width=12)),
        dbc.Row([
            dbc.Col([
                dbc.Label("ID (deixe vazio para auto)"),
                dbc.Input(id="cad-id", type="text", placeholder="ID opcional"),
                dbc.Label("Nome"),
                dbc.Input(id="cad-nome", type="text", placeholder="Nome do produto"),
                dbc.Label("Categoria"),
                dbc.Input(id="cad-categoria", type="text", placeholder="Categoria"),
                dbc.Label("Quantidade em estoque"),
                dbc.Input(id="cad-quantidade", type="number", min=0, value=1),
                dbc.Label("Preço de compra"),
                dbc.Input(id="cad-preco-compra", type="number", min=0, step="0.01"),
                dbc.Label("Preço de venda"),
                dbc.Input(id="cad-preco-venda", type="number", min=0, step="0.01"),
                dbc.Label("Fornecedor"),
                dbc.Input(id="cad-fornecedor", type="text", placeholder="Nome do fornecedor"),
                html.Div(className="mt-3", children=[
                    dbc.Button("Salvar", id="cad-salvar", color="primary"),
                    dbc.Button("Voltar", href="/home", color="secondary", className="ms-2")
                ]),
                html.Div(id="cad-feedback", className="mt-3")
            ], width=6)
        ])
    ], fluid=True)
    return layout
