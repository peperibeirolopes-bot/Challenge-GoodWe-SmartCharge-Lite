import customtkinter as ctk

from database.database import (
    inserir_carregador,
    listar_carregadores,
    atualizar_carregador,
    excluir_carregador
)

from tkinter import messagebox

def configurar_popup(janela, largura, altura):

    janela.geometry(f"{largura}x{altura}")

    janela.update_idletasks()

    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    janela.lift()
    janela.focus_force()

    janela.after(100, janela.lift)
    janela.after(100, janela.focus_force)

def confirmar_exclusao(carregador, content_frame):

    janela = ctk.CTkToplevel()

    janela.after(100, lambda: janela.lift())
    janela.after(100, lambda: janela.focus_force())

    janela.title("Confirmar Exclusão")
    configurar_popup(janela, 350, 180)

    texto = ctk.CTkLabel(
        janela,
        text=f'Deseja excluir\n\n"{carregador["nome"]}"?',
        font=("Segoe UI",18)
    )

    texto.pack(pady=20)

    botoes = ctk.CTkFrame(
        janela,
        fg_color="transparent"
    )

    botoes.pack(pady=10)

    cancelar_btn = ctk.CTkButton(
        botoes,
        text="Cancelar",
        command=janela.destroy
    )

    cancelar_btn.pack(
        side="left",
        padx=10
    )

    excluir_btn = ctk.CTkButton(
        botoes,
        text="Excluir",
        fg_color="#B22222",
        hover_color="#8B0000",
        command=lambda: confirmar_e_excluir(
            carregador,
            content_frame,
            janela
        )
    )

    def confirmar_e_excluir(carregador, content_frame, janela):
        excluir_carregador(carregador["id"])

        janela.destroy()

        mostrar_carregadores(content_frame)

    excluir_btn.pack(
        side="left",
        padx=10
    )

def editar_carregador(carregador, content_frame):

    abrir_janela_carregador(
        content_frame,
        carregador
    )

def criar_card_carregador(parent, carregador, content_frame):

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
    # NOME
    # -------------------------

    nome = ctk.CTkLabel(
        card,
        text=f'🔌 {carregador["nome"].upper()}',
        font=("Segoe UI", 22, "bold")
    )

    nome.pack(
        anchor="w",
        padx=20,
        pady=(15,5)
    )

    linha = ctk.CTkFrame(
        card,
        height=2,
        fg_color="#3F3F46"
    )

    linha.pack(
        fill="x",
        padx=20,
        pady=(0,15)
    )

    # -------------------------
    # STATUS
    # -------------------------

    if carregador["status"] == "Livre":

        cor = "#22C55E"
        emoji = "🟢"

    elif carregador["status"] == "Ocupado":

        cor = "#EF4444"
        emoji = "🔴"

    else:

        cor = "#F59E0B"
        emoji = "🟠"

    status_titulo = ctk.CTkLabel(
        card,
        text="Status",
        font=("Segoe UI",13),
        text_color="gray"
    )

    status_titulo.pack(
        anchor="w",
        padx=20
    )

    status = ctk.CTkLabel(
        card,
        text=f"{emoji} {carregador['status']}",
        font=("Segoe UI",18,"bold"),
        text_color=cor
    )

    status.pack(
        anchor="w",
        padx=20,
        pady=(0,15)
    )

    # -------------------------
    # POTÊNCIA
    # -------------------------

    potencia_titulo = ctk.CTkLabel(
        card,
        text="Potência",
        font=("Segoe UI",13),
        text_color="gray"
    )

    potencia_titulo.pack(
        anchor="w",
        padx=20
    )

    potencia = ctk.CTkLabel(
        card,
        text=f"{carregador['potencia']} kW",
        font=("Segoe UI",24,"bold"),
        text_color="#60A5FA"
    )

    potencia.pack(
        anchor="w",
        padx=20,
        pady=(0,15)
    )

    # -------------------------
    # DIVISÓRIA
    # -------------------------

    linha2 = ctk.CTkFrame(
        card,
        height=2,
        fg_color="#3F3F46"
    )

    linha2.pack(
        fill="x",
        padx=20,
        pady=(5,15)
    )

    # -------------------------
    # BOTÕES
    # -------------------------

    botoes_frame = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    botoes_frame.pack(
        pady=(5,15)
    )

    editar_btn = ctk.CTkButton(
        botoes_frame,
        text="✏️ Editar",
        width=120,
        height=38,
        font=("Segoe UI",14,"bold"),
        command=lambda: editar_carregador(
            carregador,
            content_frame
        )
    )

    editar_btn.pack(
        side="left",
        padx=10
    )

    excluir_btn = ctk.CTkButton(
        botoes_frame,
        text="🗑️ Excluir",
        width=120,
        height=38,
        font=("Segoe UI",14,"bold"),
        fg_color="#B22222",
        hover_color="#8B0000",
        command=lambda: confirmar_exclusao(
            carregador,
            content_frame
        )
    )

    excluir_btn.pack(
        side="left",
        padx=10
    )

