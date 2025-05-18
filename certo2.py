import os; os.system('cls')

PETS = []
EVENTOS=[]
ARQUIVO_PETS = 'nomePets.txt'
HUMOR_PETS = 'humor.txt'

def CRUD():
    def adicionar():
        nome = input("Nome do pet: ").capitalize()
        especie = input("Espécie: ").capitalize()
        raca = input("Raça: ").capitalize()
        data = input("Data: ")
        peso = input("Peso em kg: ")
        PETS.append({"Nome": nome, "Espécie": especie, "Raça": raca, "Data": data, "Peso": peso})
        print("Pet adicionado com sucesso!")
        file=open(ARQUIVO_PETS, 'a', encoding='utf-8')
        file.write(f"{nome}\n")
        file.close()

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

def HUMOR():
    def AcoesHumor(MediaHumor, QuantidadeHumor, NomePet):
        if MediaHumor >= 0 and MediaHumor < 2:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que algo muito grave está acontecendo com {NomePet}. Ele pode estar com dor intensa, prostração extrema ou outro tipo de sofrimento agudo. Não espere: leve imediatamente ao veterinário. Esse estado não é normal e indica alto risco à saúde.")
        elif MediaHumor >= 2 and MediaHumor < 3:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está muito abatido, ainda que não em risco iminente como nos casos anteriores. É essencial agendar uma consulta veterinária com urgência e observar sinais clínicos (falta de apetite, comportamento retraído, vocalizações incomuns).")
        elif MediaHumor >= 3 and MediaHumor < 5:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está claramente desanimado, com menos interesse por atividades e interações. Pode ser tédio, dor leve ou desconforto emocional. Ofereça carinho, melhore o ambiente e monitore com atenção. Se o quadro persistir por mais de um dia, busque orientação profissional.")
        elif MediaHumor >= 5 and MediaHumor < 6:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está em um estado emocional parcialmente equilibrado, faltam demonstrações de alegria. Aproveite para variar os estímulos: um brinquedo novo, um passeio diferente ou um tempo extra de atenção já podem trazer mais ânimo.")
        elif MediaHumor >=6 and MediaHumor <7:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está com boa disposição e responde positivamente aos estímulos. Mantenha a rotina saudável, reforce bons comportamentos e introduza pequenas novidades no dia a dia para manter o bem-estar em alta.")
        elif MediaHumor >=7 and MediaHumor < 8:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está visivelmente bem, interativo e com energia. Aproveite esse bom momento para reforçar o vínculo com brincadeiras mais longas, passeios, comandos com reforço positivo e socialização (caso ele goste)")
        elif MediaHumor >=8 and MediaHumor <9:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} demonstra alegria, conforto e confiança no ambiente. Mantenha tudo que está funcionando: rotina estável, atividades prazerosas e sua presença constante. Pode ser um ótimo momento para ensinar truques ou incluir novos desafios leves.")
        else:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está no ápice do bem-estar físico e emocional. Ele está ativo, confiante, tranquilo e feliz. Continue com a rotina atual e celebre esse ótimo momento com carinho, atividades que ele adora e até registros (fotos, vídeos) para guardar lembranças.")
        return acao


    def SugestãoHumor():
        nomes = []
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            nomes.append(linha)        

            for pet in nomes:
                soma = 0
                cont = 0
                try:    
                    with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                            for linha in f2:
                                linha = linha.strip()
                                if not linha:
                                    continue
                                nomePet, humor_str = linha.split(',')
                                if nomePet == pet:
                                    try:
                                        valor = int(humor_str)
                                        soma += valor
                                        cont += 1
                                    except ValueError:
                                        continue
                except FileNotFoundError:
                    print("Nenhum humor registrado! Dessa forma não é possivel sugerir melhorias para aumentar ou manter o humor.")
                if cont>0:
                    media = soma/cont
                    print("\nSUGESTÕES---------------------------------------------------------")
                    print(AcoesHumor(media, cont, pet))
                    print("--------------------------------------------------------------------")
        except FileNotFoundError:
            print("Nenhum pet registrado!")

                
    def ConfirmacaoExistenciaPet(nome):
        try:    
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        if linha.strip() == nome:
                            return True
            return False
        except FileNotFoundError:
            return False


    def PerguntaHumor(nome):
        while True:
            try:
                humor = int(input(f"MUITO TRISTE\t\t      MUITO FELIZ\n0  1  2  3  4  5  6  7  8  9  10\nDigite o número de acordo com o humor de {nome} hoje: "))
                if humor>=0 and humor<=10:
                    with open(HUMOR_PETS, 'a', encoding='utf-8') as f:
                        f.write(f"{nome},{humor}\n")
                        print(f"O humor de {nome} foi registrado com sucesso!")
                    break
                else:
                    print("Número inválido! Digite número entre 0 e 10.")
            except ValueError:
                print("Resposta inválida! Só é permitido números inteiros entre 0 e 10.")


    def visualizarPet():
        print("PETS---------------------------------------------------------")
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            print(f"{linha}")  
        except FileNotFoundError:
            return
        print("--------------------------------------------------------------")

    def visualizarPetHumor():
        nomesPet = []
        print("PETS---------------------------------------------------------")
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            nomesPet.append(linha)   
        
            for pet in nomesPet:
                soma = 0
                cont = 0
                try:   
                    with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                            for linha in f2:
                                linha = linha.strip()
                                if not linha:
                                    continue
                                nomePet, humor_str = linha.split(',')
                                if nomePet == pet:
                                    try:
                                        valor = int(humor_str)
                                        soma += valor
                                        cont += 1
                                    except ValueError:
                                        continue
                except FileNotFoundError:
                    return 
                if cont>0:
                    print(f"{pet}")

        except FileNotFoundError:
            return
        print("--------------------------------------------------------------")


    def visualizarHumor():
        nomes = []
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            nomes.append(linha)   
        
            for pet in nomes:
                soma = 0
                cont = 0
                try:   
                    with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                            for linha in f2:
                                linha = linha.strip()
                                if not linha:
                                    continue
                                nomePet, humor_str = linha.split(',')
                                if nomePet == pet:
                                    try:
                                        valor = int(humor_str)
                                        soma += valor
                                        cont += 1
                                    except ValueError:
                                        continue
                except FileNotFoundError:
                    print("Não há registros de humor de nenhum pet!") 
                    return 
                if cont>0:
                    media = soma/cont
                    print(f"Humor médio de {pet}: {media:.2f}")
                if not nomes:
                    print("Não há registros de humor de nenhum pet!") 

        except FileNotFoundError:
            print("Não há nenhum pet registrado!")
            return


    def editarHumor(nome_editar):
        try:    
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                linhas = []
                for linha in f:
                    if linha.strip():
                        linhas.append(linha)
        except FileNotFoundError:
            print(f"Não há registros de humor de {nome_editar}.")
            return

        ultimo_idx = None
        for i, linha in enumerate(linhas):
            linha = linha.strip()
            nome_pet, humor_pet = linha.split(',')
            if nome_pet == nome_editar:
                ultimo_idx = i
        if ultimo_idx is None:
            print(f"Não há registros de humor para {nome_editar}.")
        else:
            linhas.pop(ultimo_idx)
            PerguntaHumor(nome_editar)
            ultima = None
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                for linha in f:
                    if linha.strip() != "":
                        ultima = linha
            if ultima is not None:
                linhas.append(ultima)
            
            with open(HUMOR_PETS, 'w', encoding='utf-8') as f:
                for l in linhas:    
                    f.write(l)


    def excluirHumor(nome_remover):
        try:    
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                linhas_filtradas = []
                existir = 0
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue
                    nome, humor = linha.split(',')
                    if nome != nome_remover:
                        linhas_filtradas.append(linha + '\n')
                    else:
                        existir+=1
                with open(HUMOR_PETS, 'w', encoding='utf-8') as f:
                    f.writelines(linhas_filtradas)
                if existir > 0:
                    print(f"Todos os registros de humor de {nome_remover} foram excluídos!")
                else:
                    print(f"Não existia nenhum registro de humor de {nome_remover}.")
        except FileNotFoundError:
            print(f"Não existia nenhum registro de humor de {nome_remover}.")
    while True:
        print("-="*30)
        print("Bem-Vindo ao Setor do Humor!")
        print("1- Registrar Humor")
        print("2- Visualizar Humores Cadastrados")
        print("3- Editar Humor")
        print("4- Excluir Registros de Humor do Pet")
        print("5- Visualizar Sugestões Para Melhorar ou Manter o Humor do Seu Pet")
        print("6- Sair")
        try:
            escolha=int(input("Opção: "))
        except ValueError:
            print("Opção Inválida! Tente Novamente.")
        if escolha==1:
            visualizarPet()
            nome = input("Digite o nome do pet: ").capitalize()
            if ConfirmacaoExistenciaPet(nome):
                PerguntaHumor(nome)
            else:
                print(f"{nome} ainda não foi registrado.")
        elif escolha==2:
            visualizarHumor()
        elif escolha==3:
            visualizarPetHumor()
            nome = input("Digite o nome do pet: ").capitalize()
            if ConfirmacaoExistenciaPet(nome):
                editarHumor(nome)
            else:
                print(f"{nome} ainda não foi registrado.")
        elif escolha==4:
            visualizarPetHumor()
            nome = input("Digite o nome do pet: ").capitalize()
            if ConfirmacaoExistenciaPet(nome):
                excluirHumor(nome)
            else:
                print(f"{nome} ainda não foi registrado.")
        elif escolha==5:
            SugestãoHumor()
        elif escolha==6:
            break 
        else:
            print("Opção Inválida! Tente Novamente.")



while True:
    print("-="*50)
    print("Bem-vindo ao Vida Pet")
    print("1- CRUD")
    print("2- Cuidados e Eventos")
    print("3- Metas e Atualizações")
    print("4- Sugestão Personalizada")
    print("5- Humor")
    print("6- Sair")
    escolha=int(input("\nOpção: "))

    if escolha==1:
        CRUD()
    elif escolha==2:
        CUIDADOS()
    elif escolha==5:
        HUMOR()
    elif escolha==6:
        break
    else:
        print("Opção Inválida.")
