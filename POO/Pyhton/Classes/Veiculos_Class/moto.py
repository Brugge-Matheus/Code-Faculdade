from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, cilindrada):
        super().__init__(marca)
        self.cilindrada = cilindrada

    def descricao(self):
        return f"{super().descricao()} e é uma moto de {self.cilindrada} cilindradas"