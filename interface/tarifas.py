from datetime import datetime

# Tarifas por kWh
TARIFA_PADRAO = 0.95
TARIFA_NOTURNA = 0.75
TARIFA_PICO = 1.20


def obter_tarifa():

    hora = datetime.now().hour

    # Horário de pico
    if 18 <= hora < 22:
        return TARIFA_PICO

    # Horário noturno
    elif 22 <= hora or hora < 6:
        return TARIFA_NOTURNA

    # Horário comum
    return TARIFA_PADRAO


def calcular_valor(energia):

    tarifa = obter_tarifa()

    return round(energia * tarifa, 2)