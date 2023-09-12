from time import sleep
print('=-=-'*20)
print('\t\t\tescola de testes computacionais'.upper())
print('=-=-'*20)
sleep(1)
print()
print('\t\tProfessor: Lance 5 notas (Total de 20 pts em cada)!')
print()
alunos = []  # lista para receber os dados inseridos abaixo
while True:
    print('\n\n')
    nome = input('Nome do Aluno: ')
    nota_1 = float(input('\nNota 1: '))
    while nota_1>=21:
        nota_1 = float(input('\nNota 1: '))
    nota_2 = float(input('\nNota 2: '))
    while nota_2>=21:
        nota_2 = float(input('\nNota 2: '))
    nota_3 = float(input('\nNota 3: '))
    while nota_3>=21:
        nota_3 = float(input('\nNota 3: '))
    nota_4 = float(input('\nNota 4: '))
    while nota_4>=21:
        nota_4 = float(input('\nNota 4: '))
    nota_5 = float(input('\nNota 5: '))
    while nota_5>=21:
        nota_5 = float(input('\nNota 5: '))
    faltas = float(input('\nFaltas na etapa: '))
    
    soma = nota_1+nota_2+nota_3+nota_4+nota_5  # aqui somamos as notas
    media = soma/5       # aqui estabelecemos a média
    dados = {'Nome': nome, 'Nota 1': nota_1, 'Nota 2': nota_2, 'Nota 3': nota_3,
             'Nota 4': nota_4, 'Nota 5': nota_5, 'Média': media}
    #dados receberá as informações digitadas no começo do programa(Notas (1,2) e média)
    alunos.append(dados)    # A lista alunos (começo) receberá a lista criada dentro de dados
    msg = input('\nDeseja continuar? [S/N]: ').strip().upper()
    if msg == 'N':
        break
sleep(2)
print('\n\n\t\t\t\tAguarde'.upper())
print('')
print('=-=-' * 20)
print('No.\t\tNome\t\tMédia\t\tNota Final\tFaltas')
print('____' * 20)
sleep(2)
for indice, aluno in enumerate(alunos, start=1):#aqui criaremos o indice para aparecer a ordem das notas
    nome_ = aluno['Nome']#aqui o nome receberá as informações do item 0 da lista dados que é {'Nome': nome}
    nota1 = aluno['Nota 1']
    nota2 = aluno['Nota 2']
    nota3 = aluno['Nota 3']
    nota4 = aluno['Nota 4']
    nota5 = aluno['Nota 5']
    mediafinal = aluno['Média']
    print(f'{indice}\t\t{nome_}\t\t{mediafinal}\t\t{soma}\t\t{faltas} ')#começo colocando o indice para aparecer primeiro, depois os dados que eu desejo
print('')
print('____' * 20)
sleep(1)
while True:
    print()
    sleep(1)
    msg2 = int(input('\nMostrar nota de qual aluno? (0 para sair): '))
    if msg2 == 0:
        break
    if 1 <= msg2 <= len(alunos):
        aluno_selecionado = alunos[msg2 - 1]  # Subtrai 1 para obter o índice correto na lista
        nome_ = aluno_selecionado['Nome']#pegando as informações da lista criada quando pegamos os dados   
        nota1 = aluno_selecionado['Nota 1']
        nota2 = aluno_selecionado['Nota 2']
        nota3 = aluno_selecionado['Nota 3']
        nota4 = aluno_selecionado['Nota 4']
        nota5 = aluno_selecionado['Nota 5']
        mediafinal = aluno_selecionado['Média']    
        print(f'Notas do (a) aluno (a): {nome_}\n\nNota 1: {nota1}\t\tNota 2: {nota2}\n\nNota 3: {nota3}\t\tNota 4: {nota4}\n\nNota 5: {nota5}\t\tMédia: {mediafinal}')
        print('')
        print('____' * 20)
sleep(1)
print()
print()
print('\t\t\t\tsaindo do sistema...'.upper())
sleep(1)
print('\n')
print('\t\t*****Agradecemos por usar o sistema EPB*****')
input()