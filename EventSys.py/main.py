# ==========================================
# IMPORTAÇÕES
# ==========================================

from usuarios import Cliente, Administrador
from eventos import Evento
from vendas import Compra, ler_inteiro, ler_valor


# ==========================================
# FUNÇÃO PARA NORMALIZAR CPF
# ==========================================

def normalizar_cpf(cpf):
    return ''.join(
        caractere for caractere in cpf
        if caractere.isdigit()
    )


# ==========================================
# FUNÇÃO PARA VALIDAR CPF
# ==========================================

def validar_cpf(cpf):

    cpf = cpf.strip()

    if not cpf.replace('.', '').replace('-', '').isdigit():
        return False

    cpf = normalizar_cpf(cpf)

    return len(cpf) == 11


# ==========================================
# FUNÇÃO DE AUTENTICAÇÃO
# ==========================================

def autenticar_administrador(administrador):

    print('\n' + '=' * 50)
    print('ACESSO DO ADMINISTRADOR'.center(50))
    print('=' * 50)

    cpf = input('Digite o CPF do administrador: ').strip()
    senha = input('Digite a senha do administrador: ')

    if not validar_cpf(cpf):
        print('CPF inválido!')
        return False

    cpf = normalizar_cpf(cpf)

    if (
        cpf == normalizar_cpf(administrador.cpf)
        and senha == administrador.senha
    ):
        print('\nAcesso autorizado!')
        return True

    print('\nAcesso negado!')
    return False


# ==========================================
# LISTAS PRINCIPAIS
# ==========================================

usuarios = []
eventos = []
compras = []


# ==========================================
# ADMINISTRADOR INICIAL
# ==========================================

administrador = Administrador(
    'Administrador',
    18,
    '00000000000',
    'admin1234'
)


# ==========================================
# MENU PRINCIPAL
# ==========================================

print('=' * 130)
print('EVENTSYS'.center(130))
print('=' * 130)

while True:

    print('\n' + '=' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('=' * 50)

    print('1 - Cadastro de usuário')
    print('2 - Consultar eventos')
    print('3 - Comprar ingressos')
    print('4 - Consultar compras')
    print('5 - Cadastrar evento (Administrador)')
    print('6 - Consultar faturamento (Administrador)')
    print('0 - Sair')

    print('=' * 50)

    opcao = input('Digite a opção desejada: ').strip()


    # ======================================
    # CADASTRO DE USUÁRIO
    # ======================================

    if opcao == '1':

        print('\nCADASTRO DE USUÁRIO')

        nome = input('Digite seu nome completo: ').strip()

        if not nome:
            print('Nome inválido!')
            continue

        idade = ler_inteiro('Digite sua idade (anos): ')

        if idade <= 0:
            print('Idade inválida!')
            continue

        cpf = input('Digite seu CPF (11 números): ').strip()

        if not validar_cpf(cpf):
            print('CPF inválido! Informe exatamente 11 números.')
            continue

        cpf = normalizar_cpf(cpf)

        if any(
            normalizar_cpf(usuario.cpf) == cpf
            for usuario in usuarios
        ):
            print('Este CPF já está cadastrado!')
            continue

        senha = input('Crie uma senha (mínimo 8 caracteres): ')

        if len(senha) < 8:
            print('A senha precisa ter pelo menos 8 caracteres!')
            continue

        cliente = Cliente(nome, idade, cpf, senha)
        usuarios.append(cliente)

        print('Usuário cadastrado com sucesso!')


    # ======================================
    # CONSULTAR EVENTOS
    # ======================================

    elif opcao == '2':

        print('\nEVENTOS DISPONÍVEIS')

        if not eventos:
            print('Nenhum evento cadastrado.')

        else:

            for indice, evento in enumerate(eventos, start=1):

                print(f'\nEvento {indice}')
                evento.mostrar_informacoes()


    # ======================================
    # COMPRAR INGRESSOS
    # ======================================

    elif opcao == '3':

        print('\nCOMPRA DE INGRESSOS')

        cpf = input('Digite seu CPF: ').strip()

        if not validar_cpf(cpf):
            print('CPF inválido!')
            continue

        cpf = normalizar_cpf(cpf)

        cliente = None

        for usuario in usuarios:

            if normalizar_cpf(usuario.cpf) == cpf:
                cliente = usuario
                break

        if cliente is None:
            print('Usuário não encontrado!')
            continue

        if not eventos:
            print('Não existem eventos disponíveis!')
            continue

        print('\nEVENTOS DISPONÍVEIS')

        for indice, evento in enumerate(eventos, start=1):

            print(
                f'{indice} - {evento.nome} | '
                f'R$ {evento.valor:.2f} | '
                f'Ingressos: {evento.quantidade}'
            )

        escolha = ler_inteiro('Escolha o número do evento: ')

        if escolha < 1 or escolha > len(eventos):
            print('Evento inválido!')
            continue

        evento = eventos[escolha - 1]

        print('\nTIPO DE INGRESSO')
        print('1 - Padrão')
        print('2 - VIP (+20%)')

        tipo = input('Escolha o tipo de ingresso: ').strip()

        quantidade = ler_inteiro('Quantidade de ingressos: ')

        compra = Compra(cliente, evento, tipo, quantidade)

        if compra.finalizar_compra():
            compras.append(compra)


    # ======================================
    # CONSULTAR COMPRAS
    # ======================================

    elif opcao == '4':

        cpf = input('Digite seu CPF: ').strip()

        if not validar_cpf(cpf):
            print('CPF inválido!')
            continue

        cpf = normalizar_cpf(cpf)

        cliente = None

        for usuario in usuarios:

            if normalizar_cpf(usuario.cpf) == cpf:
                cliente = usuario
                break

        if cliente is None:
            print('Usuário não encontrado!')

        else:
            cliente.consultar_compras()


    # ======================================
    # CADASTRAR EVENTO
    # ======================================

    elif opcao == '5':

        if not autenticar_administrador(administrador):
            continue

        print('\nCADASTRAR EVENTO')

        nome = input('Nome do evento: ').strip()
        categoria = input('Categoria: ').strip()
        local = input('Local: ').strip()
        data = input('Data do evento: ').strip()

        if not nome or not categoria or not local or not data:
            print('Preencha todas as informações!')
            continue

        idade_minima = ler_inteiro(
            'Idade mínima do evento (anos): '
        )

        if idade_minima <= 0:
            print('Idade mínima inválida!')
            continue

        idade_minima = max(18, idade_minima)

        valor = ler_valor('Valor do ingresso (R$): ')

        quantidade = ler_inteiro(
            'Quantidade de ingressos: '
        )

        if valor <= 0 or quantidade <= 0:
            print('Valor e quantidade devem ser maiores que zero!')
            continue

        evento = Evento(
            nome,
            categoria,
            local,
            data,
            idade_minima,
            valor,
            quantidade
        )

        administrador.cadastrar_evento(eventos, evento)


    # ======================================
    # CONSULTAR FATURAMENTO
    # ======================================

    elif opcao == '6':

        if not autenticar_administrador(administrador):
            continue

        print('\nFATURAMENTO DO EVENTSYS')

        administrador.consultar_faturamento(compras)


    # ======================================
    # ENCERRAR PROGRAMA
    # ======================================

    elif opcao == '0':

        print('\nPrograma encerrado!')
        break

    else:

        print('Opção inválida! Tente novamente.')