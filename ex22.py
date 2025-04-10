palavras = []
maiores = 0
for i in range(6):
    palavras.append(input("Insira uma palavra: "))
    if len(palavras[i]) > 5:
        maiores += 1
print(f"Existem {maiores} palavras maiores que 5 caracteres.")