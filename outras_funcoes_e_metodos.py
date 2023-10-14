frutas = {"maça", "banana", "laranja", "uva", "manga"}
#LEN (LEITURA DE QUANTIDADES DE ELEMENTOS)
numero_frutas=len(frutas)
print(numero_frutas)

#IN
fruta_desejada = "maça"
if fruta_desejada in frutas:
    print(f'{fruta_desejada} está no conjunto de frutas')
else:
    print(f'{fruta_desejada} não está no conjunto de frutas')
