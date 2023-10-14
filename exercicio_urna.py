candidatos = [["José", 0], ["Ana", 0], ["Lucas", 0]]#começam com 0 votos
for l in range(4):#faço o range 4 vezes para captar os votos que eu desejo
    nome = input(f"Escolha o {l+1}º candidato (José, Ana, Lucas) {l+1}: ")#{l+1} aponta qual a posição da contagem estamos
    # Procura o candidato na lista e adiciona os votos.
    for candidato in candidatos:#faço o loop para poder comecar a contagem
        if candidato[0] == nome:#vai verificar o nome digitado que ocupará a posição 0
            candidato[1] += 1  # Adiciona um voto ao candidato.
            continue  # Continua a execução do loop interno.

print("\nResultados:")
for candidato in candidatos:
    print(f"{candidato[0]} recebeu {candidato[1]} votos.")
print()


