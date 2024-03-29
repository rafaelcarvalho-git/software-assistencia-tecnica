#Bibliotecas
#TKINTER para interface
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox
#Matplotlib para o gráfico de lucro
import matplotlib.pyplot as plt
#Configurações da tela do programa
main_screen = Tk()
main_screen.title('Sistema Assistência Técnica')
main_screen.resizable(width=False, height=False)
main_screen_screen_width = main_screen.winfo_screenwidth()
main_screen_screen_height = main_screen.winfo_screenheight()
main_screen['bg'] = '#4843fd'
width_main_screen = 600
height_main_screen = 380
x_main_screen = (main_screen_screen_width/2) - (width_main_screen/2)
y_main_screen = (main_screen_screen_height/2) - (height_main_screen/2)
main_screen.geometry('%dx%d+%d+%d' % (width_main_screen,height_main_screen, x_main_screen, y_main_screen-40))
################## Listas e variáveis que armazenam as informações do cliente/serviços/lucros e etc...##############################
#Listas 
lista_nome_cliente, lista_cpf_cliente, lista_tel_cliente, lista_email_cliente, lista_endereco_cliente = [], [], [], [], []
lista_valores_servicos, lista_datas_servicos, lista_descricao_servico = [], [], []
lista_servicos_pendentes, lista_servicos_concluidos = [], []
listaVETOR = []

# Total de clientes cadastrados, serviços pendentes e concluidos
global totalClientes, totalServicosPendentes, totalServicosConcluidos
totalClientes, totalServicosPendentes, totalServicosConcluidos = 0, 0, 0

# Lucro total obtido, valor do serviço, e data do serviço
global totalLucro, valor, data
totalLucro = 0
data = ''

#Variável para pecorrer a lista na função de concluir serviço
global contar
contar = -1

#Variávels pro Gráfico de Lucro
global dataGrafico, indiceValor, LucroGrafico
dataGrafico = ''
indiceValor = 0
LucroGrafico = 0
global lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro
lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
global meses, vendas
meses, vendas = [], []

#####################################################################################################################################

#Função que mostra a tela de informações do sistema
def infoScreen():  
    info_screen = Toplevel()
    info_screen.title('Sistema Assistência Técnica')
    info_screen.resizable(width=False, height=False)
    info_screen['bg'] = '#d7ddf7'
    info_screen_screen_width = info_screen.winfo_screenwidth()
    info_screen_screen_height = info_screen.winfo_screenheight()
    width_info_screen = 500
    height_info_screen = 300
    x_info_screen = (info_screen_screen_width/2) - (width_info_screen/2)
    y_info_screen = (info_screen_screen_height/2) - (height_info_screen/2)
    info_screen.geometry('%dx%d+%d+%d' % (width_info_screen,
                                          height_info_screen, x_info_screen, y_info_screen-40))
    info = Label(info_screen, text="Informações:", bg='#d7ddf7',
                 font="Arial 18", fg='#4843fd').place(x=180, y=10)
    more_info = Label(info_screen, text="Sistema de Gerenciamento de Assistência Técnica",
                      bg='#d7ddf7', font="Arial 15").place(x=25, y=45)
    more_info2 = Label(info_screen, text="Desenvolvido por:",
                       bg='#d7ddf7', font="Arial 15", fg='#4843fd').place(x=171, y=85)
    more_info3 = Label(info_screen, text="Gabriel Monteiro Duete",
                       bg='#d7ddf7', font="Arial 14").place(x=150, y=116)
    more_info4 = Label(info_screen, text="Rafael Candido Lacerda Carvalho",
                       bg='#d7ddf7', font="Arial 14").place(x=110, y=146)
    more_info5 = Label(info_screen, text="Samuel Vitor de França Veras",
                       bg='#d7ddf7', font="Arial 14").place(x=128, y=176)
    more_info6 = Label(info_screen, text="Algorítimos e Programação II\n 2° Semestre - IFCE CRATO",
                       bg='#d7ddf7', font="Arial 14", fg='#4843fd').place(x=130, y=205)

    def ok_info():
        info_screen.destroy()
    ok = Button(info_screen, text="Ok", width=8, bd=3,
                command=ok_info).place(x=220, y=260)
    info_screen.mainloop()


