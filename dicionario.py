#Dicionarios
meu_dicionario = {"A":"JOSE", "B":"LUCAS", "C":"LIMA"}
for chave in meu_dicionario.items():
  print(chave)
for chave in meu_dicionario.values():
  print(chave)
for chave in meu_dicionario.keys():
  print(chave)
## Abaixo é a primeira forma de adicionar itens onde há o sinal : separando respectivamente a Chave dos Dados nelas contidos.
usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }
##Abaixo está mais um exemplo de criar um dicionario atribuindo o valor da chave como os dados que a ela pertence.
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]

print(usuarios)
print("##############========#########")
# O metodo get irá pesquisar dentro do dicionario todas as chaves que irão iniciar com a string ("Chaves")
print("Dados: ",usuarios.get("Chaves"))


