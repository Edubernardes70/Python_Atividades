from time import sleep
print()
print('=-'*30)
print()
bco='BANCO EPB INVESTIMENTOS LTDA'
print(f'{bco:^60}')
print()
print('=-'*30)
print()
sleep(1)
cx_eletr='CAIXA ELETRONICO 24H'
cx_1=('**'*10)
cx_2=('--'*30)
agrd=('AGUARDE.....')
print(f'{cx_1}{cx_eletr}{cx_1}')
print()
sleep(1)
saldo_inicial=1000
deposito=0
saque=0
saldo_real=0
saldo_real=saldo_inicial
while True:
    
    menu=int(input("""\n\nSelecione uma opção:
               
    [1] Verificar saldo
    [2] Depositar 
    [3] Sacar
    [4] Terminar
    
    Digite a opção= """))
    if menu==1:
        #saldo_real+=deposito
        #saldo_real-=saque
        #saldo_real=saldo_inicial-saque
        
        sleep(1)
        print(f'\n\n\n{agrd:^60}\n\n\n')
        sleep(2)
        print(f'{cx_2}')
        seu_sld='Seu saldo é de =>=>=> '
        print(f'\n\n{seu_sld:^50} R${saldo_inicial:.2f}\n\n')
        print(f'{cx_2}')
        sleep(2)
    if menu==2:
        dpsto_sucss='Deposito realizado com sucesso!!!'
        dgt_dpsto=('Digite o valor a depositar: R$=>=>=>')
        sleep(1)
        print(f'\n\n\n{agrd:^60}\n\n\n')
        sleep(2)
        print(f'{cx_2}')
        deposito=int(input(f'{dgt_dpsto:^55}'))
        if deposito>0:
            saldo_inicial+=deposito
        else:
            print('VALOR DE DEPÓSITO INVÁLIDO')
        sleep(1)
        print(f'\n\n{dpsto_sucss:^60}')
        print(f'{cx_2}')
    elif menu==3:
        saque_sucess=(' Saque realizado com sucesso!')
        vlr_saque=('\n\nDigite o valor a sacar: R$=>=>=>')
        saque=int(input(f'{vlr_saque:^60}'))
        if saque>0:
            saldo_inicial-=saque
        sleep(1)
        print(f'\n\n\n{agrd:^60}\n\n\n')
        sleep(2)
        sleep(1)
        if saque<=saldo_inicial:
            saque_sucess=(' Saque realizado com sucesso!')
            print(f'{cx_2}')
            print(f'\n\n{saque_sucess:^60}')
            print(f'\n\n{cx_2}')
        elif saque>saldo_inicial:
            saque_sucess=(' Saque realizado com sucesso!')
            print(f'{cx_2}')
            sleep(1)
            print("""                           ATENÇÃO!!!
                VOCÊ ESTÁ USANDO SEU CHEQUE ESPECIAL""")
            sleep(2)
            print(f'\n\n{saque_sucess:^60}')
            print(f'\n\n{cx_2}')
            sleep(1)
                   
    if menu==4:
        sleep(2)
        print()
        print()
        saida='Saindo do sistema..'
        sleep(2)
        print()
        print(f'{saida:^60}')
        break
else:

    menu=int(input("""Selecione uma opção:
               
    [1] Verificar saldo
    [2] Depositar 
    [3] Sacar
    [4] Terminar
    
    Digite a opção= """))

print('=-'*30)
print()
bco='BANCO EPB INVESTIMENTOS LTDA'
print(f'{bco:^60}')
print()
print('=-'*30)
print()
msg_final='AGRADECEMOS POR USAR NOSSOS SERVIÇOS'
cx_1=('**'*5)
print(f'{cx_1}{msg_final}{cx_1}')
print()




