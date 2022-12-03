#Strings são objetos e podem ser aplicados métodos nelas.



jose = " meu * nome * é * jose    "
print ("----------------------------------------------")
print (jose[8])
print (jose[9])
print (jose[12])
print (jose[14])
print (jose[0:12])
print (jose[2:14])
print (jose[0:11])
print (jose[0:17])
print ("----------------------------------------------")
#colocando o texto em minúsculo
print ("----------------------------------------------")
print (jose.lower())
print ("----------------------------------------------")
#colocando o texto em maiúsculo
print ("----------------------------------------------")
print (jose.upper())
print ("----------------------------------------------")
#remove espaço ou caracteres especiais no inicio e no fim da string
print ("----------------------------------------------")
print (jose.strip())
print ("----------------------------------------------")
#Converte a string em uma lista e dentro do parenteses eu escolho os caracteres que ele ira utilizar para quebrar o  texto
print ("----------------------------------------------")
print  (jose.split())
print  (jose.split("*"))
print ("----------------------------------------------")
#metodo find é utilizado para encontrar uma keyword dentro  do texto e retorna o índice em que ele esta.
print ("----------------------------------------------")
busca = jose.find("jose")
print (busca)
print (jose[busca:]) # irá pegar todo o texto esta escrito após a palavra encontrada ou seja apartir do indice 18
print ("----------------------------------------------")
# a palavra jose esta localizada no indice 18

# o metodo replace é utilizado para substituir uma palavra
print ("----------------------------------------------")
substituido = jose.replace("jose","lucas") #substituindo a palavra jose pela palavra lucas
print (substituido)
print ("----------------------------------------------")