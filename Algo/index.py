# #Isso é um comentário

# print("Mensagem")

#________________________________________________________________________________________________________________________

# nome=input("Insira um nome ")
# idade=int(input("Insira a idade "))
# peso=float(input("Insira o seu peso "))

# #Não é necessário declarar a variável anteriormente, mas deve-se declarar um valor
# #Quando se utiliza um input, o tipo padrão é string, então deve-se declarar seu tipo caso contrário

# # String - str - Caractere
# # Inteiro - int
# # Float - Real

# print(f"{nome} {idade} anos {peso} kg")

# #Se utiliza chaves para chamar variáveis dentro de uma string após um f (de formatação)

#________________________________________________________________________________________________________________________

# pedaco_pizza = 5
# cliente = "John"
# print(type(pedaco_pizza))
# print(type(cliente))

# # Type - retorna o tipo da variável

#________________________________________________________________________________________________________________________

# pedaco_pizza = input("Informe quantos pedaços comeu ")
# print(type(pedaco_pizza))

# # Lê uma string

# pedaco_pizza = int(input("Informe quantos pedaços comeu "))
# print(type(pedaco_pizza))

# # Lê um inteiro

#________________________________________________________________________________________________________________________

# a = 4
# A = "Sally"

# print(a)
# print(A)

# # Lê duas variáveis diferentes, já que possuem capitalização diferente, ou seja, o python é case sensitive.

# a = 4
# a = "Sally"

# print(a)
# print(A)

#________________________________________________________________________________________________________________________

# # Lê apenas uma variável e não lê a variável com capitalização diferente

# fruta1, fruta2, fruta3 = "laranja", "Banana", "Maçã"
# print(fruta1, fruta2, fruta3)

# # É possível atribuir valores a várias variáveis ao mesmo tempo, desde que o número de variáveis seja igual ao número de valores

#________________________________________________________________________________________________________________________

# primeiro_numero = 5
# segundo_numero = 10
# print(primeiro_numero + segundo_numero)

#________________________________________________________________________________________________________________________

# nome=input("Qual é o vingador mais forte? ")
# print(f"Olá, {nome}")
# if nome == "hulk":
#     print("Bem vindo, vingador mais forte!")
# else:
#     print("Acesso negado.")
    
# # Utiliza = para atribuição e == para comparação

#________________________________________________________________________________________________________________________

x = 5

if x > 2 and x < 10:
    print("O valor está entre 2 e 10.")
else:
    print("O valor não está entre 2 e 10")
    
# And - Retorna verdadeiro apenas quando duas outras condições forem verdadeira. Equivalente ao "e".

if x < 2 or x > 4:
    print("O número é menor que 2 ou maior que 4.")
    
# Or - Retorna verdadeiro caso uma de duas condições seja verdadeira. Equivalente ao "ou"

if not x > 10:
    print("O x não é maior que 10")
    
# Not - Retorna o oposto de uma condição.

y = 8

if x > 2 and (y > 10 or not x == 5):
    print("Condição complexa atendida.")
else:
    print("Condição não atendida.")

# O python avalia primeiro o Not, depois o And e depois o Or.

#________________________________________________________________________________________________________________________

