livro = {
    #"chave" : "valor",
    "titulo": "1984",
    "autor": "Jorge Orwell",
    "ano" : 1949
}

print(livro["autor"])#imprime o valor associado ao valor da chave

#----------------------------

frutas = [ "maça", "banana", "laranja"]
print(frutas [2])

#-----------------------------
coordenadas = (4.5, 6.7, 8.2)
print(coordenadas [1])

#-----------------------------
contatos = {
    "Alice": "Tel.:555-1234",
    "Bruno": "Tel.:555-5678",
    "Tiago": "Tel.:338-6652",
    "Miguel": "Tel.:158-1185"
    }
print(contatos["Miguel"])
print()
#-----------------------------
#SINTAXE BÁSICA

carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "Ano": 1984
    }
print(carro)
print(carro["modelo"])
print()
#-----------------------

#DICIONÁRIO VAZIO
pessoas = {}
print(pessoas)
print()
#-----------------------
#DICIONÁRIO COM MULTIPLOS ITENS

#Dicionaário pode conter vários pares e serem separados por virgula
pessoas = {
    "nome": "Maria", #Chave = nome - Valor= Maria
    "idade": 30,
    "profissão": "Professora",
    "nacionalidade": "brasileira"
}
print(pessoas)
print(f'Seu nome é {pessoas["nome"]} e sua profissão é {pessoas["profissão"]}')
print()
print()
#--------------------------
#DICIONÁRIOS ANINHADOS
#Um dicionário pode conter outros dicionario, listas ou tuplas
familia = {#dicionário familia e subdicionários (pai, mae e filho)

    "pai": {"nome": "Roberto",
            "idade": 50},
    "mae": {"nome": "Sueli",
            "idade": 45},
    "filho": {"nome": "Tiago",
              "idade": 22}
}
print(familia["pai"]["nome"])
print(f'Sua mãe se chama {familia["mae"]["nome"]}')
print(f'O filho {familia["filho"]["nome"]} tem {familia["filho"]["idade"]} anos de idade')