def  tabuada_personalizada(base, inicio, fim): # Função que multiplica a base por todos os números entre o início e o fim
    print(f"Tabuada do {base}, de {inicio} até {fim}")
    for i in range(inicio, fim + 1):
        print(f"{base} x {i} = {base * i}")   

tabuada_personalizada(base = int(input("Insira a base que será multiplicada: ")), inicio = int(input("Insira o múltiplo inicial da tabuada: ")), fim = int(input("Insira o múltiplo final da tabuada: ")))
