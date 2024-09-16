contador = 1# inicializando a variável

while contador <= 5:
    print (contador)
    contador += 1
    
print("="*40)

# 2ª Forma de utilizar o while - loop condocional normal

valor = 0# inicializando a variável 
while valor >=0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar): "))
    print(f"Você digitou {valor}")
    
print("="*40)

#3ª Forma de utilizar while - como se fosse faça..enquanto
while True:
    senha = input("Informe a senha : ")
    if senha == "123":
        print("Parabains, senha correeeta")
        break # Forma de encerrar o while 
    else: 
        print("Senha incorreta, try again")
