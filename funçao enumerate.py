##Função Enumerate é útil para enumerar todos os dados de uma  lista com um numero identificador.
##a função LIST retorna uma tupla que pode ser consultada através de índices.
usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()
tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome"), input("Digite o nível")]