animal = {
    "tipo": "gato",
    "cor": "branco",
    "idade": 3

}
print(animal)

estudante = {}
estudante ["nome"]= "Carlos"
estudante ["Curso"] = "Matemática"
estudante ["Semestre"] = "2"

print(estudante)

livro = {
    "livro": "A arte da guerra",
    "autor": "Sun Tzu",
    "publicado": -500
    }
print (livro)

universidade = {
    "polo": {"nome": "Universidade do Estado de Minas - UEMG"},
    "local": {"localidade": "Poços de Caldas"},
    "bairro": {"bairro": "Contry Club"}
                    }
print(f'Estamos abrindo a {universidade["polo"]["nome"]}')
print(f'Na cidade de {universidade["local"]["localidade"]}')
print(f'No bairro {universidade["bairro"]["bairro"]}')