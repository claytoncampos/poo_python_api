from modelos.cardapio.item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    """
    Este código define uma classe chamada Sobremesa que herda da classe ItemCardapio. A classe Sobremesa possui os seguintes atributos:
    nome: herdado de ItemCardapio.
    preco: herdado de ItemCardapio.
    descricao: específico da classe Sobremesa.
    tipo: específico da classe Sobremesa.
    tamanho: específico da classe Sobremesa.
    O método __str__ é sobrescrito para retornar o nome da sobremesa. Além disso, a classe implementa o método aplicar_desconto, que reduz o preço da sobremesa em 15%.
    """

    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.15
