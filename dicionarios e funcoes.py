# Sintaxe Dicionario =  {"CHAVE":"VALOR"} o  caractér que separa a chave do valor que irá receber são os dois pontos :
dicionario = {"NOME":"JOSE", "IDADE":"22", "CPF":"49439384958"}
# a Chave nome irá receber o valor JOSE, ac have idade irá receber o valor 22

#printando a chave nome
print(dicionario["NOME"])
#printando a chave idade
print(dicionario["IDADE"])
#printando a chave CPF
print(dicionario["CPF"])
print ("----------------------------------------------")
#printando todas as chaves do meu dicionario
for chaves in dicionario:
  print(chaves)
print ("----------------------------------------------")
#printando a chave e o valor delas
for chave in dicionario:
  print(chave+":"+dicionario[chave])
print ("----------------------------------------------")
#convertendo o dicionario em uma tupla e irá me  retornar os itens que estão no dicionario
for i in dicionario.items():
  print(i)
# irá me retornar apenas os valores que estão contidos nas chaves do dicionario
print ("----------------------------------------------")
for i in dicionario.values():
  print (i)
# ira me retornar apenas as chaves que estão contidas no dicionario
print ("----------------------------------------------")
for i in dicionario.keys():
  print (i)