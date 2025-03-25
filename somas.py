def soma_maior_menor(lista):
    if not lista:
        return 0
    maior = max(lista)
    menor = min(lista)
    return maior + menor

numeros = [3,12,44,76,28,92]
resultado = soma_maior_menor(numeros)
print(f"A soma do maior e do menor da lista eh: {resultado}")