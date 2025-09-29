# callbacks/movimentacao_callbacks.py
# Lida com entradas e saídas de estoque e registra histórico em CSV simples.
from dash import Input, Output, State
from app import app
import pandas as pd
import os
from callbacks.common import carregar_produtos, salvar_produtos, buscar_produto_por_id

HIST_CSV = 'data/movimentacoes.csv'

def garantir_historico_existe():
    if not os.path.exists(HIST_CSV):
        df = pd.DataFrame(columns=['timestamp', 'id', 'acao', 'quantidade', 'usuario'])
        df.to_csv(HIST_CSV, index=False)

garantir_historico_existe()

@app.callback(
    Output('mov-feedback', 'children'),
    Output('mov-historico', 'children'),
    Input('mov-entrada', 'n_clicks'),
    Input('mov-saida', 'n_clicks'),
    State('mov-id', 'value'),
    State('mov-quantidade', 'value'),
    prevent_initial_call=True
)
def movimentar(entrada_clicks, saida_clicks, prod_id, quantidade):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "", ""
    btn_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if not prod_id:
        return dbc.Alert("Informe o ID do produto.", color="danger"), ""
    if not quantidade:
        return dbc.Alert("Informe a quantidade.", color="danger"), ""
    prod = buscar_produto_por_id(prod_id)
    if not prod:
        return dbc.Alert("Produto não encontrado.", color="danger"), ""
    df = carregar_produtos()
    idx = df[df['ID'] == prod_id].index
    if idx.empty:
        return dbc.Alert("Produto não encontrado na base.", color="danger"), ""
    idx = idx[0]
    quantidade = int(quantidade)
    acao = 'entrada' if btn_id == 'mov-entrada' else 'saida'
    if acao == 'saida' and df.at[idx, 'Quantidade em estoque'] < quantidade:
        return dbc.Alert("Quantidade insuficiente em estoque.", color="danger"), ""
    # aplica movimentação
    if acao == 'entrada':
        df.at[idx, 'Quantidade em estoque'] += quantidade
    else:
        df.at[idx, 'Quantidade em estoque'] -= quantidade
    salvar_produtos(df)
    # registra histórico
    hist = pd.read_csv(HIST_CSV)
    import datetime
    hist = pd.concat([hist, pd.DataFrame([{
        'timestamp': datetime.datetime.now().isoformat(),
        'id': prod_id,
        'acao': acao,
        'quantidade': quantidade,
        'usuario': 'dev'  # poderá vir do session-store
    }])], ignore_index=True)
    hist.to_csv(HIST_CSV, index=False)
    # monta histórico resumido
    ultimos = hist.tail(8).iloc[::-1]
    rows = []
    for _, r in ultimos.iterrows():
        rows.append(html.Div(f"{r['timestamp']} - {r['id']} - {r['acao']} - {r['quantidade']}"))
    return dbc.Alert(f"Movimentação {acao} de {quantidade} aplicada ao produto {prod_id}.", color="success"), rows
