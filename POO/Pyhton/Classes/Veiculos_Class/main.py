from carro import Carro
from moto import Moto

def apresentar_veiculo(veiculo):
    print(veiculo.descricao())

carro = Carro("Chevrolet", "kleber")
moto = Moto("Volkswagem", "9000")

apresentar_veiculo(carro)
apresentar_veiculo(moto)