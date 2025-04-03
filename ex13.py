nome=input("Insira o nome do aluno ")
idade=int(input("Insira a idade do aluno "))
turma=input("Insira a turma do aluno ")
print(f"Aluno cadastradi com sucesso:{nome}, {idade} anos, turma {turma}")
if idade < 6:
    print("Matricula inválida")
else:
    print("Matrícula válida")