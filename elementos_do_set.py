#CONJUNTO INICIAL
#removendo elementos

s = {1,2,3,4,}
print(s)
print("\n")

#add item

s.add(5)
s.add(3)
s.add(6)
print(s)
print("\n")

#remove item

s.remove(5)
print(s)

try:
    s.remove(9)#tentando deletar um número que não existe
except KeyError as e:
    print(f"Erro: {e}")


print("\n")

#usando o discard
s.discard(4)
#discard remove um elemento solicitado, se ele não existir
#não irá apontar o erro, se existir ele apagará
s.discard(15)
print(s)
print("\n")

#usando o pop

elemento_removido =s.pop()#aqui deleta fora de ordem (desordenado)
print(f'Elemento removido: {elemento_removido}')

print("\n")

#usando clear - remove tudo

s.clear()
print(s)