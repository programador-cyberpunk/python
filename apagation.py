#tem que apagar os bagulho e devolver uma nova string
def remove_letra(string, n):
    if n > len(string):
        return ""
    return string[n:]

#na pratica

string_terra1 = "Thin Lizzy"
n = 9
string_terra2 = remove_letra(string_terra1, n)
print(f" A nova string eh: {string_terra2}")