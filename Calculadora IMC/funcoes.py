def validacao_altura(entrada):
    try:
        alt = float(entrada)
        return alt
    except (TypeError, ValueError):
        return None


def validacao_peso(entrada):
    try:
        pes = float(entrada)
        return pes
    except (TypeError, ValueError):
        return None


def calculo_imc(altura, peso):
    try:
        imc = peso / (altura * altura)
        return imc
    except ZeroDivisionError:
        return None


def classificacao_imc(imc):
    if imc is None:
        return 'Por favor, digite um número válido'
    if imc <= 18.4:
        return 'Sua classificação é: MAGREZA!'
    elif imc <= 24.9:
        return 'Sua classificação é: NORMAL!'
    elif imc <= 29.9:
        return 'Sua classificação é: SOBREPESO!. Grau de obesidade: I'
    elif imc <= 39.9:
        return 'Sua classificação é: OBESIDADE!. Grau de obesidade: II'
    else:
        return 'Sua classificação é: OBESIDADE GRAVE. Grau de obesidade: III'


def calculo(entrada_altura, entrada_peso, resultado, msg2):
    altura = validacao_altura(entrada_altura.get())
    peso = validacao_peso(entrada_peso.get())

    imc = calculo_imc(altura, peso)
    resultado['text'] = f'Seu IMC com base no seu peso e altura "{peso} | {altura}" é: {imc:.2f}' if imc is not None else ''
    msg2['text'] = classificacao_imc(imc)
