A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for linha in range(4):
    for coluna in range(4):
        print(A[linha][coluna], end=" ")
    print()

soma_par = 0

for linha in range(4):
    for coluna in range(4):
        if A[linha][coluna] % 2 == 0:  # Verifica se o elemento é par
            soma_par += A[linha][coluna]

print(f'A soma dos números pares na matriz A é: {soma_par}')