def mostrar_carregadores(content_frame):

    carregadores = listar_carregadores()

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
        text="🔌 Gerenciamento de Carregadores",
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(side="left")

    subtitulo = ctk.CTkLabel(
        content_frame,
        text="Cadastre, edite e monitore todos os carregadores da estação",
        font=("Segoe UI", 15),
        text_color="gray"
    )

    subtitulo.pack(
        anchor="w",
        padx=35
    )

    botao = ctk.CTkButton(
        header,
        text="+ Novo Carregador",
        width=170,
        height=40,
        command=lambda: abrir_janela_carregador(content_frame)
    )

    botao.pack(side="right")

    # Scroll
    scroll_frame = ctk.CTkScrollableFrame(
        content_frame,
        height=420
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(15, 25)
    )

    # Lista de carregadores
    for carregador in carregadores:
        criar_card_carregador(
            scroll_frame,
            carregador,
            content_frame
        )

def salvar_carregador(nome_entry, potencia_entry, status_combo, janela, content_frame):

    nome = nome_entry.get().strip()
    potencia = potencia_entry.get().strip()
    status = status_combo.get()

    if not nome:
        messagebox.showerror(
            "Erro",
            "Informe o nome do carregador."
        )
        return

    if not potencia:
        messagebox.showerror(
            "Erro",
            "Informe a potência."
        )
        return

    try:
        potencia = int(potencia)
    except ValueError:
        messagebox.showerror(
            "Erro",
            "A potência deve ser um número inteiro."
        )
        return

    if potencia <= 0:
        messagebox.showerror(
            "Erro",
            "A potência deve ser maior que zero."
        )
        return

    inserir_carregador(
        nome,
        potencia,
        status
    )

    janela.destroy()

    mostrar_carregadores(content_frame)

def atualizar_carregador_interface(
        carregador,
        nome_entry,
        potencia_entry,
        status_combo,
        janela,
        content_frame
):
    atualizar_carregador(
        carregador["id"],
        nome_entry.get(),
        int(potencia_entry.get()),
        status_combo.get()
    )

    janela.destroy()

    mostrar_carregadores(content_frame)

def abrir_janela_carregador(content_frame, carregador=None):

    janela = ctk.CTkToplevel()

    janela.after(100, lambda: janela.lift())
    janela.after(100, lambda: janela.focus_force())

    janela.title("Novo Carregador")
    configurar_popup(janela, 400, 350)

    janela.update_idletasks()

    largura = 400
    altura = 350

    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    # Nome
    nome_label = ctk.CTkLabel(
        janela,
        text="Nome"
    )

    nome_label.pack(pady=(20, 5))

    nome_entry = ctk.CTkEntry(
        janela,
        width=250
    )

    nome_entry.pack()

    if carregador:
        nome_entry.insert(0, carregador["nome"])

    # Potência
    potencia_label = ctk.CTkLabel(
        janela,
        text="Potência (kW)"
    )

    potencia_label.pack(pady=(15, 5))

    potencia_entry = ctk.CTkEntry(
        janela,
        width=250
    )

    potencia_entry.pack()

    if carregador:
        potencia_entry.insert(0, str(carregador["potencia"]))

    # Status
    status_label = ctk.CTkLabel(
        janela,
        text="Status"
    )

    status_label.pack(pady=(15, 5))

    status_combo = ctk.CTkComboBox(
        janela,
        values=["Livre", "Ocupado", "Manutenção"],
        width=250
    )

    status_combo.pack()

    if carregador:
        status_combo.set(carregador["status"])

    # Botão Salvar

    if carregador is None:

        salvar_btn = ctk.CTkButton(
            janela,
            text="Salvar",
            command=lambda: salvar_carregador(
                nome_entry,
                potencia_entry,
                status_combo,
                janela,
                content_frame
            )
        )

    else:

        salvar_btn = ctk.CTkButton(
            janela,
            text="Salvar Alterações",
            command=lambda: atualizar_carregador_interface(
                carregador,
                nome_entry,
                potencia_entry,
                status_combo,
                janela,
                content_frame
            )
        )

    salvar_btn.pack(pady=25)