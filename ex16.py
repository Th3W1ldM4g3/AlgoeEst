nota1 = float(input("insira uma nota "))
nota2 = float(input("insira uma nota "))
nota3 = float(input("insira uma nota "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")