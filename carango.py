class Caranga:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def informacoes(self):
        print(f"Velociade maxima: {self.max_speed} mk/h")
        print(f"Kilometragem: {self.mileage} km....")
        
carro1 = Caranga(180,150)
carro1.exibir.informacoes()

class Buzum(Caranga):
    def __init__(self, max_speed, mileage,capacidade,tipo):
        super().__init__(max_speed, mileage)
        self.capacidade = capacidade
        self.tipo = tipo
    
    def informacoes(self):
        super().informacoes()
        print(f"Capacidae: {self.capacidade}")
        print(f"Tipo: {self.tipo}")
        
buzao1 = Buzum(100,150,47,"viagem")
buzao1.exibir.informacoes()

class Carrao(Caranga):
    def __init__(self, max_speed, mileage, modelo):
        super().__init__(max_speed, mileage)
        self.modelo = modelo
    
    def informacoes(self):
        super().informacoes()
        print(f"Modelo: {self.modelo}")
        
  veiculos = [
      Buzum(100,150,49,"viagem"),
      Carrao(180,200,"Fusca"),
      Buzum(300,250,49,"urbano"),
      Carrao(180,280,"Maverick"),
  ] 
  
  for veiculo in veiculos:
      print(f"Nome da classe: {veiculo.__class_._name__}")
      veiculo.exibir_informacoes()
      print()
      
       @classmethod
    def quantidade_de_carros(cls):
        #Método de classe que retorna a quantidade de carros criados
        return cls.contador_carros

    @staticmethod
    def informacoes_gerais():
        #Método estático que fornece informações gerais sobre carros
        return "Os carros são veículos motorizados com quatro rodas, usados principalmente para transporte de pessoas."
