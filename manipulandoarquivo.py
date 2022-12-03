## Manipulando Arquivos
import os

# Meu Primeiro Arquivo
# arquivo = open ("Arquivo.txt", "w") # a Função open tem a seguinte sintaxe ("Caminho do arquivo", privilégio)
# Privilégios: (R) Arquivo apenas para leitura (W) arquivo apenas para escrita (A) Append para leitura e escrita (x) Modo exclusivo quem abrir o arquivo consegue ler e escrever mas enquanto essa pessoa não fechar o arquivo não é possível fazer nenhuma alteração.
# arquivo.write(" José Lucas ramos de lima") # Escrevendo algo no arquivo
# arquivo.close # fechando o arquivo.
texto = int(input(" você deseja criar um arquivo de texto:   [1] SIM [2] NAO"))

while texto == 1:
    escrever = input(" Pronto, o Arquivo de texto foi criado, agora insira a frase que você deseja colocar nele:  ")
    salvar = int(
        input(" \n \n {}  \n \n Deseja salvar a seguinte frase no arquivo [1] SIM ou [2] NAO: ".format(escrever)))
    if (salvar == 1):
        with open("arquivo.txt", "w") as arquivo:
            arquivo.write(escrever)
            arquivo.close
            with open("arquivo.txt", "r") as arquivo:
                ler = input("Você deseja ler o arquivo digite [1] SIM e [2] NAO")
                if (ler == 1):
                    conteudo = arquivo.read()
                    print(conteudo)

# conteudo = arquivo.read() Lê o arquivo todo ao invés do comando .readline que irá ler linha por linha
# print(conteudo)


# for linha in arquivo.readline():  ler uma linha de cada vez que contém no arquivo e depois printa ela
# print (linha)

# Programa para ler arquivos JSON







