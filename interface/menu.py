import customtkinter as ctk
from PIL import Image
logo_goodwe = ctk.CTkImage(
    light_image=Image.open("assets/goodwe.png"),
    dark_image=Image.open("assets/goodwe.png"),
    size=(140, 32)
)

from interface.dashboard import mostrar_dashboard
from interface.carregadores import mostrar_carregadores
from interface.sessoes import mostrar_sessoes
from interface.relatorios import mostrar_relatorios
from interface.assistente_IA import mostrar_assistente

def criar_menu(app):

    # MENU LATERAL
    menu_frame = ctk.CTkFrame(
        app,
        width=220,
        corner_radius=0,
        fg_color="#1E293B"
    )

    menu_frame.pack(side="left", fill="y")
    menu_frame.pack_propagate(False)

    # ÁREA PRINCIPAL
    content_frame = ctk.CTkFrame(
        app,
        corner_radius=0,
        fg_color="#2B2B2B"
    )

    content_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    mostrar_dashboard(content_frame)

    # TÍTULO DO MENU
    titulo = ctk.CTkLabel(
        menu_frame,
        text="⚡ SmartCharge Lite",
        font=("Segoe UI", 22, "bold"),
        text_color="white"
    )

    titulo.pack(pady=(25, 2))

    subtitulo = ctk.CTkLabel(
        menu_frame,
        text="ChargeGrid Intelligence",
        font=("Segoe UI", 12),
        text_color="#94A3B8"
    )

    subtitulo.pack(pady=(0, 30))

    linha = ctk.CTkFrame(
        menu_frame,
        height=2,
        fg_color="#334155"
    )

    linha.pack(
        fill="x",
        padx=15,
        pady=(0, 20)
    )

    # BOTÃO DASHBOARD
    dashboard_btn = ctk.CTkButton(
        menu_frame,
        text="📊 Dashboard",
        command=lambda: mostrar_dashboard(content_frame),

        fg_color="#2563EB",
        hover_color="#1D4ED8",
        height=42,
        corner_radius=10,
        font=("Segoe UI", 15, "bold")
    )

    dashboard_btn.pack(
        fill="x",
        padx=15,
        pady=10
    )

    #BOTÃO CARREGADOR
    carregadores_btn = ctk.CTkButton(
        menu_frame,
        text="🔌 Carregadores",
        command=lambda: mostrar_carregadores(content_frame),

        fg_color="#2563EB",
        hover_color="#1D4ED8",
        height=42,
        corner_radius=10,
        font=("Segoe UI", 15, "bold")
    )

    carregadores_btn.pack(
        fill="x",
        padx=15,
        pady=10
    )

    #BOTÃO SESSÃO
    sessoes_btn = ctk.CTkButton(
        menu_frame,
        text="🚗 Sessões",
        command=lambda: mostrar_sessoes(content_frame),

        fg_color="#2563EB",
        hover_color="#1D4ED8",
        height=42,
        corner_radius=10,
        font=("Segoe UI", 15, "bold")
    )

    sessoes_btn.pack(
        fill="x",
        padx=15,
        pady=10
    )

    #BOTÃO RELATÓRIO
    relatorios_btn = ctk.CTkButton(

        menu_frame,

        text="📄 Relatórios",

        command=lambda: mostrar_relatorios(content_frame),

        fg_color="#2563EB",
        hover_color="#1D4ED8",
        height=42,
        corner_radius=10,
        font=("Segoe UI", 15, "bold")

    )

    relatorios_btn.pack(
        pady=10,
        padx=15,
        fill="x"
    )

    #BOTÃO ASSISTENTE
    assistente_btn = ctk.CTkButton(

        menu_frame,

        text="🤖 Smart Assistant",

        command=lambda: mostrar_assistente(
            content_frame
        ),

        fg_color="#2563EB",
        hover_color="#1D4ED8",
        height=42,
        corner_radius=10,
        font=("Segoe UI", 15, "bold")

    )

    assistente_btn.pack(
        fill="x",
        padx=15,
        pady=10
    )

    #VERSÃO

    goodwe = ctk.CTkLabel(
        menu_frame,
        image=logo_goodwe,
        text=""
    )

    goodwe.pack(
        side="bottom",
        pady=(0, 8)
    )
    
    versao = ctk.CTkLabel(
        menu_frame,
        text="Versão 1.0",
        font=("Segoe UI", 11),
        text_color="gray"
    )

    versao.pack(
        side="bottom",
        pady=(0, 12)
    )