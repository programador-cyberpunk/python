#onde eu faço a magia toda da matematica
def somak(k):
    return( k *(k + 1)) // 2

#vem a vez do usuario agora
k = int(input("Digite um numero ai topeira: "))
if k < 1:
    #sempre bom verificar
    print("Porra, um numero e gente por favor....")
else:
    resultado = somak(k)
    print(f"A soma de oos os numeros de 1 a {k} eh: {resultado}")
    #eu nao gosto de usar o latin strengh pq sempre a merda