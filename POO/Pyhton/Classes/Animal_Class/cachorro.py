from animal import Animal

class Cachorro(Animal):
    def __init__(self, name, race):
        super().__init__(name)
        self.race = race

    def get_som(self):
        return "AU AU VADIA"