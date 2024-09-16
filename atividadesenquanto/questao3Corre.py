contadora = 1
soma = 0
totalnegativos = 0

while contadora <=10:
    valor = int(input(f"Informe o valor {contadora}: "))
    
    if valor< 0:
      totalnegativos = totalnegativos + 1
    else:
        soma = soma + valor
print(f"A soma dos positivos é {soma}")
print(f"O total de negativos é {totalnegativos}")