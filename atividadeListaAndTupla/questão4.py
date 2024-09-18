temperaturas_anuais = []


for temperatura in range(2):
  temperaturas_anuais = input(f"Qual a temperatura do mês {temperatura+1}: ")
  mediaAnual = temperaturas_anuais % 12

print(mediaAnual)