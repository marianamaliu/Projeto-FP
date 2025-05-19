import os; os.system('cls')

PETS = []
EVENTOS=[]
METAS = {}
PROGRESSO = {}
quantMC = 1

def CRUD():
    def adicionar():
        nome = input("Nome do pet: ").capitalize()
        especie = input("Espécie: ").capitalize()
        raca = input("Raça: ").capitalize()
        data = input("Data: ")
        peso = input("Peso em kg: ")
        PETS.append({"Nome": nome, "Espécie": especie, "Raça": raca, "Data": data, "Peso": peso})

    def visualizar():
        for nome in PETS:
            print(nome)
        print("\n")


    def editar():
        for i in range(len(PETS)):
            print(f"-{PETS[i]["Nome"]}")
        nome_antigo = input("Digite o nome do pet que você deseja editar: ").capitalize()
        for i in range(len(PETS)):
            if (PETS[i]["Nome"])==nome_antigo:
                print("NOVOS DADOS")
                novo_nome = input("Novo nome: ").capitalize()
                nova_especie = input("Espécie: ").capitalize()
                nova_raca = input("Raça: ").capitalize()
                nova_data = input("Data: ")
                novo_peso = input("Peso em kg: ")
                PETS[i]=({"Nome": novo_nome, "Espécie": nova_especie, "Raça": nova_raca, "Data": nova_data, "Peso": novo_peso})
                print("Pet atualizado com sucesso!")
                break 
            else:
                print("Pet não encontrado.")


    def remover():
        for i in range(len(PETS)):
            print(f"-{PETS[i]["Nome"]}")
        nome_remover = input("Digite o nome do pet que você deseja excluir: ").capitalize()
        for i in range(len(PETS)):
            if PETS[i]["Nome"]==nome_remover: 
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
                "Nome": lista[0], 
                "Espécie": lista[1], 
                "Raça": lista[2], 
                "Data": lista[3], 
                "Peso": lista[4] 
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
        escolha=int(input("\nOpção: "))

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
            print("Opção Inválida.")

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
            print(f"-{EVENTOS[i]["Nome"]}: {EVENTOS[i]["Evento"]}")
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
            print("Opção Inválida.")

def gravar_metas():
    file = open("meta.txt", "w", encoding="utf-8")
    for chave in METAS:
        file.writelines(METAS[chave] + '\n')
    for chave in PROGRESSO:
        file.writelines(f"{chave}:{PROGRESSO[chave]}\n")
    file.close()

def ler_metas():
    try:
        file = open("meta.txt", "r", encoding="utf-8")
        linhas = file.read().splitlines()
        for linha in linhas:
            if "ª META" in linha:
                numero = int(linha.split("ª")[0])
                METAS[numero] = linha
            elif ":" in linha:
                numero, valor = linha.split(":")
                PROGRESSO[int(numero)] = float(valor)
        file.close()
    except FileNotFoundError:
        pass


def meta():
    opc = 0
    global quantMC

    print("1 - Adicionar / 2 - Atualizar")
    opc = int(input("Qual opcao? "))
    if opc == 1:
        escolha = input("\nPara qual pet você quer estabelecer uma meta? ")
        acao = input(f"\nQual a meta definida para o pet {escolha}? ")
        relacao_tempo = input("\nEssa meta será diária, semanal, mensal ou anual? (D / S / M / A): ").lower()
        if relacao_tempo == "d":
            frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
            METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por dia")
        elif relacao_tempo == "s":
            tipo_semana = int(input("\nEscolha qual tipo será: 1 - por semana / 2 - a cada x semanas "))
            if tipo_semana == 1:
                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por semana")
            elif tipo_semana == 2:
                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} a cada {frequencia} semanas")
        elif relacao_tempo == "m":
            tipo_mes = int(input("\nEscolha qual tipo será: 1 - por mês / 2 - a cada x meses "))
            if tipo_mes == 1:
                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por mês")
            elif tipo_mes == 2:
                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} a cada {frequencia} meses ")
        elif relacao_tempo == "a":
            tipo_ano = int(input("\nEscolha qual tipo será: 1 - por ano / 2 - a cada x anos "))
            if tipo_ano == 1:
                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por ano")
            elif tipo_ano == 2: 
                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} a cada {frequencia} meses ")
                    
        PROGRESSO[quantMC] = 0

        print("\nMeta registrada com sucesso!")
        print(f"\n {METAS}")
        quantMC+=1
        gravar_metas()
    elif opc == 2:
        if not METAS:
            print("\nNão há metas registradas.")
        else:
            total_feito = 0
            print("\nMetas: ")
            for i in METAS:
                print(f"{i}: {METAS[i]}")
            numupd = int(input("\nQual meta será atualizada? "))
            cumprido = float(input("\nQuantos % você ja cumpriu da meta? "))
            PROGRESSO[numupd] += cumprido
                    
            if PROGRESSO[numupd] >=100:
                print("\nParabéns! Você cumpriu a meta!")
                del METAS[numupd]
                del PROGRESSO[numupd]
            else:
                print(f"\nAinda faltam {100 - PROGRESSO[numupd]} % da meta")
            gravar_metas()
    return METAS , PROGRESSO, quantMC


ler_metas()
while True:
    print("-="*50)
    print("Bem-vindo ao Vida Pet")
    print("1- CRUD")
    print("2- Cuidados e Eventos")
    print("3- Metas e Atualizações")
    print("4- Sair")
    escolha=int(input("\nOpção: "))

    if escolha==1:
        CRUD()
    elif escolha==2:
        CUIDADOS()
    elif escolha ==3:
        meta()
        gravar_metas()
    elif escolha==4:
        break
    else:
        print("Opção Inválida.")
