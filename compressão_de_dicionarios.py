#Criar dicionario com quadrado de números
#{chave: valor for item in iteravel}
quadrado = {x: x**2 for x in range (1,6)}
print(quadrado)

#usando loop for tradiciona
quadrado = {}
for x in range(1,6):
    quadrado [x] = x**2
print(quadrado)

#converter chaves em valores e valores em chaves

original = {"a":1, "b":2, "c":3}
invertido = {valor:chave for chave, valor in original.items()}
print(invertido)#acima fazemos a inversão
print(original)
invertido = {}
for chave, valor in original.items():
    invertido [valor]= chave
    print(invertido)
print("\n\n")
#filtrando itens do dicionario:

precos = {
    "notebook":1000,
    "mouse": 25,
    "monitor": 200,
    "teclado": 55,
    "cabo hdmi": 15
    }

caros = {}
for produto, preco in precos.items():
    if preco > 56:
        caros[produto]= preco
print(caros)
barato = {}
for produto, preco in precos.items():
    if preco <=55:
        barato[produto]= preco
print(barato)
print("\n")
#usando compressão de lista
caros = {produto: preco for produto, preco in precos.items()if preco >56}
print(caros)
print("\n")
#dicionario com palavras e seus comprimentos

palavras = ["Python", "dicionario", "compressão"]
comprimentos = {palavra: len(palavra) for palavra in palavras}
print(comprimentos)

print("\n")

palavras = ["Python", "dicionario", "compressão"]
comprimentos = {}
for palavra in palavras:
    comprimentos[palavra] = len(palavra)
print(comprimentos)