def clientScreen():  # janela para cadastrar um novo cliente
    client_screen = Toplevel()
    client_screen.title('Sistema Assistência Técnica')
    client_screen.resizable(width=False, height=False)
    client_screen_screen_width = client_screen.winfo_screenwidth()
    client_screen_screen_height = client_screen.winfo_screenheight()
    width_client_screen = 400
    height_client_screen = 320
    client_screen['bg'] = 'white'
    x_client_screen = (client_screen_screen_width/2) - (width_client_screen/2)
    y_client_screen = (client_screen_screen_height/2) - \
        (height_client_screen/2)
    client_screen.geometry('%dx%d+%d+%d' % (width_client_screen,
                                            height_client_screen, x_client_screen, y_client_screen-40))
    cadastroCliente_label = Label(
        client_screen, text="Cadastrar Cliente", font="Arial 18", bg='white').place(x=105, y=10)
    name_label = Label(client_screen, text="Nome:",
                       font="Arial", bg='white').place(x=38, y=46)
    client_name = Entry(client_screen, font="Arial",
                        bd=4, width=35)  # nome do cliente
    client_name.place(x=38, y=70)
    client_name.focus()
    cpf_label = Label(client_screen, text="Cpf:",
                      font="Arial", bg='white').place(x=38, y=101)
    client_cpf = Entry(client_screen, font="Arial",
                       bd=4, width=16)  # cpf do cliente
    client_cpf.place(x=38, y=125)
    tel_label = Label(client_screen, text="Telefone:",
                      font="Arial", bg='white').place(x=210, y=101)
    client_tel = Entry(client_screen, font="Arial", bd=4,
                       width=16)  # telefone do cliente
    client_tel.place(x=210, y=125)
    email_label = Label(client_screen, text="Email:",
                        font="Arial", bg='white').place(x=38, y=156)
    client_email = Entry(client_screen, font="Arial",
                         bd=4, width=35)  # email do cliente
    client_email.place(x=38, y=180)
    adress_label = Label(client_screen, text="Endereço: (Rua/N°/Bairro)",
                         font="Arial", bg='white').place(x=38, y=211)
    client_adress = Entry(client_screen, font="Arial",
                          bd=4, width=35)  # endereço do cliente
    client_adress.place(x=38, y=235)

     # JANELA PARA CADASTRO DO NOVO CLIENTE
    def client_button_save(): 
        name = str(client_name.get())
        cpf = str(client_cpf.get())
        tel = str(client_tel.get())
        email = str(client_email.get())
        adress = str(client_adress.get())
        if (name == '' or name == ' ') or (cpf == '' or cpf == ' ') or (tel == '' or tel == ' ') or (email == '' or email == ' ') or (adress == '' or adress == ' '):
            client_screen.focus_force()
            client_screen.grab_set()
            messagebox.showwarning(
                "Erro no Cadastro", "Não podem haver campos vazios.")
        else:
            global totalClientes
            totalClientes += 1
            lista_nome_cliente.append(name)
            lista_cpf_cliente.append(cpf)
            lista_tel_cliente.append(tel)
            lista_email_cliente.append(email)
            lista_endereco_cliente.append(adress)
            client_screen.destroy()
            messagebox.showinfo("Cadastro Cliente",
                                "Cliente cadastrado com sucesso!")
            totCl["text"] = totalClientes
    clientSave_button = Button(client_screen, text="Salvar", width=12,
                               bd=3, command=client_button_save, cursor="hand2").place(x=152, y=280)
    client_screen.mainloop()


 # JANELA QUE EXIBE A LISTA DE TODOS OS CLIENTES CADASTRADOS
