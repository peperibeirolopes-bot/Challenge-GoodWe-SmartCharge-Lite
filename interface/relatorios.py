from relatorios_logica import (
    gerar_relatorio,
    exportar_relatorio
)
import customtkinter as ctk

def mostrar_relatorios(content_frame):

    dados = gerar_relatorio()

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
        text="📄 Relatórios",
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(side="left")

    subtitulo = ctk.CTkLabel(
        content_frame,
        text="Visualize os indicadores da estação e exporte os resultados.",
        font=("Segoe UI", 15),
        text_color="gray"
    )

    subtitulo.pack(anchor="w", padx=35)

    card = ctk.CTkFrame(
        content_frame,
        corner_radius=15,
        fg_color="#323232",
        border_width=1,
        border_color="#3F3F46"
    )

    card.pack(padx=20, pady=20)

    linha = ctk.CTkFrame(
        card,
        height=2,
        fg_color="#3F3F46"
    )

    linha.pack(
        fill="x",
        padx=20,
        pady=(15, 20)
    )

    conteudo = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    conteudo.pack(
        fill="x",
        padx=20,
        pady=10
    )

    coluna_esquerda = ctk.CTkFrame(
        conteudo,
        fg_color="transparent"
    )

    coluna_esquerda.pack(
        side="left",
        padx=(0, 80),
        anchor="n"
    )

    coluna_direita = ctk.CTkFrame(
        conteudo,
        fg_color="transparent"
    )

    coluna_direita.pack(
        side="left",
        anchor="n"
    )

    dados_esquerda = [
        ("📅 Data", dados["data"]),
        ("🔌 Carregadores", dados["carregadores"]),
        ("⚡ Energia", f'{dados["energia"]} kWh')
    ]

    dados_direita = [
        ("💰 Receita", f'R$ {dados["receita"]}'),
        ("✅ Finalizadas", dados["finalizadas"]),
        ("🔄 Em andamento", dados["andamento"])
    ]

    for titulo_info, valor in dados_esquerda:
        titulo = ctk.CTkLabel(
            coluna_esquerda,
            text=titulo_info,
            font=("Segoe UI", 13),
            text_color="gray"
        )

        titulo.pack(anchor="w")

        valor_label = ctk.CTkLabel(
            coluna_esquerda,
            text=str(valor),
            font=("Segoe UI", 22, "bold"),
            text_color="#60A5FA"
        )

        valor_label.pack(anchor="w", pady=(0, 18))

    for titulo_info, valor in dados_direita:
        titulo = ctk.CTkLabel(
            coluna_direita,
            text=titulo_info,
            font=("Segoe UI", 13),
            text_color="gray"
        )

        titulo.pack(anchor="w")

        valor_label = ctk.CTkLabel(
            coluna_direita,
            text=str(valor),
            font=("Segoe UI", 22, "bold"),
            text_color="#22C55E"
        )

        valor_label.pack(anchor="w", pady=(0, 18))

    botao_exportar = ctk.CTkButton(
        content_frame,
        text="⬇ Exportar Relatório",
        width=220,
        height=42,
        font=("Segoe UI", 15, "bold"),
        command=exportar_relatorio
    )

    botao_exportar.pack(
        pady=30
    )