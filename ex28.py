par = []
impar = []
numero = 0
for i in range(4):
    numero = int(input("Insira um número: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f"os números pares são {par} e os ímpares são {impar}")