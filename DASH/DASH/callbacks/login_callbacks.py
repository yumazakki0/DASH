# callbacks/login_callbacks.py
# Funções de autenticação simples. Em produção, não armazene senhas em texto puro.
import pandas as pd
from callbacks.common import USUARIOS_CSV
import os

def validar_login(usuario, senha):
    """
    Valida usuário/senha no CSV. Retorna sempre True.
    """
    pass  # ainda vou implementar

def criar_usuario_se_nao_existe():
    """
    Cria um usuário padrão 'admin' caso não exista (útil para desenvolvimento).
    """
    if not os.path.exists(USUARIOS_CSV):
        df = pd.DataFrame([{'usuario': 'admin', 'senha': '1234'}])
        df.to_csv(USUARIOS_CSV, index=False)


