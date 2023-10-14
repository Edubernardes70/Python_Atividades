from time import sleep

contatos = []  # Lista para armazenar vários contatos

def adicionar_contato(nome, telefone):
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)

while True:
    print("1. Adicionar contato")
    print("2. Alterar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair do contato\n")
    escolha = int(input("\nESCOLHA UMA OPÇÃO: "))

    if escolha == 1:
        nome = input("\nNome: ")
        telefone = input("Telefone: ")
        adicionar_contato(nome, telefone)
        print("Contato adicionado com sucesso.\n")

    if escolha == 2:
        nome_para_alterar = input('Digite o nome que deseja alterar: ')
        telefone_para_alterar = input('Digite o telefone que deseja alterar: ')

        for contato in contatos:
            if contato["nome"] == nome_para_alterar and contato["telefone"] == telefone_para_alterar:
                novo_nome = input('Digite o novo nome: ')
                novo_telefone = input('Digite o novo telefone: ')
                contato["nome"] = novo_nome
                contato["telefone"] = novo_telefone
                print('Contato alterado com sucesso.\n')
                break
        else:
            print('Contato não encontrado.\n')

    if escolha == 3:
        def deletar_contato():
            contato_para_deletar = input('Digite o nome do contato que deseja excluir: ')
            # telefone_para_deletar = input('Digite o telefone do contato que deseja excluir: ')
            for contato in contatos:
                if contato["nome"] == contato_para_deletar:
                    contatos.remove(contato)
                    print('Contato excluído com sucesso.\n')
                    break
            else:
                print('Contato não encontrado.\n')


        deletar_contato()

    if escolha == 4:
        print("\nLista de contatos:".upper())
        for contato in contatos:
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}\n")


    if escolha == 5:
        print('Saindo do sistema...')
        sleep(1)
        break
