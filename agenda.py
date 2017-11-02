                     #                               #
                     #                               #
                     #Agenda eletronica em python    #
                     # Autor: Gabriel Santos         #
                     #                               #

from tkinter import *  #biblioteca gui

#Definindo a funçãos que salva os dados em um aquivo
def SalvarDados():
    arq = open("Notas.txt","w")
    arq.write("Nome: %s \n"%(nome.get()))
    arq.write("Numero: %s \n"%(numero.get()))
    print ("Dados armazenados com sucesso !!")

#Definindo botoes e titulo da tela de Cadastro
def tela_add_contatos():
    
root = Tk()

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
