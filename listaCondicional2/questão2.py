ano = int(input("Qual o ano? : "))

if ano % 400 == 0 or ano % 4 == 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")

#if(ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 outra forma de fazer 