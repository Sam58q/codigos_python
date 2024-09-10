soma = 0# inicializando uma variável 
contador = 0

for cont in range (50, 71):
    
    if cont % 2==0:
        soma += cont # soma = soma + cont
        contador += 1# 
    
    media = soma/contador
    
    print(f"Soma:{soma}")
    print(f"Média:{media}")
    print(f"Total de números lidos:{contador}")