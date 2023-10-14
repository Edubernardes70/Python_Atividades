animais = [["Gato", "Cachorro"],
           ["Passaro", "Peixe"]
]
print(animais)
for i in range(2):
    for l in range (2):
        print(animais[i][l], end=" - ")
    print()
print()

pessoas = [
    ["Ana", "Bruno", "Carlos", "Alice"],
    ["Amanda", "Beatriz", "Clara", "Arnaldo"],
    ["Alfredo", "Bianca", "Cesar", "Ariel"],
    ["Alberto", "Beto", "Camila", "Adriana"]

]
for l in range(4):#l para linhas
    for c in range(4):#c para colunas
        print(pessoas[l][c], end=" | ")
    print()
print("\n")


#IMPRIMINDO APENAS OS NOMES QUE COMEÇAM COM A
for l in range(4):#l para linhas
    for c in range(4):#c para colunas
        if pessoas[l][c][0] == "A":
            print(pessoas[l][c], end=" | ")
    print()


print("\n")
for l in range(4):#l para linhas
    for c in range(4):#c para colunas
        if pessoas[l][c][0] == "B":
            print(pessoas[l][c], end=" | ")
    print()


