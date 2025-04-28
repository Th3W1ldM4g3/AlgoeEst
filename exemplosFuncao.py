# # tabuada do 7
# print("Tabuada do 7")
# for i in range(1,11):
#     print("7 x", i, "=", 7*i) #Mostra o número atual da tabuada
    
# # tabuada do 8
# print("Tabuada do 8")
# for i in range(1,11):
#     print("8 x", i, "=", 8*i) #Mostra o número atual da tabuada

# # tabuada do 9
# print("Tabuada do 9")
# for i in range(1,11):
#     print("9 x", i, "=", 9*i) #Mostra o número atual da tabuada

# Declaração de variáveis

# def tabuada(numero):
#     print(f"Tabuada do {numero}")
#     for i in range(1,11):
#         print(f"{numero} x", i, "=", numero*i) #Mostra o número atual da tabuada
        
# # tabuada(7)
# # tabuada(8)
# # tabuada(9)
# for i in range(1,101):
#     tabuada(i)

def  tabuada_personalizada(base, inicio, fim): # Função que multiplica a base por todos os números entre o início e o fim
    print(f"Tabuada do {base}, de {inicio} até {fim}")
    for i in range(inicio, fim + 1):
        print(f"{base} x {i} = {base * i}")   

tabuada_personalizada(7, 1, 10)
tabuada_personalizada(5, 5, 15)