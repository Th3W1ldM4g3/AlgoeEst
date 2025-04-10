notas = []
media = 0
for i in range(5):
    notas.append(int(input("Insira uma nota: ")))
    media += notas[i]/5
print(f"A média das notas é {media}")