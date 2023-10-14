livro = {
    "titulo": "Milenio",
    "autor": "Tom Holland",
    "ano": 2006
}

def exibir_livro (dados):
    for chave, valor in dados.items():
        print(f'{chave.title()}: {valor}')

exibir_livro(livro)
print("\n")
def registrar_livro (titulo, autor, ano):
    return{"titulo": titulo,
    "autor": autor,
    "ano": ano}

novo_livro = registrar_livro("1984", "George Orwell", 1949)
exibir_livro(novo_livro)
