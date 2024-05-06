from veiculo import Veiculo


# 3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    # 4- Implemente o Método Especial __str__ na Classe Filha: Adicione um método especial __str__ à classe Carro que estenda o método da classe pai (Veiculo).
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self.marca}, {self.modelo}, - Portas:{self.portas}"
