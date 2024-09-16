usuario = input("usuario: ")

while True: 
    senha = input("Senha: ")
    if senha == usuario:
        print("Senha deve ser diferente do usuario")
    else:
        print("Conta criada")  
        break
    
    
while True:
    usuario2 = input("Usuario: ")
    if usuario2 == usuario:
        print("Este usuário já existe")
        break
        


while True:
    senha2 = input("Senha: ")
    if senha2 == senha:
        print("Está senha já está sendo usada")
    elif senha2 == usuario2:      
        print("Senha deve ser diferente do usuario")
    else:
        print("Conta criada")
        break