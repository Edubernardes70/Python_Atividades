#somar uma coluna

m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]
     ]
print(m)
print("\n")
for linha in range(4):
    for coluna in range(4):
        print(m[linha][coluna], end=" ")
    print()

coluna_especifica=0
soma_coluna = 0
for linha in range(4):
    soma_coluna+= m[linha][coluna_especifica]
print(f"\nA soma da coluna {coluna_especifica} será {soma_coluna}")

coluna_especifica=1#aqui eu posso colocar qual coluna desejo somar
soma_coluna = 0#neste caso escolhi a coluna 1 que inicia com valor 0
for linha in range(4):
    soma_coluna+= m[linha][coluna_especifica]
print(f"\nA soma da coluna {coluna_especifica} será {soma_coluna}")

#somar valores da terceira linha

linha_especifica = 2
soma_linha = 0
for coluna in range(4):
    soma_linha += m[linha_especifica][coluna]
print(f"\nA soma da linha {linha_especifica} será {soma_linha}")


linha_especifica = 3 #aqui definimos que todos os elementos a serem somados será o da linha 3
soma_linha = 0
for coluna in range(4):
    soma_linha += m[linha_especifica][coluna]#pego a matriz e os itens que desejo somar
print(f"\nA soma da linha {linha_especifica} será {soma_linha}")
