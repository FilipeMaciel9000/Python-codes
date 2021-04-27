def vogal(letra):
    vogais = "aeiou"
    if letra.lower() not in vogais:
        return False
    return True

letra = input("Digite uma letra: ")
print(vogal(letra))