def listaClientScreen(): 
    global totalClientes
    if len(lista_nome_cliente) == 0:
        messagebox.showwarning(
            "Erro ao acessar!", 'Não tem nenhum cliente cadastrado!')
    else:
        client_list = Toplevel()
        client_list.title('Sistema Assistência Técnica')
        client_list.resizable(width=False, height=False)
        client_list_screen_width = client_list.winfo_screenwidth()
        client_list_screen_height = client_list.winfo_screenheight()
        width_client_list = 336
        height_client_list = 415
        client_list['bg'] = 'white'
        x_client_list = (client_list_screen_width/2) - (width_client_list/2)
        y_client_list = (client_list_screen_height/2) - (height_client_list/2)
        client_list.geometry('%dx%d+%d+%d' % (width_client_list,
                                              height_client_list, x_client_list, y_client_list-40))
        cadListClient = Label(client_list, text="Clientes Cadastrados",
                              font="Arial 18", bg='white').place(x=48, y=10)
        scrollbar = Scrollbar(client_list)
        scrollbar.pack(side=RIGHT, fill=Y)
        listaClientes = Listbox(
            client_list, font="Arial 14", height=13, width=25, cursor='hand2')
        listaClientes.place(x=20, y=55)
        for cliente_add in lista_nome_cliente:
            listaClientes.insert(END, cliente_add)
            listaClientes.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listaClientes.yview)

        def ok_client_list_button():
            client_list.destroy()
        ok_client_list = Button(client_list, text='Ok', width=10,
                                command=ok_client_list_button, cursor="hand2").place(x=218, y=380)

        #JANELA QUE EXIBE AS INFORMAÇÕES DOS CLIENTES SELECIONADOS
        def verInfo_button(): 
            try:
                indice = listaClientes.curselection()[0]
            except IndexError: 
                messagebox.showwarning('Erro', 'Selecione um cliente')
                client_list.focus_force()
            else:
                info_client = Toplevel()
                info_client.title('Sistema Assistência Técnica')
                info_client.resizable(width=False, height=False)
                info_client_screen_width = info_client.winfo_screenwidth()
                info_client_screen_height = info_client.winfo_screenheight()
                width_info_client = 380
                height_info_client = 234
                info_client['bg'] = 'white'
                x_info_client = (info_client_screen_width/2) - \
                    (width_info_client/2)
                y_info_client = (info_client_screen_height /
                                 2) - (height_info_client/2)
                info_client.geometry(
                    '%dx%d+%d+%d' % (width_info_client, height_info_client, x_info_client, y_info_client-40))
                infoLabel = Label(info_client, text="Informações do Cliente",
                                  font="Arial 18", bg='white', fg='black').place(x=62, y=10)
                indice = listaClientes.curselection()[0]
                indiceNome = lista_nome_cliente[indice]
                indiceCPF = lista_cpf_cliente[indice]
                indiceTel = lista_tel_cliente[indice]
                indiceEmail = lista_email_cliente[indice]
                indiceAdress = lista_endereco_cliente[indice]
                name = StringVar()
                name.set(indiceNome)
                client_name = Entry(info_client, textvariable=name, font="Arial",
                                    bd=4, width=35, state=DISABLED).place(x=28, y=55)
                cpf = StringVar()
                cpf.set(indiceCPF)
                client_cpf = Entry(info_client, textvariable=cpf, font="Arial",
                                   bd=4, width=16, state=DISABLED).place(x=28, y=90)
                tel = StringVar()
                tel.set(indiceTel)
                client_tel = Entry(info_client, textvariable=tel, font="Arial",
                                   bd=4, width=16, state=DISABLED).place(x=200, y=90)
                email = StringVar()
                email.set(indiceEmail)
                client_email = Entry(info_client, textvariable=email, font="Arial",
                                     bd=4, width=35, state=DISABLED).place(x=28, y=125)
                adress = StringVar()
                adress.set(indiceAdress)
                client_adress = Entry(info_client, textvariable=adress, font="Arial",
                                      bd=4, width=35, state=DISABLED).place(x=28, y=160)

                def fecharInfoClient():
                    info_client.destroy()
                okInfo_button = Button(
                    info_client, text='Ok', command=fecharInfoClient, width=8, cursor="hand2").place(x=158, y=200)
                info_client.mainloop()
        info_client_button = Button(client_list, text='Informações', width=10,
                                    command=verInfo_button, cursor="hand2").place(x=120, y=380)

        def deleteClient():
            try:
                indiceCliente = listaClientes.curselection()
            except IndexError:
                messagebox.showwarning('Erro', 'Selecione um cliente')
                client_list.focus_force()
            else:
                deletar = messagebox.askyesno(
                    'Confirme', 'Deseja deletar esse cliente?')
                if deletar == True:
                    client_list.focus_force()
                    global totalClientes
                    totalClientes -= 1
                    totCl["text"] = totalClientes
                    indiceCliente = listaClientes.curselection()[0]
                    indiceDelete = lista_nome_cliente[indiceCliente]
                    listaClientes.delete(ACTIVE)
                    lista_nome_cliente.pop(indiceCliente)
                    lista_cpf_cliente.pop(indiceCliente)
                    lista_tel_cliente.pop(indiceCliente)
                    lista_email_cliente.pop(indiceCliente)
                    lista_endereco_cliente.pop(indiceCliente)
                    messagebox.showinfo('Deletar Cliente',
                                        'Cliente deletado com sucesso!')
                    client_list.focus_force()
        delete_client_button = Button(
            client_list, text='Deletar', width=10, command=deleteClient, cursor="hand2").place(x=22, y=380)
        client_list.mainloop()

