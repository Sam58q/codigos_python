pessoa = ["Maria","48","Rua 10"]
print(pessoa)

# Iniciando com dicionário
print('-'*50)
dados_pessoais = {
    'Nome':'Jão',
    'idade':23,
    'Endereço':'Avenida 4'
}

print(dados_pessoais)

#Exibindo as chaves utilizando o comando keys()
print('-'*50)
print(dados_pessoais.keys())

#Exibindo os valores utilizando os values()
print('-'*50)
print(dados_pessoais.values())

#Exibindo tanto a chave quanto o valor com o comando items()
print('-'*50)
print(dados_pessoais.items())

#Exibindo o dicionario detalhado
print('-'*50)
for chave, valor in dados_pessoais.items():
    print(f"{chave}:{valor}")
    
#Realizando operações com dicionário
#Adicionando dados ao dicionário
print('-'*50)

dados_pessoais["Peso"] = 68
print(dados_pessoais)
print('-'*50)

#Forma 2  - usando o comando update()
dados_pessoais.update({"Profissão":"Engenheiro"})
print(dados_pessoais)
print('-'*50)
#Remover dados do dicionário
#Forma 1 - usando pop()
print('-'*50)
dados_pessoais.pop("Endereço")#Preciso passar a chave para poder excluir o registro
print(dados_pessoais)
print('-'*50)
#Forma 2 - usando o del()
del(dados_pessoais["Endereço"])