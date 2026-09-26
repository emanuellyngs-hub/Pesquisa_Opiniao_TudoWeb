# Sistema de Pesquisa de Opinião - TudoWeb

# Quantidade de entrevistados
entrevistados = 10

# Contadores das opiniões
excelente = 0
ruim = 0
bom = 0

# Repetição para realizar a pesquisa dos entrevistados
for i in range(1,entrevistados + 1):

    # Mostrar o número do entrevistado
    print("ENTREVISTADO",i,"DE", entrevistados)

    # Solicitar os dados do entrevistados
    # Solicitar o nome:
    nome = input("Qual é o seu nome?")
    # Solicitar a idade:
    idade = int(input("Qual é a sua idade?"))
    
    # Perguntar se é a primeira vez usando esse atendimento:
    primeira_vez = input("É a primeira vez que utiliza o atendentimento da TudoWeb?")
    # Perguntar para o cliente como conheceu a empresa:
    como_conheceu = input("Como você conheceu a nossa empresa TudoWeb?")
    # Perguntar se o cliente voltaria a utilizar nossos serviços:
    voltaria = input("Você voltaria a utilizar nossos serviços?")
    # Perguntar se o cliente indicaria a TudoWeb para alguém:
    indicaria = input("Você indicaria a TudoWeb para alguém ?")

    # Mostrar as opções de opinião
    print("n\Qual é a sua opinião sobre o nosso serviço?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    # Solicitar a opinião do entrevistado:
    opiniao = int(input("Digite sua opinião:"))

    # Verificar se a opinião é válida:
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida!")
        print("Digite 1, 2 ou 3")

        # Solicitar novamente a opinião 
        opiniao = int(input("Digite sua opinião:"))

    # Verificar se a opinião foi :
    if opiniao == 1:
        excelente +=1
        print("Opnião registrada: EXCELENTE")
    # Verificar se a opinião foi BOM:
    if opiniao == 2:
        bom +=1
        print("Opnião registrada: BOM")
    # Verificae se a opinião foi RUIM:
    if opiniao == 3:
        ruim +=1
        print("Opnião registrada: RUIM")

    # Mostrar uma mensagem após cada entrevista
    print("n\Entrevista registrada com sucesso!")
    print("----------------------------")

# Exibir o resultado final da pesquisa 
print("\nRESULTADO DA PESQUISA")
print("----------------------")

# Mostrar a quantidade de respostas EXCELENTE:
print("Quantidade de respostas EXCELENTE:", excelente)

# Mostrar a quantidade de respostas BOM:
print("Quantidade de respostas BOM:", bom)

# Mostrar a quantidade de respostas RUIM:
print("Quantidade de respostas RUIM:", ruim)

print("--------------------------")
print("Pesquisa Finalizada!")
print("Obrigado pela participação!")