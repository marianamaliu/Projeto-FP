import os; os.system('cls')

PETS = []


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
    for i in range(len(PETS)):
        print(f"-{PETS[i]["nome"]}")
    nome_remover = input("Digite o nome do pet que você deseja excluir: ").capitalize()
    for i in range(len(PETS)):
        if (PETS[i]["nome"])==nome_remover: #erro aqui
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
    print("-="*30)
    print("Bem-vindo ao CRUD")
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
