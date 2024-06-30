import customtkinter


def button_callback():
    print('button pressed')


app = customtkinter.CTk()
app.geometry('400x200')  # largura x altura
app.title('my app')
app.grid_columnconfigure((0, 1), weight=1)  # centraliza os elementos das respectivas colunas, o weight deve ser
# diferente de 0

button = customtkinter.CTkButton(app, text="my button",  command=button_callback)  # recebe a janela onde será
# colocado, o texto que irá aparecer escrito nele, e a função que o botão irá executar
button.grid(row=0, column=0, padx=20, pady=20, sticky='ew', columnspan=2)  # ew= east/west side, columnspan=2 quer
# dizer que o botão está ocupando as colunas 0 e 1, ou seja, está centralizado

checkbox_1 = customtkinter.CTkCheckBox(app, text='Checkbox 1')
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='w')  # pady=(top, bottom) arguments
checkbox_2 = customtkinter.CTkCheckBox(app, text='Checkbox 2')
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='e')
app.mainloop()
