numero = 17
palpite = 0
i = 0
palpites = []
while palpite != numero and i < 20:
    palpite = int(input("Insira um número entre 1 e 20: "))
    i += 1
    palpites.append(palpite)
if palpite == numero:
    print("Parabéns! Você acertou!")
else:
    print("Acabaram as tentativas.")
print("Suas tentativas foram:", palpites)