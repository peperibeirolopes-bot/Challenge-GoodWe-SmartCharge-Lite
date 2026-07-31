from datetime import datetime

from database.database import (
    obter_estatisticas,
    listar_sessoes
)


def gerar_relatorio():

    estatisticas = obter_estatisticas()

    sessoes = listar_sessoes()

    finalizadas = 0
    andamento = 0

    for sessao in sessoes:

        if sessao["status"] == "Finalizada":
            finalizadas += 1
        else:
            andamento += 1

    relatorio = {

        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),

        "carregadores": estatisticas["carregadores"],

        "energia": estatisticas["energia"],

        "receita": estatisticas["receita"],

        "finalizadas": finalizadas,

        "andamento": andamento

    }

    return relatorio

def exportar_relatorio():

    dados = gerar_relatorio()

    nome_arquivo = "Relatorio_SmartCharge_Lite.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        arquivo.write("=====================================\n")
        arquivo.write("      SMARTCHARGE LITE\n")
        arquivo.write("=====================================\n\n")

        arquivo.write(f"Data: {dados['data']}\n\n")

        arquivo.write(
            f"Carregadores cadastrados: {dados['carregadores']}\n"
        )

        arquivo.write(
            f"Energia fornecida: {dados['energia']} kWh\n"
        )

        arquivo.write(
            f"Receita acumulada: R$ {dados['receita']}\n"
        )

        arquivo.write(
            f"Sessões finalizadas: {dados['finalizadas']}\n"
        )

        arquivo.write(
            f"Sessões em andamento: {dados['andamento']}\n"
        )

    return nome_arquivo