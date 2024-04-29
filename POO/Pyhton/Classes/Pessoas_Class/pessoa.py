class Pessoa:

    def __init__(self, name):
        self.name = name

    
    def apresentar(self):
        return f"Olá, meu nome é {self.name}"