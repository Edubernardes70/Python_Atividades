usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com"
     }

def exibir_perfil(perfil): #aceita a criação do dicionario perfil
    for chave, valor in perfil.items():
        print(f'{chave}: {valor}')

exibir_perfil(usuario)#quando for imprimir ele vai pegar os dados do dicionario usuario e passar pela função exibir

print("\n")

#retornando dicionarios de funçoes
def criar_perfil (nome, idade, email):
    return{
    "nome": nome,
    "idade": idade,
    "email": email
     }

novo_usuario = criar_perfil ("Ana", 30, "ana@email.com")

exibir_perfil(novo_usuario)
print("\n")
def criar_perfil2 (nome, idade, email):
    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }
novo_usuario2 = criar_perfil2("Eduardo", 30, "eduardo@email.com")

exibir_perfil(novo_usuario2)