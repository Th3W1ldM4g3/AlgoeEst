salario_base=float(input("Insira o salário base "))
qnt_horas_extras=int(input("Insira a quantidade de horas extras "))
valor_horas_extras=float(input("Insira o valor pago por hora extra"))

salario_total= salario_base + qnt_horas_extras * valor_horas_extras

print(f"O salário total é {salario_total}")