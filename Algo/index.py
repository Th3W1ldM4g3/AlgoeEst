#Isso é um comentário

# print("Mensagem")

nome=input("Insira um nome ")
idade=int(input("Insira a idade "))
peso=float(input("Insira o seu peso "))

#Não é necessário declarar a variável anteriormente, mas deve-se declarar um valor
#Quando se utiliza um input, o tipo padrão é string, então deve-se declarar seu tipo caso contrário

# String - str - Caractere
# Inteiro - int
# Float - Real

print(f"{nome} {idade} anos {peso} kg")

#Se utiliza chaves para chamar variáveis dentro de uma string após um f (de formatação)
