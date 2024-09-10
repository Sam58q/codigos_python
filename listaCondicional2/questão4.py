salario = float(input("Quanto você recebe? :"))

if salario <= 1900:
    print("Isento")
elif salario >= 1901 and salario <= 2800:
    imposto = salario * 0.075
    print(f"O imposto em cima do seu salário é: {imposto:.2f}")
elif salario >= 2801 and salario <= 3700:
    imposto = salario * 0.15
    print(f"O imposto em cima do deu salário é: {imposto:.2f}")
elif salario > 3700:
    imposto = salario * 0.225
    print(f"O imposto em cima  do seu salário é : {imposto:.2f}")
    