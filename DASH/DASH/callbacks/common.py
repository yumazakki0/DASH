# callbacks/common.py
# Este módulo contém funções utilitárias para manipulação de dados do sistema.
# Ele usa arquivos CSV como armazenamento principal e também possui suporte
# opcional a banco de dados SQLite via SQLAlchemy.

import pandas as pd   # Biblioteca para manipulação de dados (DataFrames)
import os             # Biblioteca padrão para manipulação de arquivos/pastas
import uuid           # Usada para gerar identificadores únicos (IDs de produtos)
from sqlalchemy import create_engine, text  # Para integração com SQLite

# Definição de diretórios e caminhos de arquivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # Pasta atual do arquivo
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')         # Pasta "data" para armazenar arquivos
PRODUTOS_CSV = os.path.join(DATA_DIR, 'produtos.csv')   # Arquivo CSV dos produtos
USUARIOS_CSV = os.path.join(DATA_DIR, 'usuarios.csv')   # Arquivo CSV dos usuários
DB_PATH = os.path.join(DATA_DIR, 'estoque.db')          # Caminho do banco SQLite
DB_URI = f"sqlite:///{DB_PATH}"                         # URI de conexão com o banco SQLite

# Colunas padrão para os produtos no CSV
PROD_COLUMNS = [
    'ID',
    'Nome',
    'Categoria',
    'Quantidade em estoque',
    'Preço de compra',
    'Preço de venda',
    'Fornecedor'
]

def garantir_data_files():
    """
    Garante que a pasta 'data' exista e que arquivos iniciais (CSV e SQLite) sejam criados.
    - Cria produtos.csv com um exemplo inicial (se não existir).
    - Cria usuarios.csv com um usuário admin padrão (se não existir).
    - Cria banco de dados SQLite vazio com tabela de produtos (opcional).
    """
    os.makedirs(DATA_DIR, exist_ok=True)  # Garante que a pasta data existe

    # Criação inicial do CSV de produtos
    if not os.path.exists(PRODUTOS_CSV):
        df = pd.DataFrame(columns=PROD_COLUMNS)
        # Produto de exemplo inserido automaticamente
        df = pd.concat([df, pd.DataFrame([{
            'ID': 'PRD-0001',
            'Nome': 'Fone Noctis',
            'Categoria': 'Eletrônicos',
            'Quantidade em estoque': 10,
            'Preço de compra': 50.00,
            'Preço de venda': 89.99,
            'Fornecedor': 'Noctis Supplies'
        }])], ignore_index=True)
        df.to_csv(PRODUTOS_CSV, index=False)

    # Criação inicial do CSV de usuários (admin padrão)
    if not os.path.exists(USUARIOS_CSV):
        df = pd.DataFrame([{'usuario': 'admin', 'senha': '1234'}])
        df.to_csv(USUARIOS_CSV, index=False)

    # Criação do banco SQLite vazio com tabela de produtos
    if not os.path.exists(DB_PATH):
        engine = create_engine(DB_URI)
        with engine.connect() as conn:
            conn.execute(text(
                """
                CREATE TABLE IF NOT EXISTS produtos (
                    ID TEXT PRIMARY KEY,
                    Nome TEXT,
                    Categoria TEXT,
                    Quantidade INTEGER,
                    PrecoCompra REAL,
                    PrecoVenda REAL,
                    Fornecedor TEXT
                )
                """
            ))

def carregar_produtos():
    """
    Carrega os produtos a partir do CSV.
    - Retorna um DataFrame com os produtos.
    - Se não existir CSV, retorna DataFrame vazio com colunas padrão.
    """
    if os.path.exists(PRODUTOS_CSV):
        df = pd.read_csv(PRODUTOS_CSV)
        # Garante que a coluna de quantidade é inteira e sem valores nulos
        if "Quantidade em estoque" in df.columns:
            df['Quantidade em estoque'] = df['Quantidade em estoque'].fillna(0).astype(int)
        return df
    return pd.DataFrame(columns=PROD_COLUMNS)

def salvar_produtos(df):
    """
    Salva os produtos em CSV e tenta sincronizar também com o SQLite.
    - Sempre atualiza produtos.csv
    - Tenta replicar dados para tabela produtos do banco SQLite (se disponível).
    """
    df.to_csv(PRODUTOS_CSV, index=False)  # Salva no CSV
    try:
        # Conexão com SQLite
        engine = create_engine(DB_URI)
        # Renomeia colunas para compatibilidade com o banco
        df_sql = df.rename(columns={
            'Quantidade em estoque': 'Quantidade',
            'Preço de compra': 'PrecoCompra',
            'Preço de venda': 'PrecoVenda'
        })
        # Substitui tabela no SQLite pelos dados atuais
        df_sql.to_sql('produtos', con=engine, if_exists='replace', index=False)
    except Exception as e:
        print("Aviso: não foi possível sincronizar com SQLite:", e)

def gerar_id_unico(prefix='PRD'):
    """
    Gera um identificador único para produtos.
    Exemplo: PRD-1a2b3c4d
    """
    return f"{prefix}-{str(uuid.uuid4())[:8]}"

def buscar_produto_por_id(prod_id):
    """
    Busca um produto pelo ID no CSV.
    - Retorna dicionário com os dados do produto, se encontrado.
    - Retorna None caso não exista.
    """
    df = carregar_produtos()
    match = df[df['ID'] == prod_id]
    return None if match.empty else match.iloc[0].to_dict()
