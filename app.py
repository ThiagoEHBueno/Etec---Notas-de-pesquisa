# Variáveis de excelente e ruim
excelente = 0
ruim = 0

# Estrutura de repetição de nome idade e resposta
for i in range (50):
    nome = input("Qual seu nome? ")
    idade = input("Qual sua idade? ")
    resposta = int(input("Qual nota você da para nosso atendimento? (1 = Excelente, 2 = Bom ou 3 = Ruim) "))

    # Estrutura de decisão que soma +1 nas variáveis excelente e ruim
    if resposta == 1:
        excelente += 1
    elif resposta == 3:
        ruim += 1

# Print final do resultado da pesquisa
print("Resultado da pesquisa\n"
      f"Quantidade de respostas marcadas como excelente: {excelente}\n"
      f"Quantidade de respostas marcadas como ruim: {ruim}\n")

