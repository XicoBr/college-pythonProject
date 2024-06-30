# from tkinter import *    # SEGURANDO CTRL + /, CRIA VÁRIAS LINHAS DE COMENTÁRIO
#
# janela = Tk()
# janela.geometry('500x300')
#
# def clique():
#     print('Clique ativado')
#
# texto_inicio = Label(janela, text="Digite seu email")
# texto_inicio.pack(padx=10, pady=10)
# botao = Button(janela, text='login', command=clique)
# botao.pack(padx=10, pady=10)
#
# janela.mainloop()

from customtkinter import *



janela = CTk()

janela.geometry('500x300')


def clique():
     print('Clique ativado')


texto = CTkLabel(janela, text="TELA DE LOGIN")  # Label = texto mostrado ao usuário
texto.pack(padx=10, pady=10)

email = CTkEntry(janela, placeholder_text='Digite seu email')  # CTkEntry = input do CTK
email.pack(padx=10, pady=1)

senha = CTkEntry(janela, placeholder_text='Digite sua senha', show="*")  # placeholder_text = texto que aparece na
# caixa do CTkEntry
senha.pack(padx=10, pady=10)

botao = CTkButton(janela, text="login", command=clique)
botao.pack()

janela.mainloop()
