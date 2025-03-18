from classes.persona import pessoa
from classes.aluno import Aluno

p1 = pessoa("Mauro")
p1.setIdade(1987)
print(p1)

p2 = pessoa("Juan")
p1.setIdade(2004)
print(p2)

al1 = Aluno("Roberto")
al1.setIdade("2004")
al1 = setTurma("2 B")


#print(p1.planeta)

#sei la se ta certo

end = Endereco()
end.setRua("Faria Lima")
end.setNumero("666")
end.setBairro("Bairro do Limoeiro")
end.setCidade("Guarulhos")
end.setEstado("Sao Paulo")
end.setPais("Brasil")
print(al1.__dict__)
print(al1.endereco)