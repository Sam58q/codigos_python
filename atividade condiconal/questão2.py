salario = float(input("Qual o seu salario?: "))


if salario <= 600:
    aumento = salario*1.30
    print(f"Salario reajustado para {aumento}")
else:
    print("Você nao tem direito a um reajuste")
    
