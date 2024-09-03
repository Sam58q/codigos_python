distancia = float(input("Qual a distancia?: "))
tempo = float(input("Quanto tempo?: "))



velocidade = (distancia*1000)/(tempo*60)
print(f"A velociade que o projetil percorre é {velocidade:.2f}m/s")