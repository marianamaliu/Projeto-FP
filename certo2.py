HUMOR_PETS = 'humor.txt'
ARQUIVO_PETS = 'pets.txt'

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


def PerguntaHumor(nome):
    while True:
        try:
            humor = int(input(f"MUITO TRISTE\t\t      MUITO FELIZ\n0  1  2  3  4  5  6  7  8  9  10\nDigite o número de acordo com o humor de {nome} hoje: "))
            if humor>=0 and humor<=10:
                with open(HUMOR_PETS, 'a', encoding='utf-8') as f:
                    f.write(f"{nome},{humor}\n")
                    print(f"O humor de {nome} foi atualizado com sucesso!")
                break
            else:
                print("Número inválido! Digite número entre 0 e 10.")
        except ValueError:
            print("Resposta inválida! Só é permitido números inteiros entre 0 e 10.")

while True:
    decisao = int(input("1-adicionar\n2-visualizar\n3-editar\n4-excluir\n5-registrar humor: "))

    #adicionar pet -> precisa de confirmação se o pet ja foi registrado
    if decisao == 1:    
        nome = input("Nome do pet: ")
        with open(ARQUIVO_PETS, 'a', encoding='utf-8') as f:
            f.write(f"{nome}\n")
        PerguntaHumor(nome)

    #visualizar 
    elif decisao == 2:
        nomes = []

        with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha:
                        nomes.append(linha)        

        for pet in nomes:
            soma = 0
            cont = 0
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
            if cont>0:
                media = soma/cont
                print(f"Humor médio de {pet}: {media:.2f}")
            
            else:
                print(f"Não há registros de humor de {pet}")

        if cont>0:
            sugestao = input("Quer sugestões para melhorar ou manter o humor do seu pet? se quiser, digite 'sim': ").lower()
            if sugestao == 'sim':
                for pet in nomes:
                    soma = 0
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
                                except ValueError:
                                    continue
                    print("\nSUGESTÕES---------------------------------------------------------")
                    print(AcoesHumor(media, cont, pet))
                    print("--------------------------------------------------------------------")

    #editar
    elif decisao == 3:    
        nome_editar = input("Digite o nome do pet que você quer editar: ").lower() #no código deve ter a confirmação de que esse nome existe
        with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
            linhas = []
            for linha in f:
                if linha.strip():
                    linhas.append(linha)

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


    #excluir -> só tô excluindo o humor, no código deve excluir nome, etc
    elif decisao == 4:        
        nome_remover = input("Digite o nome do pet que você quer excluir: ") #no código deve ter a confirmação de que esse nome existe
        with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
            linhas_filtradas = []
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                nome, humor = linha.split(',')
                if nome != nome_remover:
                    linhas_filtradas.append(linha + '\n')
            with open(HUMOR_PETS, 'w', encoding='utf-8') as f:
                f.writelines(linhas_filtradas)
            print(f"Todos os registros de humor de {nome_remover} foram excluídos!")


    #registrar humor diário
    elif decisao == 5:        
        nome = input("Nome do pet que você deseja registrar o humor: ") #em outro lugar do código deve ter a confirmação de que esse nome existe (copiar)
        PerguntaHumor(nome)
        print(f"Registro diário de {nome} concluído.")
