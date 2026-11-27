# ==========================================
# FUNÇÕES AUXILIARES
# ==========================================

def ler_inteiro(mensagem):

    while True:
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print('Informe um número positivo!')
                continue

            return valor

        except ValueError:
            print('Digite um número inteiro válido!')


def ler_valor(mensagem):

    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))

            if valor < 0:
                print('Informe um valor positivo!')
                continue

            return valor

        except ValueError:
            print('Digite um valor válido!')


def calcular_desconto(valor):

    if valor > 200:
        desconto = valor * 0.10

    else:
        desconto = 0

    return desconto, valor - desconto


# ==========================================
# CLASSE INGRESSO
# ==========================================

class Ingresso:

    def __init__(self, evento):
        self.evento = evento

    def calcular_valor_final(self):

        return self.evento.valor


# ==========================================
# CLASSE INGRESSO PADRAO
# ==========================================

class IngressoPadrao(Ingresso):

    def calcular_valor_final(self):

        return super().calcular_valor_final()


# ==========================================
# CLASSE INGRESSO VIP
# ==========================================

class IngressoVIP(Ingresso):

    def calcular_valor_final(self):

        valor = super().calcular_valor_final()

        return valor * 1.20

    def mostrar_beneficios(self):

        print('\nBenefícios do ingresso VIP:')
        print('- Acesso à área VIP')
        print('- Atendimento exclusivo')


# ==========================================
# CLASSE COMPRA
# ==========================================

class Compra:

    def __init__(self, cliente, evento, tipo_ingresso, quantidade):

        self.cliente = cliente
        self.evento = evento
        self.tipo_ingresso = tipo_ingresso
        self.quantidade = quantidade
        self.valor_total = 0

    def finalizar_compra(self):

        idade_necessaria = max(
            18, self.evento.idade_minima
        )

        # Verificar idade
        if self.cliente.idade < idade_necessaria:

            print(
                f'Compra não permitida! '
                f'Idade mínima: {idade_necessaria} anos.'
            )

            return False

        # Verificar quantidade
        if self.quantidade <= 0:

            print('Quantidade inválida!')

            return False

        # Verificar disponibilidade
        if not self.evento.verificar_disponibilidade(
            self.quantidade
        ):

            print('Quantidade de ingressos indisponível!')

            return False

        # Identificar tipo de ingresso
        if self.tipo_ingresso == '1':

            ingresso = IngressoPadrao(self.evento)

        elif self.tipo_ingresso == '2':

            ingresso = IngressoVIP(self.evento)
            ingresso.mostrar_beneficios()

        else:

            print('Tipo de ingresso inválido!')

            return False

        # Calcular valores
        subtotal = (
            ingresso.calcular_valor_final() * self.quantidade
        )

        desconto, self.valor_total = calcular_desconto(subtotal)

        # Atualizar estoque
        self.evento.quantidade -= self.quantidade

        # Registrar compra
        self.cliente.adicionar_compra(self)

        print('\nCompra realizada com sucesso!')
        print(f'Subtotal: R$ {subtotal:.2f}')
        print(f'Desconto: R$ {desconto:.2f}')
        print(f'Total: R$ {self.valor_total:.2f}')

        return True

    def __str__(self):

        return (
            f'Cliente: {self.cliente.nome} | '
            f'Evento: {self.evento.nome} | '
            f'Quantidade: {self.quantidade} | '
            f'Total: R$ {self.valor_total:.2f}'
        )