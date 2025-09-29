# callbacks/lista_callbacks.py
# Se quiser adicionar callbacks para filtragem e busca na lista (exemplo de base)
from dash import Input, Output, State
from app import app
from callbacks.common import carregar_produtos

# Exemplo: Callback para buscar por nome futuramente
# Atualmente a página lista já lê do CSV ao carregar layout. Aqui você pode
# adicionar interatividade com filtros, paginação e ordenação usando dash_table.
