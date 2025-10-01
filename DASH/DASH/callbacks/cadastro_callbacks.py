# callbacks/cadastro_callbacks.py
# Este arquivo contém o callback responsável pelo cadastro de produtos.
# Ele lida com a validação dos campos, geração de ID (quando necessário),
# inserção no DataFrame e salvamento no arquivo CSV.

from dash import Input, Output, State  # Importa objetos necessários para callbacks do Dash
import dash_bootstrap_components as dbc  # Componentes prontos de estilo Bootstrap para Dash
from app import app  # Importa a instância do aplicativo Dash
import pandas as pd  # Usado para manipulação de dados em DataFrame
from callbacks.common import carregar_produtos, salvar_produtos, gerar_id_unico  
# carregar_produtos -> carrega produtos de um CSV
# salvar_produtos   -> salva os produtos em CSV
# gerar_id_unico    -> gera um identificador único para novos produtos

# Callback responsável por salvar o produto
@app.callback(
    Output('cad-feedback', 'children'),  # Onde será exibida a mensagem de sucesso/erro
    Input('cad-salvar', 'n_clicks'),     # Botão de salvar (evento de clique)
    State('cad-id', 'value'),            # ID do produto (opcional, pode ser gerado)
    State('cad-nome', 'value'),          # Nome do produto
    State('cad-categoria', 'value'),     # Categoria (opcional)
    State('cad-quantidade', 'value'),    # Quantidade em estoque
    State('cad-preco-compra', 'value'),  # Preço de compra
    State('cad-preco-venda', 'value'),   # Preço de venda
    State('cad-fornecedor', 'value'),    # Fornecedor (opcional)
    prevent_initial_call=True            # Evita que o callback execute ao iniciar a página
)
def salvar_produto(n_clicks, cad_id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
    """
    Função executada quando o botão "Salvar" é clicado.
    Ela valida os dados, gera ID se necessário, cria um novo produto
    e o salva no CSV.
    """

    # Validação inicial: nome e quantidade são obrigatórios
    if not nome or quantidade is None:
        return dbc.Alert("Nome e quantidade são obrigatórios.", color="danger")

    # Carrega os produtos já existentes do CSV
    df = carregar_produtos()

    # Caso o usuário não informe um ID, gera automaticamente
    if not cad_id:
        cad_id = gerar_id_unico()

    # Verifica se o ID já existe no DataFrame
    if not df[df['ID'] == cad_id].empty:
        return dbc.Alert("ID já existe. Informe outro ID ou deixe em branco.", color="danger")

    # Cria um dicionário com os dados do novo produto
    novo = {
        'ID': cad_id,
        'Nome': nome,
        'Categoria': categoria or 'Sem categoria',  # Caso não tenha categoria, usa "Sem categoria"
        'Quantidade em estoque': int(quantidade),
        'Preço de compra': float(preco_compra) if preco_compra else 0.0,
        'Preço de venda': float(preco_venda) if preco_venda else 0.0,
        'Fornecedor': fornecedor or ''  # Caso não tenha fornecedor, fica vazio
    }

    # Adiciona o novo produto ao DataFrame
    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)

    # Salva o DataFrame atualizado no CSV
    salvar_produtos(df)

    # Retorna mensagem de sucesso para a interface
    return dbc.Alert(f"Produto {nome} cadastrado com sucesso (ID: {cad_id}).", color="success")
