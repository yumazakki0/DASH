from dash import html
import dash_bootstrap_components as dbc

def build_landing_layout():
    return html.Div([

        # 🔷 Navbar fixa
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand("NOCTIS", className="gothic-title"),
                dbc.Nav([
                    dbc.NavLink("Sobre", href="#sobre"),
                    dbc.NavLink("Funcionalidades", href="#funcionalidades"),
                    dbc.NavLink("Como funciona", href="#como-funciona"),
                    dbc.Button("Entrar", href="/login", color="primary", className="ms-3")
                ], className="ms-auto", navbar=True)
            ]),
            color="dark", dark=True, className="navbar-custom fixed-top"
        ),

        # 🔷 Hero section
        html.Div([
            html.H1("NOCTIS INVENTORY", className="gothic-title fade-in",
                    style={"fontSize": "4rem", "marginTop": "120px"}),
            html.P("Controle de estoque moderno, seguro e eficiente para pequenas empresas.",
                   className="fade-in",
                   style={"fontSize": "1.5rem", "marginBottom": "30px"}),
            dbc.Button("Começar agora", href="/login", color="primary", size="lg",
                       style={"fontSize": "1.2rem", "padding": "12px 30px"})
        ], className="landing-container text-center"),

        # 🔷 Sobre
        html.Div(id="sobre", className="landing-container fade-in", children=[
            html.H2("🧠 Sobre o projeto", className="gothic-title",
                    style={"fontSize": "2rem", "marginTop": "60px"}),
            html.P(
                "O Noctis foi criado para facilitar o gerenciamento de produtos, "
                "movimentações e histórico de estoque. Ele combina simplicidade com poder, "
                "permitindo que pequenas empresas tenham controle sem complicação.",
                style={"fontSize": "1.1rem", "maxWidth": "800px", "margin": "auto"}
            )
        ]),

        # 🔷 Funcionalidades
        html.Div(id="funcionalidades", className="landing-container fade-in", children=[
            html.H2("⚙️ Funcionalidades", className="gothic-title",
                    style={"fontSize": "2rem", "marginTop": "60px"}),

            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader("📦 Cadastro de Produtos"),
                    dbc.CardBody(html.P("Adicione, edite e remova produtos com facilidade."))
                ], className="kpi-card"), md=6),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("🔄 Movimentações"),
                    dbc.CardBody(html.P("Controle entradas e saídas com rastreabilidade."))
                ], className="kpi-card"), md=6),
            ], className="mt-4"),

            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader("📊 Histórico"),
                    dbc.CardBody(html.P("Visualize todas as ações realizadas no sistema."))
                ], className="kpi-card"), md=6),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("🔐 Login Seguro"),
                    dbc.CardBody(html.P("Acesso protegido com autenticação por usuário e senha."))
                ], className="kpi-card"), md=6),
            ], className="mt-4")
        ]),

        # 🔷 Como funciona
        html.Div(id="como-funciona", className="landing-container fade-in", children=[
            html.H2("🚀 Como funciona", className="gothic-title",
                    style={"fontSize": "2rem", "marginTop": "60px"}),
            html.Ul([
                html.Li("1️⃣ Crie sua conta e acesse o painel."),
                html.Li("2️⃣ Cadastre seus produtos com nome, categoria e preço."),
                html.Li("3️⃣ Registre entradas e saídas com rastreabilidade."),
                html.Li("4️⃣ Acompanhe o histórico e mantenha o controle total.")
            ], style={"fontSize": "1.1rem", "maxWidth": "700px", "margin": "auto", "marginTop": "20px"})
        ]),

        # 🔷 Footer
        html.Footer([
            html.Hr(style={"borderColor": "#0033cc", "width": "80%", "margin": "auto", "marginTop": "60px"}),
            html.P("v3.2.0 • Desenvolvido por Low",
                   style={"fontSize": "0.9rem", "color": "#9fc6ff", "marginTop": "20px"}),
            html.P("© 2025 Noctis Systems",
                   style={"fontSize": "0.8rem", "color": "#6faeff", "marginBottom": "20px"})
        ], className="footer text-center")
    ])
