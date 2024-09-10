idade = int(input("Qual sua idade? :"))

if idade < 12:
    print("Você é criançã!")
elif idade >=12 and idade <=18:
    print("Adolescente")
elif idade >= 19 and idade <=60:
    print("Adulto")
else:
    print("Já é um idoso") 
    