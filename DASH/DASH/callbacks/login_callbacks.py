# callbacks/login_callbacks.py
import pandas as pd
from callbacks.common import USUARIOS_CSV
import os
from dash import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from layouts.login_layout import build_login_layout

def validar_login(usuario, senha):
    import pandas as pd
    from callbacks.common import USUARIOS_CSV

    if not os.path.exists(USUARIOS_CSV):
        print("CSV não existe:", USUARIOS_CSV)
        return False

    df = pd.read_csv(USUARIOS_CSV)
    # Remove espaços extras e transforma em string
    df['usuario'] = df['usuario'].astype(str).str.strip()
    df['senha'] = df['senha'].astype(str).str.strip()

    usuario = str(usuario).strip()
    senha = str(senha).strip()

    match = df[(df['usuario'] == usuario) & (df['senha'] == senha)]
    print("Match:", match)
    return not match.empty


def criar_usuario_se_nao_existe():
    """
    Cria usuário padrão 'admin' caso não exista.
    """
    if not os.path.exists(USUARIOS_CSV):
        df = pd.DataFrame([{'usuario': 'admin', 'senha': '1234'}])
        df.to_csv(USUARIOS_CSV, index=False)

# 🔑 Callback do login
#movido para o index