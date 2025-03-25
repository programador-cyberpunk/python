#definindo como o bang vai funcionar

def calcula_produto(a, b):
    produto = a * b
    if produto <= 1000:
        return produto
    else:
        return a + b
    
   #agora vc incrementa o bagulho
num1 = 10
num2 = 30

resultado = calcula_produto(num1,num2)
print(f'E o resulao eh: {resultado}')