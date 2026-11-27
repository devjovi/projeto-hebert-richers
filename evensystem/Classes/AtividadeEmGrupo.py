class Usuario:
    def __init__(self, nome, email, cpf, senha):
        self.nome=nome
        self.email=email
        self.__cpf=cpf
        self.__senha=senha

class Adiministrador(Usuario):
    def __init__(self):
        super().__init__(
            'Miguel',
            'miguel@email.com',
            '12345678999',
            'ADM12345')
        self.eventos = []

    def validar_administrador(self):
        print(' VALIDAÇÃO DO ADMINISTRADOR ')
        cpf = input('Digite seu CPF: ')
        senha = input('Digite sua senha: ')

        if cpf == self.cpf and senha == self.senha:
            print(f'\nAcesso autorizado. Bem-vindo, {self.nome}!\n')
            return True

        else:
            print('Acesso negado! Dados incorretos.')
            return False
        
    def criar_eventos(self):
        print('Criar Evento')
        nome = input('Nome do evento: ')
        data = input('Data: ')
        local = input('Local: ')

        evento = {
            'nome': nome,
            'data': data,
            'local': local
        }

        self.eventos.append(evento)

        print('Evento criado com sucesso!')

    
class Cliente(Usuario):
    def __init__(self, nome, email, cpf, senha):
        super().__init__(nome, email, cpf, senha)

        self.historico_compras = []

    def comprar_evento(self, evento):
        compra = {
            'evento': evento,
            'cliente': self.nome}

        self.historico_compras.append(compra)

        print(f'Compra do evento:{self.evento}, realizada com sucesso!')

    def mostrar_historico(self):
        print(' HISTÓRICO DE COMPRAS ')

        if len(self.historico_compras) == 0:
            print('Você ainda não realizou compras.')
            return

        for compra in self.historico_compras:
            print(f"Evento: {compra['evento']}")
            print(f"Cliente: {compra['cliente']}")