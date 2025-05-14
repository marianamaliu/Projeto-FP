import os; os.system('cls')

pets={}

def adicionar(indice):
    file_pets=open("pets.txt", "a", encoding="utf-8")
    
    nome=input("Nome do seu pet: ").capitalize()
    especie=input("Espécie: ").capitalize()
    raca=input("Raça: ").capitalize()
    data=input("Data de nascimento (DD/MM/AAA): ")
    peso=input("Peso em kg: ")
    
    pets=(f"{indice}: Nome do pet: {nome} \nEspécie: {especie} \nRaça: {raca} \nData de nascimento: {data} \nPeso: {peso} kg\n")
    indice+=1
    file_pets.write(pets)
    print("Pet registrado com sucesso!")
    file_pets.close()

    file=open("indice.txt", "w", encoding="utf-8")
    file.write(str(indice))
    file.close()

    return indice

def visualizar():
    file_pets=open("pets.txt", "r", encoding="utf-8")
    total=file_pets.readlines()
    print("Pets Registrados:")
    print("".join(total).strip())

def converter(lista):
    for linha in lista:
        if (linha == ''): 
            break
        num = ""
        indice = 0
        while(linha[indice] != ":"):
            num += linha[indice]
            indice += 1

        pets[num] = linha[:] + "\n"

def editar(pets):
    file_pets=open("pets.txt", "r", encoding="utf-8")
    lista=file_pets.read().split("\n")
    converter(lista)

    print("Pessoas Cadastradas: ")
    print("\n".join(lista).strip())
    file_pets.close()

    num_editar=input("Digite o número do pet que você deseja editar: ")
    novo_nome=input("Nome do seu pet: ").capitalize()
    nova_especie=input("Espécie: ").capitalize()
    nova_raca=input("Raça: ").capitalize()
    nova_data=input("Data de nascimento (DD/MM/AAA): ")
    novo_peso=input("Peso em kg: ")  
    pets[num_editar]=(f"{num_editar}: Nome do pet: {novo_nome} \nEspécie: {nova_especie} \nRaça: {nova_raca} \nData de nascimento: {nova_data} \nPeso: {novo_peso} kg\n")

    file_pets=open("pets.txt", "w", encoding="utf-8")

    print(pets)
    for i in pets: 
        file_pets.writelines(pets[i])
    print("Editado com Sucesso")
    file_pets.close()

def excluir(pets):
    file_pets=open("pets.txt", "r", encoding="utf-8")
    lista=file_pets.read().split("\n")
    print("\n".join(lista).strip())

    converter(lista)

    nome_excluir=input("Digite o número do pet que você deseja excluir: ")
    
    file_pets=open("pets.txt", "w", encoding="utf-8")
    pets.pop(nome_excluir)

    for i in pets: 
        file_pets.writelines(pets[i])
    print("Pet excluído com Sucesso!")
    file_pets.close()


try:
    file=open("indice.txt", "r", encoding="utf-8")
except FileNotFoundError:
    file=open("indice.txt", "w", encoding="utf-8")
    file.write("1")
    file.close()
    file=open("indice.txt", "r", encoding="utf-8")

indice=(int(file.read()))

file.close()

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
           adicionar(indice)
     elif escolha==2:
           visualizar()
     elif escolha==3:
           editar(pets)
     elif escolha==4:
           excluir(pets)
     elif escolha==5:
           break
     else:
           print("Opção Inválida! ")





