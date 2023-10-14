#RETORNO MULTIPLOS VALORES USANDO TUPLAS

def analisar_vendas(vendas_a, vendas_b):
    total_vendido = vendas_a+vendas_b
    mais_vendido = "A" if vendas_a > vendas_b else "B"
    return total_vendido, mais_vendido

total, top_produto = analisar_vendas(100,85)
print(f'TOTAL VENDIDO {total}')
print(f'PRODUTO MAIS VENDIDO {top_produto}')
#-----------------------------------------------------------------
print()
print()
#uso de tuplas em loops for

vendas = [(100,90), (35,115), (105,100)]
for vendas_a, vendas_b in vendas:
    print(f"Vendas A {vendas_a}, Vendas de B {vendas_b}")

#------------------------------------------------------------------
print("\n")
#TROCA DE VALORES ENTRE DUAS VARIAVEIS

vendas_a = 100
vendas_b = 85
vendas_a, vendas_b = vendas_b, vendas_a
print(f"Valor corrigido {vendas_a}")
print(f"Valor corrigido {vendas_b}")

#-----------------------------------------------------------------


