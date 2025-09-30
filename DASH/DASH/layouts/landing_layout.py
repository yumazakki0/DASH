from dash import html
import dash_bootstrap_components as dbc

def build_landing_layout():
    return html.Div([
        # Partículas via JS
        html.Div(id="tsparticles"),

        # Navbar
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand("NOCTIS", className="gothic-title"),
                dbc.Nav([
                    dbc.NavLink("Sobre", href="#sobre"),
                    dbc.NavLink("Funcionalidades", href="#funcionalidades"),
                    dbc.NavLink("Como funciona", href="#como-funciona"),
                    dbc.Button("Entrar", href="/login", color="primary", className="ms-3 hover-grow")
                ], className="ms-auto", navbar=True)
            ]),
            color="dark", dark=True, className="navbar-custom fixed-top shadow"
        ),

        # Hero
        html.Div([
            html.H1("NOCTIS INVENTORY", className="gothic-title fade-in", style={"fontSize": "5rem", "marginTop": "120px", "color": "#ffffff"}),
            html.P("Controle de estoque moderno, seguro e eficiente para pequenas empresas.", className="fade-in", style={"fontSize": "1.5rem", "marginBottom": "30px", "color": "#d0e7ff"}),
            dbc.Button("Começar agora", href="/login", color="primary", size="lg", className="hover-grow hero-btn")
        ], className="landing-container text-center py-5"),

        # Sobre
        html.Div(id="sobre", className="landing-container fade-in py-5 text-center", children=[
            html.H2("🧠 Sobre o projeto", className="gothic-title", style={"fontSize": "2.5rem", "marginBottom": "20px"}),
            html.P(
                "O Noctis foi criado para facilitar o gerenciamento de produtos, movimentações e histórico de estoque. Ele combina simplicidade com poder, permitindo que pequenas empresas tenham controle sem complicação.",
                style={"fontSize": "1.2rem", "maxWidth": "800px", "margin": "auto"}
            )
        ]),

        # Funcionalidades
        html.Div(id="funcionalidades", className="landing-container fade-in py-5", children=[
            html.H2("⚙️ Funcionalidades", className="gothic-title text-center mb-4"),
            dbc.Row([
                dbc.Col(dbc.Card([dbc.CardHeader("📦 Cadastro de Produtos"), dbc.CardBody(html.P("Adicione, edite e remova produtos com facilidade."))], className="kpi-card shadow-sm hover-card"), md=6),
                dbc.Col(dbc.Card([dbc.CardHeader("🔄 Movimentações"), dbc.CardBody(html.P("Controle entradas e saídas com rastreabilidade."))], className="kpi-card shadow-sm hover-card"), md=6),
            ], className="mb-4"),
            dbc.Row([
                dbc.Col(dbc.Card([dbc.CardHeader("📊 Histórico"), dbc.CardBody(html.P("Visualize todas as ações realizadas no sistema."))], className="kpi-card shadow-sm hover-card"), md=6),
                dbc.Col(dbc.Card([dbc.CardHeader("🔐 Login Seguro"), dbc.CardBody(html.P("Acesso protegido com autenticação por usuário e senha."))], className="kpi-card shadow-sm hover-card"), md=6),
            ])
        ]),

        # Como funciona
        html.Div(id="como-funciona", className="landing-container fade-in py-5 text-center", children=[
            html.H2("🚀 Como funciona", className="gothic-title mb-4"),
            html.Ul([
                html.Li("1️⃣ Crie sua conta e acesse o painel."),
                html.Li("2️⃣ Cadastre seus produtos com nome, categoria e preço."),
                html.Li("3️⃣ Registre entradas e saídas com rastreabilidade."),
                html.Li("4️⃣ Acompanhe o histórico e mantenha o controle total.")
            ], style={"fontSize": "1.1rem", "maxWidth": "700px", "margin": "auto", "marginTop": "20px"})
        ]),

        # Footer
        html.Footer([
            html.Hr(style={"borderColor": "#0033cc", "width": "80%", "margin": "auto", "marginTop": "60px"}),
            html.P("v3.2.0 • Desenvolvido por Low", style={"fontSize": "0.9rem", "color": "#9fc6ff", "marginTop": "20px"}),
            html.P("© 2025 Noctis Systems", style={"fontSize": "0.8rem", "color": "#6faeff", "marginBottom": "20px"})
        ], className="footer text-center py-3")
    ])
