#tenho que saber quantas vezes uma substring aparece dentro dessa merda
def substring(string):
    contagem = {}
    for tamanho in range(len(string) + 1):
        for i in range(len(string) - tamanho + 1):
            substring = string[i:i + tamanho]
            if substring in contagem:
                contagem[substring] +=1
            else:
                contagem[substring] = 1
    return contagem

#agora entra o usuario na historia
string_usuario = input("Digita sua string ai: ")
resultado = contar_substring(string_usuario)

print("contagem e substrings: ")
for substringm, contagem in resultado.items():
    print(f"{substring}: {contagem} vezes")