matriz=[[0,0,0], [0,0,0], [0,0,0]]#como eu sei o tamanho da matriz que desejo já criei a lista dentro da lista
for l in range (0,3): #l significa linha - 0 a 3 pq colocarei apenas 3 elementos
    for c in range(0,3):#l significa coluna - 0 a 3 pq colocarei apenas 3 elementos
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))#aqui iremos inserir os valores para as colunas e para as linhas
#matriz, no caso, receberá os valores que irão para L e C.
print('-='*20)#daqui para baixo iremos formatar a impressão
for l in range(0,3):#esse for é de alimentação
    for c in range (0,3):#esse é o for de formatação
        print(f'[{matriz[l][c]:^5}]', end='')
    print()#este print alinhado desta forma e colocado aqui faz a quebra da linha
    
