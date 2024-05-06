from carro import Carro
from moto import Moto


# 7- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
# 8- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método __str__.
def main():
    moto1 = Moto("Honda", "CB 500", "esportiva")
    moto2 = Moto("Kawasaki", "xr500", "casual")
    carro1 = Carro("Toyota", "Corolla", 5)

    print(moto1)
    print(moto2)
    print(carro1)


if __name__ == "__main__":
    main()
