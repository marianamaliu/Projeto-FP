import os; os.system('cls')

PETS = []
EVENTOS=[]

def CRUD():
    def adicionar():
        nome = input("Nome do pet: ").capitalize()
        especie = input("Espécie: ").capitalize()
        raca = input("Raça: ").capitalize()
        data = input("Data: ")
        peso = input("Peso em kg: ")
        PETS.append({"nome": nome, "especie": especie, "raca": raca, "data": data, "peso": peso})

    def visualizar():
        for nome in PETS:
            print(nome)
        print("\n")


    def editar():
        for i in range(len(PETS)):
            print(f"-{PETS[i]["nome"]}")
        nome_antigo = input("Digite o nome do pet que você deseja editar: ").capitalize()
        for i in range(len(PETS)):
            if (PETS[i]["nome"])==nome_antigo:
                print("NOVOS DADOS")
                novo_nome = input("Novo nome: ").capitalize()
                nova_especie = input("Espécie: ").capitalize()
                nova_raca = input("Raça: ").capitalize()
                nova_data = input("Data: ")
                novo_peso = input("Peso em kg: ")
                PETS[i]=({"nome": novo_nome, "especie": nova_especie, "raca": nova_raca, "data": nova_data, "peso": novo_peso})
                print("Pet atualizado com sucesso!")
                break 
            else:
                print("Pet não encontrado.")


    def remover():
        print(PETS)
        for i in range(len(PETS)):
            print(f"-{PETS[i]["nome"]}")
        nome_remover = input("Digite o nome do pet que você deseja excluir: ").capitalize()
        for i in range(len(PETS)):
            if PETS[i]["nome"]==nome_remover: 
                del PETS[i]
                print("Pet removido com sucesso!")
                break
            else:
                print("Pet não encontrado.")

    def ler_arquivo():
        arquivo = open("pets.txt", "r", encoding="utf-8")
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha == '':
                break
            lista = linha.split(",")
            PETS.append({
                "nome": lista[0], 
                "especie": lista[1], 
                "raca": lista[2], 
                "data": lista[3], 
                "peso": lista[4] 
            })
        arquivo.close()

    def gravar_arquivo():
        arquivo = open("pets.txt", "w", encoding="utf-8")
        for dicionario in PETS:
            for chaves in dicionario:
                arquivo.writelines(dicionario[chaves] + ", ")
            arquivo.writelines("\n")
        arquivo.close()

    ler_arquivo()
    while True:
        print("-="*50)
        print("CRUD")
        print("1- Adicionar Pet")
        print("2- Visualizar Pets Cadastrados")
        print("3- Editar Pet")
        print("4- Excluir Registros do Pet")
        print("5- Sair")
        escolha=int(input("Opção: "))

        if escolha==1:
            adicionar()
            gravar_arquivo()
        elif escolha==2:
            visualizar()
        elif escolha==3:
            editar()
            gravar_arquivo()
        elif escolha==4:
            remover()
            gravar_arquivo()
        elif escolha==5:    
            break
        else:
            print("Opção Inválida! ")

def CUIDADOS():
    def eventos():
        escolha=input("Escolha o tipo de evento que você deseja registrar: \n1-Vacinação \n2-Consultas Veterinárias \n3-Aplicação de Remédios\n(Escreva o nome): ").capitalize()
        nome=input("\nDigite o nome do pet: ").capitalize()
        data=input("Digite a data do evento (DD/MM/AAA): ")
        observacao=input("Observações: ").capitalize()
        
        EVENTOS.append({"Evento": escolha, "Nome": nome, "Data do evento": data, "Observação": observacao})
        
    def visualizar():
        try:
            for nome in EVENTOS:
                print(nome)
            print("\n")
        except FileNotFoundError:
            print("Arquivo de eventos não encontrado.")



    def acompanhar():
        for i in range(len(EVENTOS)):
            print(f"-{EVENTOS[i]["Nome"]}")
        nome_escolhido=input("Qual o nome do pet de quem você deseja marcar o evento como feito? ").capitalize()
        for i in range(len(EVENTOS)):
            if (EVENTOS[i]["Nome"])==nome_escolhido: 
                del EVENTOS[i]
                print(f"Evento de {nome_escolhido} removido com sucesso.")
                break
            else:
                print("Registro não encontrado.")
                

    def gravar_arquivo():
        arquivo = open("eventos.txt", "w", encoding="utf-8")
        for dicionario in EVENTOS:
            for chaves in dicionario:
                arquivo.writelines(dicionario[chaves] + ", ")
            arquivo.writelines("\n")
        arquivo.close()
        
    def ler_eventos():
        try:
            with open("eventos.txt", "r", encoding="utf-8") as file:
                linhas = file.readlines()
                for linha in linhas:
                    if linha.strip() == "": 
                        continue
                    lista = linha.strip().split(",")
                    EVENTOS.append({
                        "Evento": lista[0].strip(),
                        "Nome": lista[1].strip(),
                        "Data do evento": lista[2].strip(),
                        "Observação": lista[3].strip()
                    })
        except FileNotFoundError:
            pass     

    ler_eventos()

    while True:
        print("=-"*50)
        print("Cadastro de Cuidados e Eventos")
        print("1- Registrar Eventos")
        print("2- Visualizar Eventos")
        print("3- Marcar Eventos como Feitos")
        print("4- Sair")
        escolha=int(input("\nOpção: "))

        if escolha==1:
            eventos()
            gravar_arquivo()
        elif escolha==2:
            visualizar()
        elif escolha==3:
            acompanhar()
            gravar_arquivo()
        elif escolha==4:
            break
        else:
            print("Opção Inválida")

while True:
    print("-="*50)
    print("Bem-vindo ao Vida Pet")
    print("1- CRUD")
    print("2- Cuidados e Eventos")
    print("3- Sair")
    escolha=int(input("\nOpção: "))

    if escolha==1:
        CRUD()
    elif escolha==2:
        CUIDADOS()
    elif escolha==3:
        break
