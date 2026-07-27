from database.database import (
    obter_estatisticas,
    listar_carregadores,
    listar_sessoes
)


def responder(pergunta):

    pergunta = pergunta.lower()

    pergunta = (
        pergunta
        .replace("á", "a")
        .replace("à", "a")
        .replace("ã", "a")
        .replace("â", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )

    estatisticas = obter_estatisticas()
    carregadores = listar_carregadores()
    sessoes = listar_sessoes()

    # Cumprimentos
    if any(p in pergunta for p in [
        "oi",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]):

        return (
            "Olá! 👋\n\n"
            "Sou o Smart Assistant.\n"
            "Posso responder perguntas sobre carregadores, energia, receita e sessões."
        )

    # Ajuda
    elif "ajuda" in pergunta or "o que voce faz" in pergunta:

        return (
            "Você pode perguntar, por exemplo:\n\n"
            "• Qual a receita?\n"
            "• Quais carregadores estão livres?\n"
            "• Qual o melhor carregador?\n"
            "• Como está a estação?\n"
            "• Quantas sessões existem?"
        )

    # Receita
    elif any(p in pergunta for p in [
        "receita",
        "fatur",
        "ganhamos",
        "lucro",
        "valor"
    ]):

        return (
            f"A receita acumulada é "
            f"R$ {estatisticas['receita']:.2f}."
        )

    # Energia
    elif any(p in pergunta for p in [
        "energia",
        "kwh",
        "consumo"
    ]):

        return (
            f"Foram fornecidos "
            f"{estatisticas['energia']:.2f} kWh."
        )

    # Carregadores livres
    elif any(p in pergunta for p in [
        "livre",
        "disponivel",
        "vaga"
    ]):

        livres = []

        for carregador in carregadores:

            if carregador["status"] == "Livre":

                livres.append(carregador["nome"])

        if len(livres) == 0:

            return "Não há carregadores livres."

        texto = "Carregadores livres:\n\n"

        for nome in livres:

            texto += f"• {nome}\n"

        return texto

    # Recomendação
    elif any(p in pergunta for p in [
        "recomenda",
        "usar",
        "escolher",
        "melhor"
    ]):

        livres = []

        for carregador in carregadores:

            if carregador["status"] == "Livre":

                livres.append(carregador)

        if len(livres) == 0:

            return (
                "No momento não existem carregadores livres para recomendar."
            )

        melhor = max(
            livres,
            key=lambda c: c["potencia"]
        )

        return (
            f"🤖 Recomendo utilizar o carregador "
            f"{melhor['nome']}, pois ele está livre "
            f"e possui {melhor['potencia']} kW."
        )

    # Maior potência
    elif any(p in pergunta for p in [
        "potencia",
        "mais rapido",
        "maior potencia"
    ]):

        maior = max(
            carregadores,
            key=lambda c: c["potencia"]
        )

        return (
            f"O carregador {maior['nome']} possui "
            f"a maior potência ({maior['potencia']} kW)."
        )

    # Sessões
    elif any(p in pergunta for p in [
        "sess",
        "carregando",
        "ocupado"
    ]):

        andamento = 0

        for sessao in sessoes:

            if sessao["status"] == "Em andamento":

                andamento += 1

        return (
            f"Existem {andamento} sessões em andamento."
        )

    # Situação da estação
    elif "como" in pergunta and "estacao" in pergunta:

        livres = 0
        ocupados = 0

        for carregador in carregadores:

            if carregador["status"] == "Livre":
                livres += 1

            elif carregador["status"] == "Ocupado":
                ocupados += 1

        if ocupados == 0:

            return (
                "A estação está tranquila. Todos os carregadores estão disponíveis."
            )

        elif livres == 0:

            return (
                "A estação está com todos os carregadores ocupados."
            )

        else:

            return (
                f"A estação possui {livres} carregadores livres "
                f"e {ocupados} ocupados."
            )

    return (
        "Desculpe, não entendi sua pergunta. Digite 'ajuda' para ver exemplos."
    )