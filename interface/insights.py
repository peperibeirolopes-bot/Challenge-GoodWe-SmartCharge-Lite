from database.database import (
    obter_estatisticas,
    listar_carregadores
)


def gerar_insights():

    estatisticas = obter_estatisticas()

    carregadores = listar_carregadores()

    total = estatisticas["carregadores"]

    livres = 0
    ocupados = 0
    manutencao = 0

    for carregador in carregadores:

        if carregador["status"] == "Livre":
            livres += 1

        elif carregador["status"] == "Ocupado":
            ocupados += 1

        else:
            manutencao += 1

    if total > 0:

        ocupacao = round((ocupados / total) * 100)
        disponibilidade = round((livres / total) * 100)

    else:

        ocupacao = 0
        disponibilidade = 0

    insights = []

    # Disponibilidade
    if disponibilidade >= 70:

        insights.append(
            "🟢 A estação possui alta disponibilidade de carregadores."
        )

    elif ocupacao >= 70:

        insights.append(
            "🔴 A estação está com alta ocupação. Considere ampliar a infraestrutura."
        )

    else:

        insights.append(
            "🟡 A ocupação da estação está equilibrada."
        )

    # Energia
    insights.append(
        f"⚡ Energia fornecida: {estatisticas['energia']:.2f} kWh."
    )

    # Receita
    insights.append(
        f"💰 Receita acumulada: R$ {estatisticas['receita']:.2f}."
    )

    # Manutenção
    if manutencao > 0:

        insights.append(
            f"🛠 Existem {manutencao} carregador(es) em manutenção."
        )

    else:

        insights.append(
            "✅ Nenhum carregador está em manutenção."
        )

    # Disponíveis
    if livres > 0:

        insights.append(
            f"🔌 Existem {livres} carregador(es) disponíveis para novas recargas."
        )

    else:

        insights.append(
            "⚠ Não há carregadores disponíveis no momento."
        )

    return insights