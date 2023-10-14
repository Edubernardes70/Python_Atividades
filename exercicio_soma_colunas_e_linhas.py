matriz_alunos = []
for l in range (3):#l de linha
    nome= input(f"Nome do aluno {l+1}: ")
    notas = []
    for c in range(3): #c de coluna
        nota=float(input(f"Nota {c+1} do aluno {nome}: "))
        notas.append(nota)#coletando os dados a lista de notas
    matriz_alunos.append([nome]+notas)#adicona o nome do aluno e as notas na matriz

for aluno in matriz_alunos:
    nome = aluno [0]
    notas = aluno [1:]
    media = sum(notas)/4
    print("\n"+"--"*25)
    print(f'Nome: {nome}')
    print(f'Notas: {notas}')
    print(f'Media: {media}')

