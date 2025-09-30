# callbacks/lista_callbacks.py
from dash import Input, Output
from app import app
from callbacks.common import carregar_produtos

# Callback para atualizar a tabela de produtos
@app.callback(
    Output('produtos-tabela', 'data'),
    Input('produtos-tabela', 'id')  # trigger inicial quando o layout é carregado
)
def atualizar_tabela(_):
    df = carregar_produtos()
    return df.to_dict('records')