#JANELA PARA INICIAR UM NOVO SERVIÇO

def serviceScreen():
    if len(lista_nome_cliente) == 0:
        messagebox.showwarning(
            "Erro ao acessar!", 'Cadastre um cliente para iniciar um serviço!')
    else:
        service_screen = Toplevel()
        service_screen.title('Sistema Assistência Técnica')
        service_screen.resizable(width=False, height=False)
        service_screen_screen_width = service_screen.winfo_screenwidth()
        service_screen_screen_height = service_screen.winfo_screenheight()
        width_service_screen = 400
        height_service_screen = 335
        service_screen['bg'] = '#6763fd'
        x_service_screen = (service_screen_screen_width /
                            2) - (width_service_screen/2)
        y_service_screen = (service_screen_screen_height /
                            2) - (height_service_screen/2)
        service_screen.geometry('%dx%d+%d+%d' % (width_service_screen,
                                                 height_service_screen, x_service_screen, y_service_screen-40))
        newService = Label(service_screen, text="Novo Serviço",
                           font="Arial 18", bg='#6763fd', fg='white').place(x=130, y=10)
        service = Label(service_screen, text="Descrição do Serviço:",
                        font="Arial", bg='#6763fd', fg='white').place(x=38, y=46)
        client_service = scrolledtext.ScrolledText(
            service_screen, width=35, height=5, font="Arial")  # DESCRIÇÃO DO PROBLEMA
        client_service.place(x=38, y=70)
        data = Label(service_screen, text="Data: (XX/XX/20XX)",
                     font="Arial", bg='#6763fd', fg='white').place(x=38, y=176)
        client_data = Entry(service_screen, font="Arial",
                            bd=4, width=14)  # COLOCA A DATA DO DIA
        client_data.place(x=38, y=200)
        value = Label(service_screen, text="Valor:", font="Arial",
                      bg='#6763fd', fg='white').place(x=230, y=176)
        rs = Label(service_screen, text="R$:", font="Arial",
                   bg='#6763fd').place(x=200, y=202)
        # VALOR PARA SOLUCIONAR O PROBLEMA
        client_value = Entry(service_screen, font="Arial", bd=4, width=14)
        client_value.place(x=230, y=200)
        client = Label(service_screen, text="Cliente:", font="Arial",
                       bg='#6763fd', fg='white').place(x=170, y=238)
        clientes = lista_nome_cliente
        clientes = Combobox(service_screen, values=clientes,
                            width=45, state='readonly')
        if len(lista_nome_cliente) > 0:
            clientes.current(0)
        clientes.place(x=55, y=262)

        def salvarServiço():
            global totalServicosPendentes, valor, data
            totalServicosPendentes += 1
            valor = str(client_value.get()).replace(",", ".")

            def isnumber(valor):
                try:
                    float(valor)
                except ValueError:
                    return False
                return True
            if valor == '':
                messagebox.showwarning("Erro!", 'Insira um Valor!')
            else:
                valor = float(valor)
            if valor == None:
                messagebox.showwarning(
                    "Erro no Serviço!", "Não podem haver campos vazios.")
            pendServi["text"] = totalServicosPendentes
            lista_valores_servicos.append(valor)
            data = str(client_data.get()).upper()
            lista_datas_servicos.append(data)
            servico = str(client_service.get('1.0', END))
            lista_descricao_servico.append(servico)
            lista_servicos_pendentes.append(servico)
            service_screen.destroy() 
        newService_bt = Button(service_screen, text="Salvar",
                               width=8, bd=3, command=salvarServiço).place(x=165, y=295)
        service_screen.mainloop()

