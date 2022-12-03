#Lendo arquivos JSON
import json
with open ("nomedoarquivojson",  "r") as arq_json:
  dic = json.load(arq_json)
  for chave.dados in dic.items():
    print (chave + " " + str(dados))

# with   open("bd1.json", "w") as json_file:
#json.dump(nome da variavel, nome do arquivo) serve para gerar um arquivo com as informações que contém no dicionario que está contido em uma variavel
