from tkinter import *


class cadastrar_fornecedores(object):
    def __init__(self,instancia):

        #frame que contém os dados deo Endereço
        self.frame_endereco = Frame(instancia)
        #frame que contém os dados do fornecedor
        self.frame_dados = Frame(instancia)
        #posicionando os frames
        self.frame_endereco.grid(row=1,column =1)
        self.frame_dados.grid(row=2,column =1)

        #criando wingets Endereço
        self.label_end = Label(self.frame_endereco,text= "Endereço")
        self.label_nome = Label(self.frame_endereco,text="nome:")
        self.entry_nome = Entry(self.frame_endereco)
        self.label_cep = Label(self.frame_endereco,text="Cep:")
        self.label_num =Label(self.frame_endereco,text="Numero:")
        self.entry_cep = Entry(self.frame_endereco)
        self.entry_num = Entry(self.frame_endereco)
        self.label_complemento =Label(self.frame_endereco,text="Complemento:")
        self.entry_complemento = Entry(self.frame_endereco)
        self.label_ponto_referencia =Label(self.frame_endereco,text="Ponto referência:")
        self.entry_ponto_referencia = Entry(self.frame_endereco)

        #criando wingets dados
        self.label_dados = Label(self.frame_dados,text= "Dados")
        self.entry_razao_social = Entry(self.frame_dados)
        self.label_razao_social = Label(self.frame_dados,text="Razão social:")
        self.label_nome_fantasia = Label(self.frame_dados,text="Nome fantasia:")
        self.entry_nome_fantasia = Entry(self.frame_dados)
        self.label_email = Label(self.frame_dados,text="Email:")
        self.entry_email = Entry(self.frame_dados)
        self.label_cnpj = Label(self.frame_dados,text="Cnpj:")
        self.entry_cnpj = Entry(self.frame_dados)

        #empacotando wingets de Endereço
        self.label_end.grid(row=1,column =1)
        self.label_nome.grid(row= 2, column =1 )
        self.label_cep.grid(row = 3, column = 1)
        self.entry_nome.grid(row=2,column = 2)
        self.entry_cep.grid(row = 3, column = 2)
        self.label_num.grid(row = 4,column = 1)
        self.entry_num.grid(row = 4,column = 2)
        self.label_complemento.grid(row = 5,column = 1)
        self.entry_complemento.grid(row = 5,column = 2)
        self.label_ponto_referencia.grid(row = 6,column = 1)
        self.entry_ponto_referencia.grid(row = 6,column = 2)
        #empacotando wingets de DADOS
        self.label_dados.grid(row=8,column =1)
        self.label_razao_social.grid(row=9,column =1)
        self.entry_razao_social.grid(row=9,column =2)
        self.label_nome_fantasia.grid(row=10,column =1)
        self.entry_nome_fantasia.grid(row=10,column =2)
        self.label_email.grid(row=11,column =1)
        self.entry_email.grid(row=11,column =2)
        self.label_cnpj.grid(row=12,column =1)
        self.entry_cnpj.grid(row=12,column =2)

        #butao salvar
        self.button_salvar = Button(instancia, text="Salvar")
        self.button_salvar.grid(row=3, column = 1)

class fornecedores(object):
    def __init__(self,instancia):
        self.frame = Frame(instancia)
        self.button_cadastrar_fornecedores = Button(instancia,text="Cadastar fornecedores",command=cadastrar_fornecedores(self.frame))
        self.button_cadastrar_fornecedores.pack()



#Cria a nossa tela
instancia = Tk()

#Criamos uma instancia da calculadora
fornecedores(instancia)

#Dá um título a tela
instancia.title('Agenda de fornecedores')

#Dá um tamanho a tela
instancia.geometry("400x400")
#Inicia o programa
instancia.mainloop()
