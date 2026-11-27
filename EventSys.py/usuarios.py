# ==========================================
# CLASSE USUARIO
# ==========================================

class Usuario:

    def __init__(self, nome, idade, cpf, senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):

        if len(nova_senha) >= 8:
            self.__senha = nova_senha

        else:
            raise ValueError(
                'A senha deve possuir no mínimo 8 caracteres!'
            )

    def mostrar_informacoes(self):

        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')


# ==========================================
# CLASSE CLIENTE
# ==========================================

class Cliente(Usuario):

    def __init__(self, nome, idade, cpf, senha):
        super().__init__(nome, idade, cpf, senha)
        self.compras = []

    def adicionar_compra(self, compra):
        self.compras.append(compra)

    def consultar_compras(self):

        if not self.compras:
            print('Nenhuma compra realizada.')
            return

        for compra in self.compras:
            print(compra)


# ==========================================
# CLASSE ADMINISTRADOR
# ==========================================

class Administrador(Usuario):

    def cadastrar_evento(self, eventos, evento):

        eventos.append(evento)

        print('Evento cadastrado com sucesso!')

    def consultar_faturamento(self, compras):

        faturamento = sum(
            compra.valor_total for compra in compras
        )

        print(f'Faturamento total: R$ {faturamento:.2f}')