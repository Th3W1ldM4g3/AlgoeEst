numeros=[]
total = 0

for i in range(10):
    numeros.append(int(input("Insira um número: ")))
for i in range(10):
    print(numeros[i])
for i in range(10):
    total += numeros[i]
print(total)