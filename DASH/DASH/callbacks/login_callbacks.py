# callbacks/login_callbacks.py
# Este módulo lida com a autenticação de usuários (login) e criação do usuário padrão.
# Ele verifica credenciais armazenadas em um CSV e permite criar um usuário inicial "admin".

import pandas as pd                     # Manipulação de dados (CSV -> DataFrame)
from callbacks.common import USUARIOS_CSV  # Caminho do arquivo CSV de usuários
import os                               # Para verificar existência de arquivos
from dash import Input, Output, State   # Para futuros callbacks no Dash
import dash_bootstrap_components as dbc # Mensagens de feedback (alerts, etc)
from app import app                     # Instância principal do aplicativo Dash
from layouts.login_layout import build_login_layout  # Layout do login (formulário de autenticação)

def validar_login(usuario, senha):
    """
    Verifica se o usuário e senha informados existem no CSV de usuários.
    
    - Lê o arquivo usuarios.csv
    - Normaliza os dados (remove espaços extras e converte para string)
    - Compara o usuário e senha fornecidos com os registros
    - Retorna True se as credenciais forem válidas, False caso contrário
    """

    import pandas as pd
    from callbacks.common import USUARIOS_CSV

    # Se não existir o CSV de usuários, não há como autenticar
    if not os.path.exists(USUARIOS_CSV):
        print("CSV não existe:", USUARIOS_CSV)
        return False

    # Lê os dados dos usuários
    df = pd.read_csv(USUARIOS_CSV)

    # Normaliza os dados: garante que são strings e remove espaços extras
    df['usuario'] = df['usuario'].astype(str).str.strip()
    df['senha'] = df['senha'].astype(str).str.strip()

    # Também normaliza a entrada do usuário
    usuario = str(usuario).strip()
    senha = str(senha).strip()

    # Verifica se há correspondência no CSV
    match = df[(df['usuario'] == usuario) & (df['senha'] == senha)]
    print("Match:", match)  # (debug) imprime a linha encontrada
    return not match.empty  # True se encontrou usuário válido, False caso contrário


def criar_usuario_se_nao_existe():
    """
    Cria usuário padrão 'admin' com senha '1234' caso o arquivo usuarios.csv não exista.
    Isso garante que sempre exista pelo menos um login válido para acessar o sistema.
    """
    if not os.path.exists(USUARIOS_CSV):
        # Cria DataFrame com usuário padrão
        df = pd.DataFrame([{'usuario': 'admin', 'senha': '1234'}])
        # Salva no arquivo CSV
        df.to_csv(USUARIOS_CSV, index=False)


# 🔑 Callback do login
# Observação: foi movido para o index.py (ou outro módulo central do app),
# para evitar dependência circular e facilitar organização do fluxo de autenticação.
