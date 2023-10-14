artista ={
    "nome": "Ludwig Van Beethoven",
    "nascimento": 1770,
    "falecimento": 1827,
    "nacionalidade": "Alemã",
    "estilo": "Clássico"
}
print(f'O artista é {artista["nome"]}')
if "profissao" in artista:
    print(f"A profissão de {artista['nome']} é {artista}")
else:
    print(f'Não existe este item na lista do artista')
print(f"{artista['nome']} tem nacionalidade", artista.get("nacionalidade"))
print("Profissão", artista.get("profissão"))
if "estilo" in artista:
    print(f'O estilo musical de {artista["nome"]} é {artista["estilo"]}')
else:
    print('Informação não disponível')
if "instrumento principal" in artista:
    print(f"O instrumento principal é {artista}")
else:
    print("Instrumento principal não especificado")


