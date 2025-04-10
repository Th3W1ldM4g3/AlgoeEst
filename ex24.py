numeros = []
menor = 0
maior = 0

for i in range(5):
    numeros.append(int(input("Insira um número: ")))
    if menor > numeros[i] or menor == 0:
        menor = numeros[i]
    if maior < numeros[i]:
        maior = numeros[i]
print(f"O maior número é o {maior} e o menor é o {menor}")