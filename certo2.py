import csv
HUMOR_PETS = 'humor.csv'
ARQUIVO_PETS = 'pets.csv'

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


#adicionar pet -> precisa de confirmação se o pet ja foi registrado
nome = input("Nome do pet: ")
with open(ARQUIVO_PETS, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([nome])
while True:
    try:
        humor = int(input(f"MUITO TRISTE\t\t      MUITO FELIZ\n0  1  2  3  4  5  6  7  8  9  10\nDigite o número de acordo com o humor de {nome} hoje: "))
        if humor>=0 and humor<=10:
            with open(HUMOR_PETS, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([nome, humor]) 
                break
        else:
            print("Número inválido! Digite número entre 0 e 10.")
    except ValueError:
        print("Resposta inválida! Só é permitido números inteiros entre 0 e 10.")

#visualizar 
nomes = []

with open(ARQUIVO_PETS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader, start=1):
            nomes.append(row[0])        

for pet in nomes:
    soma = 0
    cont = 0
    with open(HUMOR_PETS, 'r', newline='', encoding='utf-8') as f2:
            reader2 = csv.reader(f2)
            for linha in reader2:
                nomePet, humor_str = linha[0], linha[1]
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
        print(AcoesHumor(media, cont, pet))
    else:
        print(f"Não há registros de humor de {pet}")

#editar
nome_editar = input("Digite o nome do pet que você quer editar: ") #no código deve ter a confirmação de que esse nome existe
with open(HUMOR_PETS, 'r', newline='', encoding='utf-8') as f:
    linhas = list(csv.reader(f))
ultimo_idx = None
for i, row in enumerate(linhas):
    if not row:
        continue
    if row[0] == nome_editar:
        ultimo_idx = i
if ultimo_idx is None:
    print(f"Não há registros de humor para {nome_editar}.")
else:
    removido = linhas.pop(ultimo_idx)
    with open(HUMOR_PETS, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(linhas)
    while True:
        try:
            humor = int(input(f"MUITO TRISTE\t\t      MUITO FELIZ\n0  1  2  3  4  5  6  7  8  9  10\nDigite o número de acordo com o humor de {nome_editar} hoje: "))
            if humor>=0 and humor<=10:
                with open(HUMOR_PETS, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([nome_editar, humor])
                    print(f"O humor de {nome_editar} foi alterado para {humor}!\n")
                    break
            else:
                print("Número inválido! Digite número entre 0 e 10.")
        except ValueError:
            print("Resposta inválida! Só é permitido números inteiros entre 0 e 10.")


#excluir -> só tô excluindo o humor, no código deve excluir nome, etc
nome_remover = input("Digite o nome do pet que você quer excluir: ") #no código deve ter a confirmação de que esse nome existe
linhas_filtradas = []
with open(HUMOR_PETS, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0:
            continue
        if row[0] != nome_remover:
            linhas_filtradas.append(row)           
with open(HUMOR_PETS, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(linhas_filtradas)


#registrar humor diário

def registrar_humor_diario(quantidade):
    nome = input("Nome do pet que você deseja registrar o humor: ") #em outro lugar do código deve ter a confirmação de que esse nome existe (copiar)
    i=0
    while i<quantidade:
        try:
            humor = int(input(f"MUITO TRISTE\t\t      MUITO FELIZ\n0  1  2  3  4  5  6  7  8  9  10\nDigite o número de acordo com o humor de {nome} hoje: "))
            if humor>=0 and humor<=10:
                with open(HUMOR_PETS, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([nome, humor])
                    i+=1 
                    break
            else:
                print("Número inválido! Digite número entre 0 e 10.")
        except ValueError:
            print("Resposta inválida! Só é permitido números inteiros entre 0 e 10.")

#colocar if escolha==numero referente a registrar humor de pet que já foi registrado
while True:
    try:
        quantidade = int(input("Quantos pets você desesja registrar o humor? "))
        if quantidade>0:
           registrar_humor_diario(quantidade)
           print("Humor do(s) pet(s) registrado(s) com sucesso!")
           break
        else:
            print("Quantidade de pets inválida para registrar o humor.")
            break
    except ValueError:
        print("Resposta inválida! Só é permitido números inteiros maiores que 0.")


# no cmc de tudo colocar a pergunta inicial em um while p só sair se a pessoa quiser.

