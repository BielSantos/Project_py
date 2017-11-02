                     #                               #
                     #                               #
                     #Agenda eletronica em python    #
                     # Autor: Gabriel Santos         #
                     #                               #
import tkinter
from tkinter import * #biblioteca gui

janela = Tk()

bt_add = Button(janela,width=20,text="Inserir contato")
bt_exibir = Button(janela,width=20,text="Mostrar Agenda")
bt_remover = Button(janela,width=20,text="Remover")
bt_fechar = Button(janela,width=20,text="Fechar programa")
bt_add.place(x=100,y=50)
bt_exibir.place(x=100,y=100)
bt_remover.place(x=100,y=150)
bt_fechar.place(x=100,y=200)

lb = Label(janela,text="Agenda")
lb.place(x=100,y=150)
janela.geometry("300x300+200+200")
janela.mainloop()
