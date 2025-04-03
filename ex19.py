idade=int(input("insira a idade: "))
genero=input("insira o gênero: ")
atleta=input("Insira sim se for atleta e não se não: ")

if idade < 15:
    print("Oferecer artigos infantis")
elif idade <=21 and genero == "feminino":
    print("Oferecer maquiagem e moda")
elif idade <= 35 and genero == "feminino":
    print("Oferecer artigos esportivos e itens de casa")
elif idade <= 32 and atleta == "sim":
    print("Oferecer artigos esportivos")
elif idade < 21 and atleta == "não":
    print("Oferecer videogames")
elif idade <= 32 and atleta == "não":
    print("Oferecer livros, jardinagem e eletrodomésticos")