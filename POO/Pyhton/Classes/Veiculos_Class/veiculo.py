class Veiculo:
    def __init__(self, marca):
        self.marca = marca


    def descricao(self):
        return f"A marca do carro é {self.marca}"