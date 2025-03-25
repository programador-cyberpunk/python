# a parte mais treta
def primos(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True 
#passando a limpo
def imprimir(inicio,fim):
    print(f"Numeo primos enter o {inicio} e {fim} ")
    for x in range(inicio, fim + 1):
        if primos(x):
            print(x, end=" ")
    print()
    
#agora entra o usuario
inicio = int(input("Digita ai o inicio: "))
fim = int(input("Agora o fimn: ")) 

imprimir(inicio, fim)