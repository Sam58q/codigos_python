while True:
    login1 = input("Informe o seu login: ")
    Senha1 = input("Informe o seu Senha: ")
    
    if login1 != Senha1:
        while True:
            login2 = input("Informe o seu login 2 : ")
            senha2 = input("Informe o seu Senha 2 : ")
            
            if login2 != login1 and login2 != senha2:
                break
           
                