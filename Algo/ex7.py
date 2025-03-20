num1 = int(input("Insira um número "))
num2 = int(input("Insira um número "))
operacao = input("Insira a operação ")

if operacao == "soma":
    print(num1 + num2)
else:
    if operacao == "subtração":
        print(num1 - num2)
    else:
        if operacao == "multiplicação":
            print(num1 * num2)
        else:
            if operacao == "divisão":
                print(num1 / num2)
            else:
                print("Erro")

