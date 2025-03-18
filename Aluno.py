class Aluno:

    def __init__(self, nome, idade, nota, presenca, endereco):

        self.nome = nome

        self.idade = idade

        self.nota = nota

        self.presenca = presenca

        self.endereco = endereco


    def __str__(self):

        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, Presença: {self.presenca}, Endereço: {self.endereco}"
