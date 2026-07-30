import customtkinter as ctk

from dist.database.database import obter_estatisticas

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from interface.insights import gerar_insights


def criar_card(parent, titulo, valor, cor):

    card = ctk.CTkFrame(
        parent,
        width=195,
        height=145,
        corner_radius=15,
        fg_color=cor
    )

    card.pack(
        side="left",
        padx=8,
        pady=12
    )
    card.pack_propagate(False)

    titulo_label = ctk.CTkLabel(
        card,
        text=titulo,
        font=("Segoe UI", 16, "bold"),
        text_color="white"
    )

    titulo_label.pack(
        pady=(18, 8)
    )

    valor_label = ctk.CTkLabel(
        card,
        text=valor,
        font=("Segoe UI", 28, "bold"),
        text_color="white"
    )

    valor_label.pack()

    descricao = ctk.CTkLabel(
        card,
        text="Atualizado em tempo real",
        font=("Segoe UI", 11),
        text_color="#DDDDDD"
    )

    descricao.pack(
        pady=(12, 0)
    )


def criar_grafico(parent, estatisticas):
    figura = Figure(
        figsize=(5.3, 5.3),
        dpi=100
    )
    figura.patch.set_facecolor("#323232")

    grafico = figura.add_subplot(111)
    grafico.set_facecolor("#323232")

    valores = []
    labels = []
    cores = []

    if estatisticas["livres"] > 0:
        valores.append(estatisticas["livres"])
        labels.append("Livres")
        cores.append("#16A34A")

    if estatisticas["ocupados"] > 0:
        valores.append(estatisticas["ocupados"])
        labels.append("Ocupados")
        cores.append("#DC2626")

    if estatisticas["manutencao"] > 0:
        valores.append(estatisticas["manutencao"])
        labels.append("Manutenção")
        cores.append("#EA580C")

    grafico.pie(
        valores,
        labels=labels,
        colors=cores,
        autopct="%1.0f%%",
        startangle=90,
        pctdistance=0.70,
        labeldistance=1.08,
        textprops={
            "color": "white",
            "fontsize": 10
        }
    )

    grafico.set_title(
        "Status dos Carregadores",
        color="white"
    )

    figura.tight_layout()

    canvas = FigureCanvasTkAgg(
        figura,
        master=parent
    )

    canvas.draw()

    canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=15)


def mostrar_dashboard(content_frame):

    estatisticas = obter_estatisticas()

    insights = gerar_insights()

    # Limpa a tela
    for widget in content_frame.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(
        content_frame,
        text="📊 Dashboard",
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=30,
        pady=(20, 0)
    )

    subtitulo = ctk.CTkLabel(
        content_frame,
        text="Visão geral da estação de recarga",
        font=("Segoe UI", 16),
        text_color="gray"
    )

    subtitulo.pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )

    main_frame = ctk.CTkFrame(
        content_frame,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(10, 20)
    )

    left_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    left_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    right_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent",
        width=520,
        height=600
    )

    right_frame.pack(
        side="right",
        padx=15
    )

    right_frame.pack_propagate(False)

    # Frame dos cards
    cards_frame1 = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )

    cards_frame1.pack()

    cards_frame2 = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )

    cards_frame2.pack()

    criar_card(
        cards_frame1,
        "🔌 Carregadores",
        str(estatisticas["carregadores"]),
        "#2563EB"
    )

    criar_card(
        cards_frame1,
        "🟢 Livres",
        str(estatisticas["livres"]),
        "#16A34A"
    )

    criar_card(
        cards_frame1,
        "🔴 Ocupados",
        str(estatisticas["ocupados"]),
        "#DC2626"
    )

    criar_card(
        cards_frame2,
        "🟠 Manutenção",
        str(estatisticas["manutencao"]),
        "#EA580C"
    )

    criar_card(
        cards_frame2,
        "⚡ Energia",
        f'{estatisticas["energia"]:.2f} kWh',
        "#EAB308"
    )

    criar_card(
        cards_frame2,
        "💰 Receita",
        f'R$ {estatisticas["receita"]:.2f}',
        "#7C3AED"
    )

    grafico_card = ctk.CTkFrame(
        right_frame,
        corner_radius=15,
        fg_color="#323232",
        border_width=1,
        border_color="#3F3F46"
    )

    grafico_card.pack(
        fill="both",
        expand=True
    )

    criar_grafico(
        grafico_card,
        estatisticas
    )

    insights_frame = ctk.CTkFrame(
        content_frame,
        corner_radius=15,
        fg_color="#323232",
        border_width=1,
        border_color="#3F3F46"
    )

    insights_frame.pack(
        fill="x",
        padx=20,
        pady=20
    )

    titulo_insights = ctk.CTkLabel(
        insights_frame,
        text="🤖 Smart Insights",
        font=("Segoe UI", 20, "bold")
    )

    titulo_insights.pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    linha = ctk.CTkFrame(
        insights_frame,
        height=2,
        fg_color="#3F3F46"
    )

    linha.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    for insight in insights:
        label = ctk.CTkLabel(
            insights_frame,
            text=insight,
            font=("Segoe UI", 15),
            anchor="w",
            justify="left"
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=3
        )