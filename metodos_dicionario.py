livro = {
    "titulo": "Pequeno Principe",
    "autor" : "Antoine de Saint - Exupéry",
    "ano": 1943,
    "editora": "Reynal e Hitchcock",
    "preco": 19.90
}

#------------------------------------------------
#KEYS, VALUES, ITEmS
print("keys(), values(), items ()")
print("Chaves do dicionario: ", list(livro.keys()))
print("Valores do dicionario: ", list(livro.values()))
print("Items do dicionario: ", list(livro.items()))

#CLEAR()
print()
copia_livro = livro.copy()
copia_livro.clear()
print(copia_livro)

#SETDEFAULT
isbn = livro.setdefault("ISBN", "987-3-25-74-1102")
print("ISBN", isbn)
print("Dicionario após setdefault:", livro)

#UPDATE
print()
atualizacoes = {
    "preco": 17.50,
    "formato": "Capa dura"
}
livro.update(atualizacoes)
print("Dicionario após Update",livro)

#FROM KEYS
print()
chaves = ["Titulo", "Autor", "Sinopse"]
novo_livro = dict.fromkeys(chaves, "Desconhecido")
print("Dicionario Fromkeys",novo_livro )