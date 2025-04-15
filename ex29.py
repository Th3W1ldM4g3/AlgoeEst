numeros = []
for i in range(4):
    numeros.append(int(input("Insira um número: ")))
mult = int(input("Insira um multiplicador: "))
for i in range(4):
    numeros[i] = numeros[i] * mult
print(f"Os números multiplicados são {numeros}")