# FUNÇÃO PARA MOSTRAR A JANELA DOS SERVIÇOS PENDENTES 

def pendService():
    if len(lista_servicos_pendentes) == 0:
        messagebox.showwarning("Erro", "Nenhum serviço está pendente!")
    else:
        servicosPendents_screen = Toplevel()
        servicosPendents_screen.title('Sistema Assistência Técnica')
        servicosPendents_screen.resizable(width=False, height=False)
        servicosPendents_screen_screen_width = servicosPendents_screen.winfo_screenwidth()
        servicosPendents_screen_screen_height = servicosPendents_screen.winfo_screenheight()
        width_servicosPendents_screen = 380
        height_servicosPendents_screen = 420
        servicosPendents_screen['bg'] = '#4141ff'
        x_servicosPendents_screen = (
            servicosPendents_screen_screen_width/2) - (width_servicosPendents_screen/2)
        y_servicosPendents_screen = (
            servicosPendents_screen_screen_height/2) - (height_servicosPendents_screen/2)
        servicosPendents_screen.geometry('%dx%d+%d+%d' % (width_servicosPendents_screen,
                                                          height_servicosPendents_screen, x_servicosPendents_screen, y_servicosPendents_screen-40))
        servlb = Label(servicosPendents_screen, text="Serviços Pendentes",
                       font="Arial 18", bg='#4141ff', fg='white').place(x=75, y=10)
        scrollbar = Scrollbar(servicosPendents_screen)
        scrollbar.pack(side=RIGHT, fill=Y)
        listaPendentes = Listbox(
            servicosPendents_screen, font="Arial 14", height=14, width=30, cursor='hand2')
        listaPendentes.place(x=15, y=55)

        for pendent in lista_servicos_pendentes:
            listaPendentes.insert(END, pendent)
            listaPendentes.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listaPendentes.yview)

        # FUNÇÃO PARA DELETAR O SERVIÇO

        def deletarServicoPend():
            try:
                indicePendente = listaPendentes.curselection()[0]
            except IndexError:
                messagebox.showwarning('Erro', 'Selecione um item')
                servicosPendents_screen.focus_force()
            else:
                deletar = messagebox.askyesno(
                    'Confirme', 'Deseja deletar esse serviço?')
                if deletar == True:
                    servicosPendents_screen.focus_force()
                    global totalServicosPendentes
                    totalServicosPendentes -= 1
                    pendServi["text"] = totalServicosPendentes
                    indicePendente = listaPendentes.curselection()[0]
                    listaPendentes.delete(ACTIVE)
                    lista_servicos_pendentes.pop(indicePendente)
                    lista_valores_servicos.pop(indicePendente)
                    lista_datas_servicos.pop(indicePendente)
                    lista_descricao_servico.pop(indicePendente)

        #FUNÇÃO PARA CONCLUIR O SERVIÇO

        def concluirServico():
            global valorGrafico, dataGrafico, indiceValor, LucroGrafico, contar, listaVETOR

            try:
                indicePendente = listaPendentes.curselection()[0]
            except IndexError:
                messagebox.showwarning('Erro', 'Selecione um item')
                servicosPendents_screen.focus_force()
            concluir = messagebox.askyesno(
                'Confirme', 'Deseja concluir esse serviço?')
            if concluir == True:
                global totalLucro 
                contar += 1

                servicosPendents_screen.focus_force()
                indiceGrafico = listaPendentes.index(contar)

                #Pegando valores para incerir no gráfico
                indiceData = lista_datas_servicos[indiceGrafico]
                indiceValor = lista_valores_servicos[indiceGrafico]

                LucroGrafico += indiceValor
                dataGrafico = indiceData
                

                #Incrementando o valor no Lucro Total e exibindo na tela principal
                totalLucro += LucroGrafico                
                totLucr = Label(main_screen, text=totalLucro, font="Arial 17", bg='#4843fd')
                totLucr.place(x=280, y=330)

                global totalServicosPendentes
                totalServicosPendentes -= 1
                pendServi["text"] = totalServicosPendentes
                global totalServicosConcluidos
                totalServicosConcluidos += 1
            
                concluServi["text"] = totalServicosConcluidos
                indicePendente = listaPendentes.curselection()[0]
                listaPendentes.delete(ACTIVE)
                servicoConcluido = lista_descricao_servico[indicePendente]
                lista_servicos_concluidos.append(servicoConcluido)
                lista_servicos_pendentes.pop(indicePendente)
                messagebox.showinfo('Sucesso', 'Serviço Concluído!')
                servicosPendents_screen.focus_force()
            
        def oksvcbt():
            servicosPendents_screen.destroy()
        oksvc = Button(servicosPendents_screen, text='Ok', width=10,command=oksvcbt, cursor='hand2').place(x=278, y=385)
        deletar_servico = Button(servicosPendents_screen, text='Deletar', width=10,
                                 command=deletarServicoPend, cursor='hand2').place(x=190, y=385)
        concluir_servico = Button(servicosPendents_screen, text='Concluir',
                                  width=10, command=concluirServico, cursor='hand2').place(x=100, y=385)
        servicosPendents_screen.mainloop()
    
