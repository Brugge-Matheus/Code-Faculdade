from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, name, disciplina):
        super().__init__(name)
        self.disciplina = disciplina


    def apresentar(self):
        return f"{super().apresentar()} e sou professor, leciono a disciplina de {self.disciplina}"