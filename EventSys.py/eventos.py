# ==========================================
# CLASSE EVENTO
# ==========================================

class Evento:

    def __init__(self, nome, categoria, local, data,
                 idade_minima, valor, quantidade):

        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.data = data
        self.idade_minima = idade_minima
        self.valor = valor
        self.quantidade = quantidade

    def mostrar_informacoes(self):

        print(f'Evento: {self.nome}')
        print(f'Categoria: {self.categoria}')
        print(f'Local: {self.local}')
        print(f'Data: {self.data}')
        print(f'Idade mínima: {self.idade_minima} anos')
        print(f'Valor: R$ {self.valor:.2f}')
        print(f'Ingressos disponíveis: {self.quantidade}')

    def verificar_disponibilidade(self, quantidade):

        return self.quantidade >= quantidade