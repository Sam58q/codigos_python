altura = float(input("Qual é a sua altura"))
sexo = int(input("Qual seu sexo(1 - Masculino ,2 - Feminino)"))



if sexo == 1 :
    peso = (72.7*altura-58)
    print(f"Seu peso ideal é:{peso}")
else:
    peso = (62.1*altura-44.7)
    print(f"Seu peso ideal é: {peso:.2f}")
    
    
    