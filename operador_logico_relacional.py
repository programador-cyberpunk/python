#basication

a = 4
b = 6
c = 2.3
soma = a + b
sub = a - b
multi = a * b
div = b/a
exp = a ** b

#poe na tela porra
print(f'a soma: {a} + {b} = {soma}')
print(f'a subtraçao: {a} - {b} = {sub}')
print(f'a divisao: {a} * {b} = {multi}')
print(f'a multiplicaçao: {b} / {a} = {div}')
print(f'a exponenciaçao: {a} ** {b} = {exp}')

#RELACIONAIS
A = 2
B = 5
C = 10
print(f'A eh igual a 2 :{A == 2}')
print(f'Aeh diferente de B :{A != B}')
print(f'B eh menor que C :{B < C}')
print(f'B eh maior que C :{B > C}')
print(f'A eh menor ou igual ao dobro de C :{A <= 2 * C}')

#LOGICOS
a1 = 2
b2 = 5
c3 = 3
print(a1 == 2 and b2 == 5)
print(a1 != b2 or b2 < c3)
print(not b2 > c3 or b2 < c3)
print(b2 < c3 and a1 >= c3)