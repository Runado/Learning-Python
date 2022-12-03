#DICIONARIO

usuarios={}
opcao=input("O que deseja realizar?
" +
            "<I> - Para Inserir um usuário
"+
            "<P> - Para Pesquisar um usuário
"+
            "<E> - Para Excluir um usuário
"+
            "<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a última data de acesso: ")
        estacao=input("Qual a última estação acessada: ").upper()
        usuarios[chave]=[nome, data, estacao]
    opcao = input("O que deseja realizar?
" +
                  "<I> - Para Inserir um usuário
" +
                  "<P> - Para Pesquisar um usuário
" +
                  "<E> - Para Excluir um usuário
" +
                  "<L> - Para Listar um usuário: ").upper()



##### OUTRA FORMA DE PREENCHER O DICIONARIO USUARIOS TAMBÉM, ECONOMIZANDO ESPAÇO NA MEMÓRIA, INSERINDO INPUT DENTRO DA CHAVE ####
#chave=input("Digite o login: ").upper()
#usuarios[chave]=[input("Digite o nome: ").upper(),
 #                input("Digite a última data de acesso: "),
  #               input("Qual a última estação acessada: ").upper()]

#IMPORTANTE NÃO COLOCAR A INPUT PARA DECLARAR A CHAVE pois é uma característica do PYTHON sempre resolver primeiro o que está após o sinal de igual.





#MANEIRA MENOS ENXUTA DE FAZER ESSE CÓDIGO
def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)


usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()



    #METODOS QUE PODEM SER USADOS PARA DICIONARIOS
    #items() irá retornar uma tupla com a chave e dados de cada elemento.
    #values() este método retorna apenas os valores que seriam os dados e não as chaves.
    #keys() este métoddo irá retornar apenas as chaves que compõem cada elemento.
    #has_key() este método irá verificar se a chave existe retornando (1) True ou (0) False.
    #clear() este método irá limpar todos os dados contidos no dicionario
    #popitem() este é um método próprio para quem deseja montar algum dicionario que contenha elementos que serão executados, de maneira aleatória, individualmente e, na sequência, deverão ser eliminados do dicionário. Poderíamos pensar em um dicinário com dicas, e à medida que cada dica fosse exibida, automaticamente ela deveria ser retirada do dicionário
    #Dados Voláteis