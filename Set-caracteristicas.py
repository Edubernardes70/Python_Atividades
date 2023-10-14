#EXEMPLO 1
lista=[1,2,3,4,4,5,5,5]
print(lista)
conjunto = set(lista)#vai apresentar a lista sem os elementos repetidos
print(conjunto)
print("\n")

#EXEMPLO 2
conjunto = {1,2,"Python", (4,5)}
print(conjunto)#não é previsivel a ordem de impressão

try:
    conjunto.add([6,7])
except TypeError as e:
    print(f"Erro: {e}")#lista mutavel em um conjunto dará erro
print("\n")

s_chaves = {1,2,3,3,4}
print(s_chaves)
print("\n")

s_funcao = set([1,2,3,4,4])
print(s_funcao)
print("\n")

#comparando os metodos
print(s_chaves==s_funcao)#dará true pois os dois metodos são iguais- dão o mesmo resultado