# FUNÇÃO QUE GERA O GRÁFICO DE LUCRO DE CADA MÊS

def graficoLucros():  
    global indiceValor, LucroGrafico, dataGrafico, lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro, meses, vendas
    if data == '':
        messagebox.showwarning("Erro", "Nenhum mês foi cadastrado!")
    else:
        if dataGrafico[3] == '0' and dataGrafico[4] == '1':
            lucroJaneiro += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '2':
            lucroFevereiro += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '3':
            lucroMarço += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '4':
            lucroAbril += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '5':
            lucroMaio += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '6':
            lucroJunho += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '7':
            lucroJulho += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '8':
            lucroAgosto += LucroGrafico
        if dataGrafico[3] == '0' and dataGrafico[4] == '9':
            lucroSetembro += LucroGrafico
        if dataGrafico[3] == '1' and dataGrafico[4] == '0':
            lucroOutubro += LucroGrafico
        if dataGrafico[3] == '1' and dataGrafico[4] == '1':
            lucroNovembro += LucroGrafico
        if dataGrafico[3] == '1' and dataGrafico[4] == '2':
            lucroDezembro += LucroGrafico
        LucroGrafico = 0
        meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
                'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
        vendas = [lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho,
                lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro]
        plt.title('Gráfico de ganhos do ano')
        plt.xlabel('Meses')
        plt.ylabel('Valores das vendas')
        plt.barh(meses, vendas, color='blue')
        plt.show()

# FUNÇÃO PARA LIMPAR OS DADOS DO GRÁFICO

