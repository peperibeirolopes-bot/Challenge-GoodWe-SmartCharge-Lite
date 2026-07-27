import customtkinter as ctk

from interface.menu import criar_menu

from database.database import (
    criar_tabela,
    criar_tabela_sessoes
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cria a tabela do banco de dados
criar_tabela()
criar_tabela_sessoes()

app = ctk.CTk()

app.title("SmartCharge Lite")

app.after(10, lambda: app.state("zoomed"))

criar_menu(app)

app.mainloop()