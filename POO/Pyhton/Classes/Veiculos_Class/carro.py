from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def descricao(self):
        return f"{super().descricao()} e é um carro do modelo {self.modelo}"