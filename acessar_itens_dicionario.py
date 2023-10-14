smartphone = {
    "marca": "Apple",
    "modelo": "Iphone 12",
    "cor": "Azul",
    "capacidade": "256 gb",
    "sistema": "IOS 15"
}
print("Método direto")
print(smartphone)
print(smartphone["marca"])
print(smartphone["modelo"])
print(smartphone["capacidade"])
print()
#------------------------------
#METODO GET
print()
print("METODO GET ()")
print("Modelo: ", smartphone.get("modelo"))
#caso eu tente acessar algum item que não exista ele retorna none
print("Camera:", smartphone.get("camera"))

#-------------------------------
#VERIFICANDO A EXISTENCIA DE UMA CHAVE

print()
print("VERIFICANDO A EXISTENCIA DE ALGUMA CHAVE")
if "sistema" in smartphone:
    print(f"O sitema no smartphone é ",smartphone["sistema"])
else:
    print("Não existe este item no smartphone")

if "camera" in smartphone:
    print(f" A camera é de {smartphone}")
else:
    print("Não existe especificação de camera")