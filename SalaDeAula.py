    class sala():
        #vamo construir primeiro
        def __init__(self, Turma):
            self.Turma = Turma

        def setAluno(self, aluno):
            self.aluno = aluno
        
        def setIdade(self, idade):
            self.idade = idade

        def setNota(self, nota):
            self.nota = nota
        
        def setPresenca(self, presenca):
            self.presenca = presenca

        def setEndereco(self, endereco):
            self.endereco = endereco
        
        def addAluno(self, aluno):
            self.aluno.append(aluno)#to improvisando

        def lista_aluno(self):
            if not self.aluno:
                return "Não há alunos para listar..."
            return "\n".join(str(aluno) for aluno in self.aluno)

        #chamando agora alguma função
        aluno1 = Aluno("Biff", 15, 7, True, "Rua 7, 127")
        aluno2 = Aluno("Maria", 16, 8, True, "Rua 2, 214") 
        aluno3 = Aluno("Jorge", 17, 1, True, "Rua 4, 422") 
        aluno4 = Aluno("Diocresildo", 15, 5, True, "Rua 3, 327") 
        aluno5 = Aluno("Glaudison", 15, 2, True, "Rua 1, 7") 
        aluno6 = Aluno("Sofia", 16, 6, True, "Rua 12, 418")

        sala_a.adicionar_aluno(aluno1)
        sala_a.adicionar_aluno(aluno2)
        sala_a.adicionar_aluno(aluno3)
        sala_a.adicionar_aluno(aluno4)
        sala_a.adicionar_aluno(aluno5)
        sala_a.adicionar_aluno(aluno6)

        print(sala_a.listar_alunos())