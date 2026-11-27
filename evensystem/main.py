print('=' * 130)
print('EVENTSYS'.center(130))
print('=' * 130)

while True:
    try:
        print('\nMENU PRINCIPAL')
        print('-' * 130)
        print('1 - Cadastro de usuario')
        print('2 - Consultar eventos')
        print('3 - Comprar ingressos')
        print('4 - Consultar compras')
        print('0 - Sair')
        print('-' * 130)

        opcao = input('Digite a opção que deseja executar: ')

        if opcao == '1':
            print('\nCADASTRO DE USUARIO')
            print('-' * 130)

            nome = input('Digite seu nome completo: ').strip()
            if not nome:
                print('ERRO: O nome não pode ficar vazio!')
                continue

            idade = int(input('Digite sua idade (anos): '))

            if idade <= 0:
                print('ERRO: Informe uma idade válida!')
                continue

            cpf = input('Digite seu CPF: ').strip()
            if not cpf:
                print('ERRO: O CPF não pode ficar vazio!')
                continue

            print('\nCadastro realizado com sucesso!')
            print(f'Nome: {nome}')
            print(f'Idade: {idade} anos')
            print(f'CPF: {cpf}')

        elif opcao == '2':
            print('\nCONSULTAR EVENTOS')
            print('Funcionalidade em desenvolvimento!')

        elif opcao == '3':
            print('\nCOMPRAR INGRESSOS')

            idade = int(input('Digite sua idade (anos): '))

            if idade < 18:
                print('Compra não permitida! Idade mínima: 18 anos.')
            else:
                print('Idade permitida. Funcionalidade de compra em desenvolvimento!')

        elif opcao == '4':
            print('\nCONSULTAR COMPRAS')
            print('Funcionalidade em desenvolvimento!')

        elif opcao == '0':
            print('\nPrograma encerrado!')
            break

        else:
            print('\nOpção inválida! Tente novamente.')

    except ValueError:
        print('\nERRO: Digite um número inteiro válido!')
