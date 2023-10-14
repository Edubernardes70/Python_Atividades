pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]
]
for l in range(4):
    for c in range (4):
        if pessoas [l][c][1]> 30:
            print(pessoas[l][c], end=" ")
    print()