class pessoa():
    #construtor da classe
    #planeta = "Terra"

    def __init__(self, Nome):
        self.nome = Nome 

    #converte as parada pra string
    def __str__(self):
        return "Mi nombre es " + self.nome + ", e tengo " + str(self.idade)

            #nome e variavel de instancia enquanto
            #planeta e variavel d eclasse

    #outro metodo,pra calcular idade agora

    def setIdade(self,ano):
        self.idade = 2025 -ano

    def setEndereco(self, endereco):
        self.endereco = endereco