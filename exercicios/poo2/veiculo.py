# 1) Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
# 2) No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass
