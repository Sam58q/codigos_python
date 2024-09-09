'''
Essa estrutura de repetição é a mais comum em qualquer outra linguagem de programação
for (contador = 1; contador <=5; contador++){
    
}'''
# 1ª exemplo 
for contador in range(1,6):
    print(contador)
    
print("-"*50)    
#2ª exemplo
for contador in range(1,11,2):# o 3ª parametro irá aumentar o incremento dos valores que estão sendo exibidos 
    print(contador)
    
print("-"*50)  
#3ª exemplo - Números do maior para o menor 
for contador in range(10,0,-1):
    print(contador,end="")# o comando end, informa como o comando python irá mostrar  o final de uma  exibição, por padrão irá dar um enter(\n)                                 