login_correto="admin"
senha_correta="1234"

login=input("Insira o login ")
senha=input("Insira a senha ")

if login == login_correto and senha == senha_correta:
    print("Login concluido")
else:
    print("Login ou senha incorretos")