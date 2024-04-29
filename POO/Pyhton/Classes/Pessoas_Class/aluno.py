from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, name, matricula):
        super().__init__(name)
        self.matricula = matricula

    def apresentar(self):
        return f"{super().apresentar()} e sou aluno, minha matricula é {self.matricula}"