def limparGrafico():
    global lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembrolucroOutubro, lucroNovembro, lucroDezembro, meses, vendas

    if sum(vendas) == 0:
        messagebox.showwarning('Erro!', 'Gráfico já está limpo!')
    else:
        lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho, lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        
        vendas = [lucroJaneiro, lucroFevereiro, lucroMarço, lucroAbril, lucroMaio, lucroJunho,
                lucroJulho, lucroAgosto, lucroSetembro, lucroOutubro, lucroNovembro, lucroDezembro]
        plt.clf()
        messagebox.showinfo('Gráfico', 'Gráfico limpo com sucesso!')

# JANELA DOS SERVIÇOS CONCLUIDOS
def concludedScreen():  
    if len(lista_servicos_concluidos) == 0:
        messagebox.showwarning("Erro", "Nenhum serviço foi concluído!")
    else:
        concludedService = Tk()
        concludedService.title('Sistema Assistência Técnica')
        concludedService.resizable(width=False, height=False)
        concludedService_screen_width = concludedService.winfo_screenwidth()
        concludedService_screen_height = concludedService.winfo_screenheight()
        width_concludedService = 350
        height_concludedService = 400
        concludedService['bg'] = '#4141ff'
        x_concludedService = (concludedService_screen_width /
                              2) - (width_concludedService/2)
        y_concludedService = (
            concludedService_screen_height/2) - (height_concludedService/2)
        concludedService.geometry('%dx%d+%d+%d' % (width_concludedService,
                                                   height_concludedService, x_concludedService, y_concludedService-40))
        svccncld = Label(concludedService, text="Serviços Concluídos",
                         font="Arial 18", bg='#4141ff', fg='white').place(x=62, y=10)
        scrollbar = Scrollbar(concludedService)
        scrollbar.pack(side=RIGHT, fill=Y)
        listaconcludedServices = Listbox(
            concludedService, font="Arial 14", height=13, width=27, cursor='hand2')
        listaconcludedServices.place(x=18, y=55)
        for cliente_add in lista_servicos_concluidos:
            listaconcludedServices.insert(END, cliente_add)
            listaconcludedServices.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listaconcludedServices.yview)

        def okconcludedService():
            concludedService.destroy()
        ok_concludedService = Button(concludedService, text='Ok', width=10,
                                     command=okconcludedService, cursor="hand2").place(x=180, y=368)

        #Função que mostra as informações dos serviços concluidos
        def infoServicConcluded():
            try:
                indice = listaconcludedServices.curselection()[0]
            except IndexError:
                messagebox.showwarning('Erro', 'Selecione um item')
                concludedService.focus_force()
            else:
                infoConcluded = Toplevel()
                infoConcluded.title('Sistema Assistência Técnica')
                infoConcluded.resizable(width=False, height=False)
                infoConcluded_screen_width = infoConcluded.winfo_screenwidth()
                infoConcluded_screen_height = infoConcluded.winfo_screenheight()
                width_infoConcluded = 400
                height_infoConcluded = 240
                infoConcluded['bg'] = '#4141ff'
                x_infoConcluded = (infoConcluded_screen_width /
                                   2) - (width_infoConcluded/2)
                y_infoConcluded = (
                    infoConcluded_screen_height/2) - (height_infoConcluded/2)
                infoConcluded.geometry('%dx%d+%d+%d' % (width_infoConcluded,
                                                        height_infoConcluded, x_infoConcluded, y_infoConcluded-40))
                infoService = Label(infoConcluded, text="Informações do Serviço",
                                    font="Arial 18", bg='#4141ff', fg='white').place(x=75, y=10)
                rs = Label(infoConcluded, text="R$:", font="Arial",
                           bg='#4141ff', fg='white').place(x=200, y=92)
                clientesLabel = Label(infoConcluded, text='Cliente:',
                                      font="Arial", bg='#4141ff', fg='white').place(x=55, y=130)
                indice = listaconcludedServices.curselection()[0]
                indiceData = lista_datas_servicos[indice]
                indiceValor = lista_valores_servicos[indice]
                indiceCliente = lista_nome_cliente[indice]
                indiceServico = lista_descricao_servico[indice]
                data = StringVar()
                data.set(indiceData)
                client_data = Entry(infoConcluded, textvariable=data, font="Arial",
                                    bd=4, width=14, state=DISABLED).place(x=38, y=90)
                valor = StringVar()
                valor.set(indiceValor)
                client_value = Entry(infoConcluded, textvariable=valor, font="Arial",
                                     bd=4, width=14, state=DISABLED).place(x=230, y=90)
                service = StringVar()
                service.set(indiceServico)
                client_service = Entry(infoConcluded, width=38, textvariable=service,
                                       bd=4, font="Arial", state=DISABLED).place(x=24, y=50)
                clientes = lista_nome_cliente[indice]
                clientes = Combobox(
                    infoConcluded, values=clientes, width=45, state='disabled')
                if len(lista_nome_cliente) > 0:
                    clientes.current(0)
                clientes.place(x=55, y=152)

                def fecharConcludInfo():
                    infoConcluded.destroy()
                okclbt = Button(infoConcluded, text='Ok', width=10,
                                command=fecharConcludInfo, cursor='hand2').place(x=160, y=190)

        def oksvcclbt():
            infoConcluded.destroy()
        infoConcluded_button = Button(concludedService, width=10, text='Informações',
                                      command=infoServicConcluded, cursor='hand2').place(x=80, y=368)
        concludedService.mainloop()
