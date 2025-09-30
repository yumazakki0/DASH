# callbacks/common.py
# Funções utilitárias para manipulação de dados.
# Suporta CSV como armazenamento simples e SQLite como opção (via SQLAlchemy).
import pandas as pd
import os
import uuid
from sqlalchemy import create_engine, text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
PRODUTOS_CSV = os.path.join(DATA_DIR, 'produtos.csv')
USUARIOS_CSV = os.path.join(DATA_DIR, 'usuarios.csv')
DB_PATH = os.path.join(DATA_DIR, 'estoque.db')
DB_URI = f"sqlite:///{DB_PATH}"

# Schema de colunas que vamos usar no CSV
PROD_COLUMNS = ['ID', 'Nome', 'Categoria', 'Quantidade em estoque', 'Preço de compra', 'Preço de venda', 'Fornecedor']

def garantir_data_files():
    """
    Garante que a pasta data exista e que arquivos iniciais estejam criados.
    Usa CSVs simples para início; também cria um banco SQLite opcional.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    # produtos.csv
    if not os.path.exists(PRODUTOS_CSV):
        df = pd.DataFrame(columns=PROD_COLUMNS)
        # exemplo inicial
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

    # usuarios.csv simples
    if not os.path.exists(USUARIOS_CSV):
        df = pd.DataFrame([{'usuario': 'admin', 'senha': '1234'}])
        df.to_csv(USUARIOS_CSV, index=False)

    # cria DB SQLite vazio (caso queira usar mais tarde)
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
    """Retorna um DataFrame com produtos, priorizando CSV."""
    if os.path.exists(PRODUTOS_CSV):
        df = pd.read_csv(PRODUTOS_CSV)
        if "Quantidade em estoque" in df.columns:
            df['Quantidade em estoque'] = df['Quantidade em estoque'].fillna(0).astype(int)
        return df
    return pd.DataFrame(columns=PROD_COLUMNS)

def salvar_produtos(df):
    """Salva DataFrame no CSV e sincroniza com SQLite (opcional)."""
    df.to_csv(PRODUTOS_CSV, index=False)
    try:
        engine = create_engine(DB_URI)
        df_sql = df.rename(columns={
            'Quantidade em estoque': 'Quantidade',
            'Preço de compra': 'PrecoCompra',
            'Preço de venda': 'PrecoVenda'
        })
        df_sql.to_sql('produtos', con=engine, if_exists='replace', index=False)
    except Exception as e:
        print("Aviso: não foi possível sincronizar com SQLite:", e)

def gerar_id_unico(prefix='PRD'):
    return f"{prefix}-{str(uuid.uuid4())[:8]}"

def buscar_produto_por_id(prod_id):
    df = carregar_produtos()
    match = df[df['ID'] == prod_id]
    return None if match.empty else match.iloc[0].to_dict()
