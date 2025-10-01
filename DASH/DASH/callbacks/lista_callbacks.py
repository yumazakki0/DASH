# callbacks/lista_callbacks.py
# Este módulo contém o callback responsável por atualizar a tabela de produtos
# exibida na interface. Ele lê os dados do CSV (via carregar_produtos)
# e os envia para a DataTable do Dash.

from dash import Input, Output   # Objetos necessários para callbacks do Dash
from app import app              # Instância principal do app Dash
from callbacks.common import carregar_produtos  # Função que carrega os produtos do CSV

# Callback que atualiza a tabela de produtos
@app.callback(
    Output('produtos-tabela', 'data'),  # A saída é o conteúdo da tabela (atributo 'data')
    Input('produtos-tabela', 'id')      # O input aqui é o 'id' da tabela.
                                        # Ele serve apenas como "gatilho" inicial
                                        # para que o callback seja executado ao carregar a página.
)
def atualizar_tabela(_):
    """
    Atualiza os dados da tabela de produtos.
    - Carrega os produtos do CSV usando carregar_produtos().
    - Converte o DataFrame em uma lista de dicionários (formato aceito pela DataTable).
    - Retorna a lista para que a tabela seja renderizada/atualizada na interface.
    """
    df = carregar_produtos()              # Carrega todos os produtos existentes
    return df.to_dict('records')          # Converte DataFrame em lista de registros (dicts)
