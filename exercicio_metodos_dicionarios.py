filme = {
    "titulo": "Inception",
    "diretor": "Cristopher Nolan",
    "ano": 2010,
    "genero": "Ficção Cientifica"
}
print("Chaves", list(filme.keys()))
print("Valores", list(filme.values()))
print("Items", list(filme.items()))
print("\n")
copia_filme = filme.copy()
copia_filme.clear()
print(copia_filme)
print("\n")
elenco = filme.setdefault("Elenco", ["Leonardo DiCaprio", "Ellen Page"])
print(filme)
print("\n")
atualizacoes = {
    "duracao": "148 minutos",
    "idioma": "Inglês"
}
filme.update(atualizacoes)
print(filme)

print("\n")
chaves = ["nome", "idade", "ocupacao"]
novo_filme= dict.fromkeys(chaves,"Desconhecido")
print(novo_filme)