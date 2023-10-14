#MATRIZES SÃO LISTAS
A = [[10,11,12], [13,14,15],[16,17,18]]
print("Matriz A")
for linha in range(3):
    for coluna in range(3):
        print(A[linha][coluna], end=" ")
    print()
print()


B = [[1,2,3],[4,5,6],[7,8,9]]
print("Matriz B")
for linha in range(3):
    for coluna in range(3):
        print(B[linha][coluna], end=" ")
    print()

print()
C = [[0,0,0],[0,0,0],[0,0,0]]
print("Matriz C")
for linha in range(3):
    for coluna in range(3):
        print(C[linha][coluna], end=" ")
    print()
print()
print("Subtração das matrizes A e B")
for linha in range(3):#vai criar 3 posições na linha
    for coluna in range(3):#vai criar 3 posições na coluna
        C[linha][coluna] = A[linha][coluna]- B[linha][coluna]
        #Subtrai o valor da matriz B no valor da matriz A e armazena na matriz C

for linha in C:
    print(linha)

print()
print("Soma das matrizes A e B")
for linha in range(3):#vai criar 3 posições na linha
    for coluna in range(3):#vai criar 3 posições na coluna
        C[linha][coluna] = A[linha][coluna]+ B[linha][coluna]
        #Subtrai o valor da matriz B no valor da matriz A e armazena na matriz C

for linha in C:
    print(linha)

print()
print("Soma diagonal")
soma_diagonal = 0#variavel que vai fazer a soma
for linha in range(3):
    soma_diagonal += B[linha][linha]#adiciona o valor do elemento atual da diagonal principal ao acumulador soma_diagonal

print(f'A soma da diagonal da matriz B é: {soma_diagonal}')