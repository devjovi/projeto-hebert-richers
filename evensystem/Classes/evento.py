class eventos:
    def __init__(self, nome: str, categoria: str, preço_base: float, idade_minima: int = 18 ):
        self.nome = nome
        self.categoria = categoria
        self.preço = preço_base
        self.idade_minima = idade_minima
        self.caixa_total = 0
        self.participantes = []
        self.ingressos_vendidos = []

    @property
    def caixa_total(self) -> float:
        return round(self.__caixa_total, 2)

    def registar_venda(self, Ingresso: ingresso, nome_participante: str,  )
        