# Trabalhando com tuplas

objetos = ('Lapis','Borracha','Caderno')

print(type(objetos))# A função type() irá exibir o tipo da variável 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)
print(objetos[1])# Estamos exibindo apenas um item, que está na posição 1


# Exibindo todos os dados da tupla
print('-'*50)
for item in range(0,3):
    print(objetos[item])

# Exibindo todos os dados sem a função range
print('-'*50)

for item in objetos:
    print(item)
    
# Tentando mudar o conteúdo da tupla

print('-'*50)

objetos[0] = "Caneta" # Irá ocorrer um erro pois os valores de uma tupla são imutáveis
print(objetos)