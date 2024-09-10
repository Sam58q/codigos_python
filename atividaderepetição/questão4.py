initial = int(input("Valor inicial: "))
final = int(input("Valor final: "))
soma = 0#inicializando a variável


for contador in range(initial,final+1):
    soma += contador  
 

print(f"A soma do intervalo de {initial} até {final} é {soma}")
#(f"A soma do intervalo de {} até {} é {} ".format(initial,final,soma))

