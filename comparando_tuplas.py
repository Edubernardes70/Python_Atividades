#COMPARAÇÃO SIMPLES = TRUE PQ 3 É MAIOR QUE 2
t1 = (1,2)
t2 = (1,3)
print(t1 < t2)

#--------------------------
#IGNORANDO ELEMENTOS IGUAIS
t1 = (1,2,3)
t2 = (1,2,4)#true pois o 4 é maior que o 3 e os outros elementos são iguais
print(t1 < t2)

#--------------------------
#COMPARANDO TUPLAS DE DIFERENTES TAMANHOS
t1 = (1,2)
t2 = (1,2,3)#vai dar true pq a t1 é menor que t2
print(t1 < t2)

#--------------------------
#COMPARAÇÃO DE ELEMENTOS DE DIFERENTES TIPOS

t1 = (1,"Maça")
t2 = (2, "Banana")#irá imprimir true porque primeiro compara elementos int
print(t1 < t2)