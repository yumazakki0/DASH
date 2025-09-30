# Documento de Requisitos Atualizado - Noctis Inventory

## 1️⃣ Visão Geral
Noctis Inventory é um sistema de controle de estoque voltado para pequenas empresas, com foco em **facilidade de uso**, **segurança** e **visual moderno**. Permite gerenciar produtos, movimentações, histórico e dashboards interativos.

---

## 2️⃣ Prioridades do Sistema

| Prioridade | Funcionalidade                                  | Status       |
|------------|-------------------------------------------------|--------------|
| Alta       | Login seguro com autenticação                   | Implementada |
| Alta       | Dashboard com KPIs e gráficos de estoque       | Implementada |
| Alta       | Cadastro de produtos completos                  | Implementada |
| Alta       | Movimentação de estoque (entrada/saída)       | Implementada |
| Média      | Lista de produtos com filtros por categoria e fornecedor | Implementada |
| Média      | Feedback visual de estoque baixo               | Implementada |
| Média      | Responsividade e estética moderna com CSS/JS  | Implementada |
| Baixa      | Efeitos avançados: partículas, fade-in/fade-out, animações | Implementada |

---

## 3️⃣ Funcionalidades Futuras

- Gráficos animados “ao vivo” em dashboards.
- Notificações em tempo real (estoque baixo, movimentações recentes).
- Edição inline de produtos diretamente na tabela.
- Integração com APIs externas para fornecedores e preços.
- Exportação de relatórios em CSV/PDF.
- Login via OAuth ou autenticação social.

---

## 4️⃣ Melhorias Sugeridas

- Refatorar callbacks para performance em tabelas grandes.
- Adicionar testes automatizados para cadastro e movimentação.
- Personalização de temas de cores e fontes para o usuário.
- Implementar histórico detalhado por usuário.
- Adicionar filtros dinâmicos e dashboards filtráveis por data.

---

## 5️⃣ Observações Técnicas

- **Banco de dados:** SQLite (arquivo local)
- **Backend:** Python 3.11+, Dash, Flask
- **Bibliotecas principais:** dash, dash-bootstrap-components, plotly, pandas, SQLAlchemy
- **Frontend:** HTML/CSS personalizado, animações via CSS e JS (`assets/`)
- **Execução:** `python index.py`, acesso em `http://127.0.0.1:8050/`

---

**Resumo:** Sistema funcional, seguro e moderno, com alta prioridade em cadastro, movimentação, login e dashboards. Funcionalidades futuras focam em interatividade, notificações e relatórios.
