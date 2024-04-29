from animal import Animal

class Gato(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


    def get_som(self):
        return "Miau VADIA"