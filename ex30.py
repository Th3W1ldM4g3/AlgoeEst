# nome = ["arara","circo"]
# print(nome[0][4])
# # for i in range(len(nome)):

nomes = []
nome = ""
tamanho = 0
for i in range(4):
    nomes.append(input("Insira um nome: "))
for nome in nomes:
    tamanho = len(nome)
    palin = True
    for i in range(len(nome)):
        if nome[i] != nome[i*-1-1]:
            palin = False
    if palin == True:
        print(f"{nome} é um palíndromo")
    