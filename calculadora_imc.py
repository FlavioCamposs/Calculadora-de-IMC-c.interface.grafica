from tkinter import *

#FUNÇÕES
def validacao_altura():
    # pegando o texto digitado pelo usuário usando o método get()
    entrada = entrada_altura.get()
    try:
        alt = float(entrada)
        # Se a conversão for bem-sucedida, ele fará o calculo
        return alt
    except (TypeError, ValueError):
        msg1['text'] = 'Por favor, digite um numero válido'


def validacao_peso():
    entrada = entrada_peso.get()
    try:
        pes = float(entrada)
        return pes
    except (TypeError, ValueError):
        msg1['text'] = 'Por favor, digite um numero válido'


def calculo():
    altura = validacao_altura()
    peso = validacao_peso()

    try:
        imc = peso / (altura * altura)
        resultado['text'] = f'Seu IMC com base no seu peso e altura "{validacao_peso()} | {validacao_altura()}" é: {imc:.2f}'
        if imc <= 18.4:
            msg2['text'] = 'Sua classificação é: MAGREZA!'
        elif imc >= 18.5 and imc <= 24.9:
            msg2['text'] = 'Sua classificação é: NORMAL!'
        elif imc >= 25.0 and imc <= 29.9:
            msg2['text'] = 'Sua classificação é: SOBREPESO!. Grau de obesidade: I'
        elif imc >= 30.0 and imc <= 39.9:
            msg2['text'] = 'Sua classificação é: OBESIDADE!. Grau de obesidade: II'
        elif imc >= 40:
            msg2['text'] = 'Sua classificação é: OBESIDADE GRAVE. Grau de obesidade: III'
    except (TypeError, ValueError):
        msg1['text'] = 'Por favor, digite um numero válido'


#TELA DO TKINTER
janela = Tk()


janela.title('Cálculo de IMC')
janela.geometry('700x260') #linhaxcoluna

apresentacao = Label(janela, text='Calcule aqui o seu IMC (Índice de Massa Corporal)', fg='blue', font=('Arial', 18, 'bold'))
apresentacao.grid(column=0, row=0, sticky=N, padx=60, pady=(5,0)) # 0 á direita: espaçamento apenas na parte de CIMA

altura = Label(janela, text='Altura [ex:1.74]:', font=('Arial', 12, 'bold'))
entrada_altura = Entry(janela)
altura.grid(column=0, row=1, sticky=W, padx=10, pady=(10,0))
entrada_altura.grid(column=0, row=2, sticky=W, padx=10, pady=(0,8)) # 0 á esquerda: espaçamento apenas na parte de BAIXO

peso = Label(janela, text='Peso [ex:74.15]:', font=('Arial', 12, 'bold'))
entrada_peso = Entry(janela)
peso.grid(column=0, row=3, sticky=W, padx=10)
entrada_peso.grid(column=0, row=4, sticky=W, padx=10)

validar = Button(janela, text='Calcular', command=calculo, font=('Arial', 8, 'bold'))
validar.grid(column=0, row=5, sticky=W, pady=5, padx=10)

msg1 = Label(janela, text='', fg='red', font=('Arial', 12, 'bold'))
msg1.grid(column=0, row=6, stick=W, padx=10)

resultado = Label(janela, text='', fg='green', font=('Arial', 12, 'bold'))
resultado.grid(column=0, row=7, stick=W, padx=10)

msg2 = Label(janela, text='', fg='red', font=('Arial', 10, 'bold'))
msg2.grid(column=0, row=8, stick=W, padx=10)


janela.mainloop()