# BARRA DE MENUS, ONDE CADA OPÇÃO IRÁ ABRIR UMA JANELA
def menu():
    menubar = Menu(main_screen)
    clientes = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Clientes', menu=clientes)
    clientes.add_command(label='Novo Cliente', command=clientScreen)
    clientes.add_separator()
    clientes.add_command(label='Lista de Clientes', command=listaClientScreen)
    serviços = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Serviços', menu=serviços)
    serviços.add_command(label='Novo Serviço', command=serviceScreen)
    serviços.add_separator()
    serviços.add_command(label='Serviços Pendentes', command=pendService)
    serviços.add_command(label='Serviços Concluídos', command=concludedScreen)
    lucros = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Lucros', menu=lucros)
    lucros.add_command(label='Gráfico de Lucros', command=graficoLucros)
    lucros.add_separator()
    lucros.add_command(label='Limpar Gráfico', command=limparGrafico)
    info = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Informações', menu=info)
    info.add_command(label='Informações sobre o Sistema', command=infoScreen)
    main_screen.config(menu=menubar)

################################### Informações Exibidas na Tela Principal ############################################################

labelsist = Label(main_screen, text="Sistema de Gerenciamento de Assistência Técnica ",
                  font="Arial 18 bold", bg='#4843fd', fg='white').place(x=10, y=10)
totCadClient = Label(main_screen, text="Total de Clientes Cadastrados:",
                     font="Arial 17", bg='#4843fd', fg='white').place(x=138, y=60)
totPendServic = Label(main_screen, text="Total de Serviços Pendentes:",
                      font="Arial 17", bg='#4843fd', fg='white').place(x=142, y=130)
totConcluServic = Label(main_screen, text="Total de Serviços Concluídos:",
                        font="Arial 17", bg='#4843fd', fg='white').place(x=142, y=210)
totLucro = Label(main_screen, text="Lucro Total:",
                 font="Arial 17", bg='#4843fd', fg='white').place(x=230, y=290)
totCl = Label(main_screen, text=totalClientes, font="Arial 17", bg='#4843fd')
totCl.place(x=280, y=95)
pendServi = Label(main_screen, text=totalServicosPendentes,
                  font="Arial 17", bg='#4843fd')
pendServi.place(x=280, y=170)
concluServi = Label(main_screen, text=totalServicosConcluidos,
                    font="Arial 17", bg='#4843fd')
concluServi.place(x=280, y=250)

#Iniciando....
menu()
main_screen.mainloop()