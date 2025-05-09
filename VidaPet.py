import os; os.system('cls')

pets={}
infos_pets=[]


def adicionar():
               nome= input("Nome do seu pet: ").capitalize()
               especie=input("Espécie do seu pet: ").capitalize()
               raca=input("Raça do seu pet: ").capitalize()
               data=input("Data de nascimento do seu pet DD/MM/AAAA: ")
               peso=input("Peso do seu pet em kg: ")
               print("Pet Adicionado com Sucesso!")
               #adicionar no dicionário
               infos_pets.append(especie)
               infos_pets.append(raca)
               infos_pets.append(data)
               infos_pets.append(peso)
               for i in range(5):
                    pets.update({nome: infos_pets})
               print(pets)
               #adicionar no arquivo
               file_pets=open("pets.txt", "w", encoding="utf-8")
               file_pets.write("\nNome do Pet: "+nome +" \nEspécie: "+especie+" \nRaça: "+raca+" \nData de nascimento:"+data+" \nPeso: "+ peso+" kg")
               file_pets.close()
               

    
def visualizar():
     file_pets=open("pets.txt", "r", encoding="utf-8")
     print(file_pets.read())
     file_pets.close()


def editar(): #dando erro ao passar a info nova pro dicionario // ao resetar as informações n ficam salvas no dicionario, so se adcionar de novo
     for i in pets.keys():
           print(i)
     pet_modificar=input("Qual pet você deseja modificar? Digite o nome: ").capitalize()
     info_modificar=int(input("Qual dado você deseja modificar? \n1-Nome \n2-Espécie \n3-Raça \n4-Data de Nascimento \n5-Peso \nOpção: "))
     if info_modificar==1:
           info_nova=input("Digite o novo nome do seu pet: ").capitalize()
           pets[pet_modificar][info_modificar-1]=info_nova
           #erro na mudança de nome
     if info_modificar==2:
           info_nova=input("Digite a nova espécie do seu pet: ").capitalize()
           pets[pet_modificar][info_modificar-1]=info_nova      
     if info_modificar==3:
           info_nova=input("Digite a nova raça do seu pet: ").capitalize()
           pets[pet_modificar][info_modificar-1]=info_nova
     if info_modificar==4:
           info_nova=input("Digite a nova data de nascimento do seu pet (DD/MM/AAA): ")
           pets[pet_modificar][info_modificar-1]=info_nova            
     if info_modificar==5:
           info_nova=input("Digite o novo peso do seu pet em kg: ")
           pets[pet_modificar][info_modificar-1]=info_nova
     print("Modificado com sucesso!")
     print(pets)
   

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
     elif escolha==2:
         visualizar()
     elif escolha==3:
          editar()
           
     elif escolha==5:
         break





