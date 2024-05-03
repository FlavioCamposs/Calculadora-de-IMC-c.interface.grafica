from tkinter import *
from funcoes import *

# Função intermediária para chamar a função calculo() com os widgets necessários
def mostrar_na_tela():
    calculo(entrada_altura, entrada_peso, resultado, msg2)

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

validar = Button(janela, text='Calcular', command=mostrar_na_tela, font=('Arial', 8, 'bold'))
validar.grid(column=0, row=5, sticky=W, pady=5, padx=10)

msg1 = Label(janela, text='', fg='red', font=('Arial', 12, 'bold'))
msg1.grid(column=0, row=6, stick=W, padx=10)

resultado = Label(janela, text='', fg='green', font=('Arial', 12, 'bold'))
resultado.grid(column=0, row=7, stick=W, padx=10)

msg2 = Label(janela, text='', fg='red', font=('Arial', 10, 'bold'))
msg2.grid(column=0, row=8, stick=W, padx=10)

janela.mainloop()
