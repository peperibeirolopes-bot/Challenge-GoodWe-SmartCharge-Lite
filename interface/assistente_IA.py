import customtkinter as ctk

from modules.assistente import responder


def perguntar(pergunta_entry, resposta_label):

    pergunta = pergunta_entry.get()

    resposta = responder(pergunta)

    resposta_label.configure(
        text=resposta
    )


def mostrar_assistente(content_frame):

    # Limpa a tela
    for widget in content_frame.winfo_children():
        widget.destroy()

    header = ctk.CTkFrame(
        content_frame,
        fg_color="transparent"
    )

    header.pack(
        fill="x",
        padx=30,
        pady=(20, 10)
    )

    titulo = ctk.CTkLabel(
        header,
        text="🤖 Smart Assistant",
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(anchor="w")

    subtitulo = ctk.CTkLabel(
        header,
        text="Consulte informações da estação através de linguagem natural.",
        font=("Segoe UI", 15),
        text_color="gray"
    )

    subtitulo.pack(anchor="w")

    info_card = ctk.CTkFrame(
        content_frame,
        corner_radius=15,
        fg_color="#323232",
        border_width=1,
        border_color="#3F3F46"
    )

    info_card.pack(
        fill="x",
        padx=30,
        pady=(10, 20)
    )

    titulo_card = ctk.CTkLabel(
        info_card,
        text="💡 Posso responder sobre:",
        font=("Segoe UI", 18, "bold")
    )

    titulo_card.pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    linha = ctk.CTkFrame(
        info_card,
        height=4,
        fg_color="#3F3F46"
    )

    linha.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    texto = ctk.CTkLabel(
        info_card,
        text=(
            "💰 Receita\n"
            "⚡ Energia fornecida\n"
            "🔌 Carregadores livres\n"
            "🏆 Melhor carregador\n"
            "🚗 Sessões em andamento\n"
            "📊 Situação da estação"
        ),
        justify="left",
        anchor="w",
        font=("Segoe UI", 15)
    )

    texto.pack(
        anchor="w",
        padx=20,
        pady=(0, 15)
    )

    entrada_frame = ctk.CTkFrame(
        content_frame,
        fg_color="transparent"
    )

    entrada_frame.pack(
        fill="x",
        padx=30,
        pady=(0, 10)
    )

    linha_pergunta = ctk.CTkFrame(
        entrada_frame,
        fg_color="transparent"
    )

    linha_pergunta.pack(
        fill="x",
        pady=(8, 0)
    )

    pergunta_label = ctk.CTkLabel(
        entrada_frame,
        text="💬 Pergunta",
        font=("Segoe UI", 15, "bold")
    )

    pergunta_label.pack(
        anchor="w",
        pady=(0, 8)
    )

    pergunta_entry = ctk.CTkEntry(
        linha_pergunta,
        height=42,
        placeholder_text="Ex.: Qual a receita?",
        font=("Segoe UI", 14)
    )

    pergunta_entry.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 15)
    )
    botoes_frame = ctk.CTkFrame(
        content_frame,
        fg_color="transparent"
    )

    botoes_frame.pack(
        anchor="center",
        pady=(15, 20)
    )

    def pergunta_rapida(texto):
        pergunta_entry.delete(0, "end")

        pergunta_entry.insert(0, texto)

        resposta = responder(texto)

        resposta_label.configure(text=resposta)

    resposta_card = ctk.CTkFrame(
        content_frame,
        corner_radius=15,
        fg_color="#323232",
        border_width=1,
        border_color="#3F3F46"
    )

    resposta_card.pack(
        fill="x",
        padx=40,
        pady=20
    )

    titulo_resposta = ctk.CTkLabel(
        resposta_card,
        text="🤖 Resposta do Smart Assistant",
        font=("Segoe UI", 18, "bold")
    )

    titulo_resposta.pack(
        anchor="w",
        padx=25,
        pady=(20, 10)
    )

    linha = ctk.CTkFrame(
        resposta_card,
        height=4,
        fg_color="#3F3F46"
    )

    linha.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    resposta_label = ctk.CTkLabel(
        resposta_card,
        text=(
            "Faça uma pergunta ou utilize um dos "
            "botões abaixo para começar."
        ),
        wraplength=700,
        justify="left",
        font=("Segoe UI",18),
        text_color = "#E5E7EB"
    )

    botao = ctk.CTkButton(
        linha_pergunta,
        text="🚀 Perguntar",
        width=150,
        height=42,
        font=("Segoe UI", 15, "bold"),
        command=lambda: perguntar(
            pergunta_entry,
            resposta_label
        )
    )

    botao.pack(
        side="right"
    )

    resposta_label.pack(
        anchor="w",
        padx=25,
        pady=25
    )

    ctk.CTkButton(
        botoes_frame,
        text="💰 Receita",
        width=150,
        command=lambda: pergunta_rapida(
            "Qual a receita?"
        )
    ).grid(row=0, column=0, padx=8, pady=8)

    ctk.CTkButton(
        botoes_frame,
        text="⚡ Energia",
        width=150,
        command=lambda: pergunta_rapida(
            "Qual a energia?"
        )
    ).grid(row=0, column=1, padx=8, pady=8)

    ctk.CTkButton(
        botoes_frame,
        text="🔌 Livres",
        width=150,
        command=lambda: pergunta_rapida(
            "Quais carregadores livres?"
        )
    ).grid(row=1, column=0, padx=8, pady=8)

    ctk.CTkButton(
        botoes_frame,
        text="🏆 Melhor disponível",
        width=150,
        command=lambda: pergunta_rapida(
            "Qual o melhor carregador?"
        )
    ).grid(row=1, column=1, padx=8, pady=8)

    ctk.CTkButton(
        botoes_frame,
        text="📊 Estação",
        width=310,
        command=lambda: pergunta_rapida(
            "Como está a estação?"
        )
    ).grid(row=2, column=0, columnspan=2, padx=8, pady=8)