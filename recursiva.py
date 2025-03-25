def recursiva(n):
    if n <=1:
        return n
    else:
        return n + recursiva(n - 1)
    
n = 7
resultado = recursiva(n)
print(f"A soma de numeros de 1 a {n} eh: {resultado}") 