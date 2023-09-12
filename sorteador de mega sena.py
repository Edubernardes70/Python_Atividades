import random
jogo=[]
print('---'*20)
print('\t\t\tJOGO NA MEGA SENA')
print('---'*20)
print('')
qtd_jogo=int(input('Quantos jogos deseja fazer: '))

print('')
for q in range (qtd_jogo):
    jogo=random.sample(range(1,61),6)
    print (f'Jogo {q+1}=>',sorted(jogo))
print('')
print('-=-=-=-=-=-=-=-=-=-=-=-= BOA SORTE -=-=-=-=-=-=-=-=-=-=-=-=-')
