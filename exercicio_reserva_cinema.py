cadeiras = [
    ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
    ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"]
]
while True:
    print("\n")
    print("1. Ver disposição do assento\n2.Reservar assento\n3.Sair")
    selecao = int(input("Selecione uma opção: "))
    if selecao==1:
        for l in range(5):
            for c in range(10):
                print(cadeiras[l][c], end=" ")
            print()

    if selecao==2:
        fileira = int(input("Digite o nº da fileira: "))
        assento = int(input("Digite o nº do assento: "))
        if cadeiras[fileira][assento]=="D":
            cadeiras[fileira][assento]="R"
            print("Assento Rerservado")



    if selecao ==3:
        break

