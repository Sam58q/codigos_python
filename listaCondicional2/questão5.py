horas = float(input("Quantas horas trabalhadas? : "))
valHora = float(input("Quanto você recebe por hora? : "))

if horas > 40 :
    bonus = valHora * horas * 0.50
    print(f"Parabens você recebeu um bonus de {bonus:.2f}")
  