nome=input("Insira o nome do produto ")
quantidade=int(input("Insira a quantidade de produtos "))
preco=float(input("Insira o preço unitário do produto "))

valor_total=quantidade*preco

if valor_total > 100:
    print(f"O valor total é {valor_total*0.9}")
else:
    print(f"O valor total é {valor_total}")