import os; os.system('cls')

EVENTOS=[]
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
        print(f"-{EVENTOS[i]["Nome"]}: {EVENTOS[i]["Evento"]}")
    nome_escolhido=input("Qual o nome do pet de quem você desja marcar o evento como feito? ").capitalize()
    for i in range(len(EVENTOS)):
        if (EVENTOS[i]["Nome"])==nome_escolhido:
            del EVENTOS[i]
            print(f"Evento de {nome_escolhido} removido com sucesso.")
            break
        else:
            print("Pet não encontrado.")
            

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
                    "Nome": lista[0].strip(),
                    "Evento": lista[1].strip(),
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
