vendas = {
    "Janeiro": 120,
    "Fevereiro": 150,
    "Março": 80,
    "Abril": 190,
    "Maio": 210
}

for meses in vendas:
    print(meses)
print()

total=0
for valor in vendas.values():
    #print(valor)
    total+=valor
soma= total
print(f'A venda em 5 meses dá o valor de {soma}')
print(f'O mês de {vendas["Março"]} foi o que vendeu menos')

print()
for meses, valor in vendas.items():
    print(f'Em {meses}, {valor} livros foram vendidos')
