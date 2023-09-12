pessoas=list()
dados=list()
totmaior=totleve=0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    msg=(input('Deseja continuar: [S/N]: ')).strip().upper()
    if len(pessoas)==0:
        totmaior=totleve=dados[1]
    else:
        if dados[1]>totmaior:
            totmaior=dados[1]
        if dados[1]<totleve:
            totleve=dados[1] 
    pessoas.append(dados[:])
    dados.clear()
 
    if msg=='N':
        break
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'{totmaior} Kg é o mais pesado.')
for p in pessoas:
    if p[1]==totmaior:
        print(f'E o (s) mais pesado é (são) {p[0]} ')
    else:
        if p[1]==totleve:
            print(f'{p[0]} é (são) a(s) pessoa (s) mais leve') 



    

