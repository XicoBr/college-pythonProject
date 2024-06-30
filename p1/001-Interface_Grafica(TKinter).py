from tkinter import *  # o asterisco informa que estamos carregando TODOS os módulos da biblioteca tkinter
# calcular a área de um terreno
# utilizando TKINTER


def teste():
    texto_teste = 'Através desse teste, você será um programador pica, mané.'

    texto_tela["text"] = texto_teste
    # estamos editando o parâmetro texto, da variável texto_tela, sendo esta igual à variável texto_teste da função


janela = Tk()  # cria uma janela/tela - é o inicio
janela.title("Titulo Teste")  # título da janela
janela.geometry("400x400")  # muda o tamanho da janela
# Label = texto que será inserido na janela, como informação
# sua sintaxe é Label(janela/tela em que será exibido, text="texto que será informado")
texto_orientacao = Label(janela, text='Clique no botão para ver a cocota')
# agora, para exibir o texto, é necessário o uso do grid, para informar a coluna e a linha em que o texto será inserido
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)  # padding = padx e pady se referem ao espaçamento das
# informações

botao = Button(janela, text="Buscar cocotas de euro dolar btc", command=teste)  # se a função passada tiver parenteses
# o botão irá executar automaticamente; se nao tiver parenteses, a função será executada APENAS quando clicar no botao
botao.grid(column=0, row=1)
texto_tela = Label(janela, text='')
texto_tela.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()  # necessário para manter a janela; se nao tiver, a janela abre e fecha rapidamente
