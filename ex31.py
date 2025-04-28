def tabuada(numero):# Cria a função tabuada, que imprime qual tabuada será feita e o resultado de toda a tabuada do número.
    print(f"Tabuada do {numero}")
    for i in range(1,11):
        print(f"{numero} x", i, "=", numero*i) #Mostra o número atual da tabuada
    
# numero = int(input("Insira um número: "))   
tabuada(numero = int(input("Insira um número: ")))
        