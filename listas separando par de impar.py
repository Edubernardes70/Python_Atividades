impar=[]
par=[]
numeros=[]
for c in range(0,7):
    numeros.append (int(input(f'Digite o {c+1}º número: ')))
for n in numeros:
    if n %2==0:
        par.append(n)
    else:
        impar.append(n)

print(f'Lista digitada: {numeros}')
print(f'Os números pares são {par}')
print(f'Os números impares são', impar)