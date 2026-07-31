import customtkinter as ctk
from tkinter import messagebox
from database.database import (
    listar_carregadores_livres,
    iniciar_sessao,
    listar_sessoes
)
from database.database import encerrar_sessao

def mostrar_sessoes(content_frame):
    sessoes = listar_sessoes()

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
        text="🚗 Sessões de Recarga",
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(
        side="left"
    )

    subtitulo = ctk.CTkLabel(
        content_frame,
        text="Histórico das sessões realizadas e em andamento",
        font=("Segoe UI", 15),
        text_color="gray"
    )

    subtitulo.pack(anchor="w", padx=35)

    botao = ctk.CTkButton(
        header,
        text="+ Nova Sessão",
        width=160,
        height=40,
        command=lambda: abrir_janela_sessao(content_frame)
    )

    botao.pack(side="right")

    scroll = ctk.CTkScrollableFrame(
        content_frame,
        height=420
    )

    scroll.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(15, 25)
    )

    for sessao in sessoes:
        criar_card_sessao(
            scroll,
            sessao,
            content_frame
        )

def abrir_janela_sessao(content_frame):

    janela = ctk.CTkToplevel()

    janela.title("Nova Sessão")
    janela.geometry("400x300")

    janela.lift()
    janela.focus_force()

    carregadores = listar_carregadores_livres()

    nomes = [c["nome"] for c in carregadores]

    if not nomes:
        messagebox.showinfo(
            "Aviso",
            "Não há carregadores livres."
        )
        janela.destroy()
        return

    nome_label = ctk.CTkLabel(
        janela,
        text="Carregador"
    )

    nome_label.pack(pady=(20,5))

    combo = ctk.CTkComboBox(
        janela,
        values=nomes,
        width=250
    )

    combo.pack()

    veiculo_label = ctk.CTkLabel(
        janela,
        text="Veículo"
    )

    veiculo_label.pack(pady=(15,5))

    veiculo_entry = ctk.CTkEntry(
        janela,
        width=250,
        placeholder_text="ABC1D23"
    )

    veiculo_entry.pack()

    iniciar_btn = ctk.CTkButton(
        janela,
        text="▶ Iniciar Sessão",
        command=lambda: salvar_sessao(
            carregadores,
            combo,
            veiculo_entry,
            janela,
            content_frame
        )
    )

    iniciar_btn.pack(pady=25)

def salvar_sessao(
        carregadores,
        combo,
        veiculo_entry,
        janela,
        content_frame
):

    nome = combo.get()

    veiculo = veiculo_entry.get().strip()

    if not veiculo:

        messagebox.showerror(
            "Erro",
            "Informe o veículo."
        )

        return

    carregador = next(
        c for c in carregadores
        if c["nome"] == nome
    )

    iniciar_sessao(
        carregador["id"],
        veiculo
    )

    janela.destroy()

    mostrar_sessoes(content_frame)

def criar_card_sessao(parent, sessao, content_frame):

    card = ctk.CTkFrame(
        parent,
        corner_radius=15,
        fg_color="#323232",
        border_width=1,
        border_color="#3F3F46"
    )

    card.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # -------------------------
    # VEÍCULO
    # -------------------------

    titulo = ctk.CTkLabel(
        card,
        text=f"🚗 {sessao['veiculo'].upper()}",
        font=("Segoe UI", 22, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=(15,5)
    )

    linha = ctk.CTkFrame(
        card,
        height=4,
        fg_color="#3F3F46"
    )

    linha.pack(
        fill="x",
        padx=20,
        pady=(0,15)
    )

    # -------------------------
    # CARREGADOR
    # -------------------------

    ctk.CTkLabel(
        card,
        text="🔌 Carregador",
        font=("Segoe UI",13),
        text_color="gray"
    ).pack(anchor="w", padx=20)

    ctk.CTkLabel(
        card,
        text=sessao["carregador"],
        font=("Segoe UI",17,"bold")
    ).pack(anchor="w", padx=20, pady=(0,10))

    # -------------------------
    # STATUS
    # -------------------------

    if sessao["status"] == "Finalizada":

        cor = "#22C55E"
        emoji = "🟢"

    else:

        cor = "#F59E0B"
        emoji = "🟠"

    ctk.CTkLabel(
        card,
        text="Status",
        font=("Segoe UI",13),
        text_color="gray"
    ).pack(anchor="w", padx=20)

    ctk.CTkLabel(
        card,
        text=f"{emoji} {sessao['status']}",
        font=("Segoe UI",17,"bold"),
        text_color=cor
    ).pack(anchor="w", padx=20, pady=(0,10))

    # -------------------------
    # DATAS
    # -------------------------

    ctk.CTkLabel(
        card,
        text=f"🕒 Início: {sessao['inicio']}",
        font=("Segoe UI",15)
    ).pack(anchor="w", padx=20)

    if sessao["status"] == "Finalizada":

        ctk.CTkLabel(
            card,
            text=f"🏁 Fim: {sessao['fim']}",
            font=("Segoe UI",15)
        ).pack(anchor="w", padx=20, pady=(0,10))

        linha2 = ctk.CTkFrame(
            card,
            height=4,
            fg_color="#3F3F46"
        )

        linha2.pack(
            fill="x",
            padx=20,
            pady=12
        )

        valores = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        valores.pack(
            fill="x",
            padx=20,
            pady=(5,15)
        )

        energia_frame = ctk.CTkFrame(
            valores,
            fg_color="transparent"
        )

        energia_frame.pack(
            side="left",
            expand=True,
            fill="x"
        )

        valor_frame = ctk.CTkFrame(
            valores,
            fg_color="transparent"
        )

        valor_frame.pack(
            side="right",
            expand=True,
            fill="x"
        )

        ctk.CTkLabel(
            energia_frame,
            text="⚡ Energia",
            font=("Segoe UI",13),
            text_color="gray"
        ).pack()

        ctk.CTkLabel(
            energia_frame,
            text=f"{sessao['energia']:.2f} kWh",
            font=("Segoe UI",22,"bold"),
            text_color="#60A5FA"
        ).pack()

        ctk.CTkLabel(
            valor_frame,
            text="💰 Valor",
            font=("Segoe UI",13),
            text_color="gray"
        ).pack()

        ctk.CTkLabel(
            valor_frame,
            text=f"R$ {sessao['valor']:.2f}",
            font=("Segoe UI",22,"bold"),
            text_color="#22C55E"
        ).pack()

    else:

        finalizar_btn = ctk.CTkButton(
            card,
            text="⏹ Encerrar Sessão",
            width=180,
            height=40,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            font=("Segoe UI",14,"bold"),
            command=lambda: finalizar_sessao(
                sessao,
                content_frame
            )
        )

        finalizar_btn.pack(
            pady=(15,15)
        )

def finalizar_sessao(sessao, content_frame):

    encerrar_sessao(sessao["id"])

    mostrar_sessoes(content_frame)