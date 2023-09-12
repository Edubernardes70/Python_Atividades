from time import sleep
print('=-'*48)
print('')
titulo='ESCOLA MUNICIPAL DE TESTE DIGITAL'
print(f'{titulo:^100}')
print('')
print('=-'*48)
sleep(1)
print('ESCOLHA AS OPÇÕES')
print('')
menu_opcao=('[1] LANÇAMENTO DE NOTA FINAL',
            '[2] LANÇAMENTO NOTA POR ATIVIDADE', 
            '[3] LANÇAMENTO DE ATIVIDADES', 
            '[4] SAIR')
for cont in range(0,len(menu_opcao)):
    print(menu_opcao[cont])
    print('')
n = int(input('Digite a escolha: '))
while True:
    if n>=5:
        print('ATENÇÃO!!! ESCOLHA UMA OPÇÃO VÁLIDA\n Digite a escolha:')
    elif n==1:
        print('')
        lanc_notas='*****LANÇAMENTO DE NOTAS DE ALUNOS*****'
        print(f'{lanc_notas:^100}')
        print('')
        sleep(1)
        while True:
            obs_1_nota_final='Lançar a nota final (0-100)'
            print(f'{obs_1_nota_final:^100}')
            print('')
            sleep(1)
            soma=materia1=nota=0
            print('=-'*48)
            print('')
            sleep(1)
            materia= input('\nDisciplina: ').strip().upper()
            nota=int(input('\nNota final: '))
            sleep(1)
            outra_nota=input('\n\nDeseja lançar outra nota [S/N]: ').strip().upper()
            while outra_nota not in "SN":
                outra_nota=input('\n\nDeseja lançar outra nota [S/N]: ').strip().upper()
            if outra_nota=='N':
                for cont in range (nota):
                    nota+=soma
            aluno=input('Digite o nome do aluno: ').strip().upper()
            sleep(1)
            turma= input('\nTurma do aluno: ').strip().upper()
            sleep(1)    
            print(soma)
            break
        break







    elif n==2:
        print('')
        lanc_atividades='***** LANÇAMENTO DE ATIVIDADES - PROFESSOR *****'
        print(f'{lanc_atividades:^100}')
        print('')
        print('')
        sleep(1)
        soma_atividades=valor_ativ=0
        prof=input(('Nome do professor: '))
        data_ativ=(input('Data da atividade: '))
        desc_ativ=input('Descreva a atividade: ')
        pts_ativ=input('Atividade pontuada: [S/N]: ').strip().upper()
        if pts_ativ=='S':
           valor_ativ=int(input('Valor: '))
        outra_ativ=input('Deseja lançar outra atividade [S/N]: ').strip().upper()
        if outra_ativ=='N':
            for c in range (valor_ativ):
                soma_atividades+=valor_ativ
            print(soma_atividades)
            sleep(1)
            break
        while pts_ativ not in 'SN':
           input('Atividade pontuada: [S/N]: ').strip().upper()
        if pts_ativ == 'N': break
        print('')
        sleep(1)
    elif n ==3:
        break



print('Fim sistema')
