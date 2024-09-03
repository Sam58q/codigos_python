nome = input("Informe seu nome: ")
end = input("Informe seu endereço: ")
idade = input("informe sua idade: ")
# Exibindo dados das variáveis
#print(nome,end,idade)

#1ª forma de concatenação
#print("\nOlá",nome,"seu endereço é ","sua idade é ", idade)

#2ª forma de concatenação

#print("\nOlá {} seu endereço é {} e sua idade é {}".format(nome,end,idade))

#3ª formar de concatenação  - f string
print(f"Bem vind@{nome},você mora no {end} e tem {idade}anos")