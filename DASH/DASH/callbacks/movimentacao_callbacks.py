# callbacks/movimentacao_callbacks.py
# Este módulo lida com a movimentação de estoque (entrada e saída de produtos).
# Ele atualiza o estoque em produtos.csv, registra no histórico (movimentacoes.csv)
# e exibe feedback e histórico recente na interface.

from dash import Input, Output, State, html   # Componentes e objetos do Dash
import dash                                   # Usado para capturar contexto do callback
import dash_bootstrap_components as dbc       # Alertas estilizados do Bootstrap
from app import app                           # Instância principal do app
import pandas as pd                           # Manipulação de dados
import os                                     # Operações de sistema de arquivos
import datetime                               # Marcações de tempo para o histórico
from callbacks.common import carregar_produtos, salvar_produtos, buscar_produto_por_id
# carregar_produtos -> lê produtos do CSV
# salvar_produtos   -> salva DataFrame no CSV
# buscar_produto_por_id -> busca produto específico pelo ID

# Caminho para o CSV de histórico de movimentações
HIST_CSV = os.path.join("data", "movimentacoes.csv")

def garantir_historico_existe():
    """
    Garante que o arquivo de histórico de movimentações exista.
    - Cria a pasta "data/" se não existir.
    - Cria movimentacoes.csv com colunas padrão, caso ainda não exista.
    """
    os.makedirs(os.path.dirname(HIST_CSV), exist_ok=True)  # garante pasta "data"
    if not os.path.exists(HIST_CSV):
        df = pd.DataFrame(columns=['timestamp', 'id', 'acao', 'quantidade', 'usuario'])
        df.to_csv(HIST_CSV, index=False)

# Executa ao carregar o módulo para garantir a existência do histórico
garantir_historico_existe()

# Callback que processa entradas e saídas de estoque
@app.callback(
    Output('mov-feedback', 'children'),   # Mensagem de alerta (erro ou sucesso)
    Output('mov-historico', 'children'),  # Histórico renderizado na tela
    Output('mov-id', 'value'),            # Limpa o campo ID após operação
    Output('mov-quantidade', 'value'),    # Reseta o campo quantidade
    Input('mov-entrada', 'n_clicks'),     # Botão de entrada
    Input('mov-saida', 'n_clicks'),       # Botão de saída
    State('mov-id', 'value'),             # ID do produto informado
    State('mov-quantidade', 'value'),     # Quantidade a movimentar
    prevent_initial_call=True             # Evita execução no carregamento inicial
)
def movimentar(entrada_clicks, saida_clicks, prod_id, quantidade):
    """
    Função executada ao clicar em "Entrada" ou "Saída".
    - Verifica qual botão foi clicado.
    - Valida ID do produto e quantidade.
    - Atualiza estoque (entrada ou saída).
    - Salva movimentação no histórico (CSV).
    - Retorna feedback, histórico recente e reseta campos do formulário.
    """

    # Captura qual botão disparou o callback
    ctx = dash.callback_context
    if not ctx.triggered:
        return "", [], "", 1
    btn_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Validações iniciais
    if not prod_id:
        return dbc.Alert("Informe o ID do produto.", color="danger"), [], "", 1
    if not quantidade:
        return dbc.Alert("Informe a quantidade.", color="danger"), [], "", 1

    # Verifica se o produto existe
    prod = buscar_produto_por_id(prod_id)
    if not prod:
        return dbc.Alert("Produto não encontrado.", color="danger"), [], "", 1

    # Carrega produtos e localiza índice do produto
    df = carregar_produtos()
    idx = df[df['ID'] == prod_id].index
    if idx.empty:
        return dbc.Alert("Produto não encontrado na base.", color="danger"), [], "", 1
    idx = idx[0]

    # Converte quantidade e define ação
    quantidade = int(quantidade)
    acao = 'entrada' if btn_id == 'mov-entrada' else 'saida'

    # Valida estoque suficiente em caso de saída
    if acao == 'saida' and df.at[idx, 'Quantidade em estoque'] < quantidade:
        return dbc.Alert("Quantidade insuficiente em estoque.", color="danger"), [], "", 1

    # Aplica movimentação ao DataFrame
    if acao == 'entrada':
        df.at[idx, 'Quantidade em estoque'] += quantidade
    else:
        df.at[idx, 'Quantidade em estoque'] -= quantidade
    salvar_produtos(df)  # Salva estoque atualizado

    # Registra no histórico
    hist = pd.read_csv(HIST_CSV)
    hist = pd.concat([hist, pd.DataFrame([{
        'timestamp': datetime.datetime.now().isoformat(),  # Data/hora atual
        'id': prod_id,
        'acao': acao,
        'quantidade': quantidade,
        'usuario': 'dev'  # Aqui poderia ser o usuário logado
    }])], ignore_index=True)
    hist.to_csv(HIST_CSV, index=False)

    # Monta histórico resumido (últimos 8 registros, invertido para ordem recente)
    ultimos = hist.tail(8).iloc[::-1]
    rows = [html.Div(f"{r['timestamp']} - {r['id']} - {r['acao']} - {r['quantidade']}") for _, r in ultimos.iterrows()]

    # Retorna: feedback, histórico, limpa campos
    return dbc.Alert(f"Movimentação {acao} de {quantidade} aplicada ao produto {prod_id}.", color="success"), rows, "", 1
