from .persona import pessoa

class Aluno(pessoa):
    def __init__(self,Nome):
        super().__init(Nome)

    def setTurma(self, turma):
         self.turma = turma

    def setEndereco(self, endereco):
         self.endereco = endereco