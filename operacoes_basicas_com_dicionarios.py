produto ={
    "id": 12345,
    "nome": "camisa polo",
    "cor": "azul",
    "preco": 49.90,
    "estoque": 100
}

#ADICIONANDO ITEM NO DICIONÁRIO
produto ["marca"]= "Polo Play"
produto ["desconto"]= 10

print('Adicionando itens', produto)

#ATUALIZANDO ITENS
produto ["preco"]= 69.90
produto ["cor"]= "amarela"
produto ["desconto"]= 15
print("Atualização de itens")
print(produto)

#REMOVENDO ITENS
del produto ["desconto"]
print(produto)
itens_removidos = produto.pop("id", "desconto")
print(itens_removidos)
item_removido = produto.popitem()# remove o ultimo item
print(item_removido)

#COPIANDO DICIONÁRIOS
produto_copia_1 = produto.copy()
produto_copia_2 = dict(produto)
print("\nCópias do produto")
print("Cópia 1", produto_copia_1)
print("Cópia 2", produto_copia_2)