idade=int(input("insira sua idade: "))
membro=input("Insira sim se for membro: ")
acompanhado=input("Insira sim se estiver acompanhado: ")

if idade < 18:
    print("Entrada negada.")
elif membro == "sim":
    print("Entrada permitida")
elif acompanhado == "sim":
    print("Pague meia entrada")
else:
    print("Pague um ingresso")