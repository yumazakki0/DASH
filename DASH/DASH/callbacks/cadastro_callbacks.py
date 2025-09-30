# callbacks/cadastro_callbacks.py
# Lida com o cadastro de produtos: gera ID se necessário e salva no CSV.
from dash import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import pandas as pd
from callbacks.common import carregar_produtos, salvar_produtos, gerar_id_unico

@app.callback(
    Output('cad-feedback', 'children'),
    Input('cad-salvar', 'n_clicks'),
    State('cad-id', 'value'),
    State('cad-nome', 'value'),
    State('cad-categoria', 'value'),
    State('cad-quantidade', 'value'),
    State('cad-preco-compra', 'value'),
    State('cad-preco-venda', 'value'),
    State('cad-fornecedor', 'value'),
    prevent_initial_call=True
)
def salvar_produto(n_clicks, cad_id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
    if not nome or quantidade is None:
        return dbc.Alert("Nome e quantidade são obrigatórios.", color="danger")

    df = carregar_produtos()
    if not cad_id:
        cad_id = gerar_id_unico()

    if not df[df['ID'] == cad_id].empty:
        return dbc.Alert("ID já existe. Informe outro ID ou deixe em branco.", color="danger")

    novo = {
        'ID': cad_id,
        'Nome': nome,
        'Categoria': categoria or 'Sem categoria',
        'Quantidade em estoque': int(quantidade),
        'Preço de compra': float(preco_compra) if preco_compra else 0.0,
        'Preço de venda': float(preco_venda) if preco_venda else 0.0,
        'Fornecedor': fornecedor or ''
    }
    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    salvar_produtos(df)
    return dbc.Alert(f"Produto {nome} cadastrado com sucesso (ID: {cad_id}).", color="success")
