valor = int(input("Digite um número maior que zero: "))

for contador in range(1, valor+1):
    if valor % contador == 0:
     print(contador,end=" ")   