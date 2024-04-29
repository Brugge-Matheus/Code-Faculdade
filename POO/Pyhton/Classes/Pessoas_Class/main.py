from aluno import Aluno
from professores import Professor

def apresentar_pessoa(pessoa):
    print(pessoa.apresentar())

aluno = Aluno("Jailson Jonas", "094567")
professor = Professor("Horacio Trovoado", "Cinema")

apresentar_pessoa(aluno)
apresentar_pessoa(professor)