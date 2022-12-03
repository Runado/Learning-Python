import json
inventario = {}


def chamarMenu():
   escolha = int(input("Digite <1> para registrar um novo equipamento em estoque ou <2> para exibir os equipamentos armazenados: "))
   return escolha

while True:

    funcao = chamarMenu()

    if funcao == 1:

        for chave in range(1,10000):
            serial = input("Qual o número de serial do equipamento: ")
            inventario[serial]=(input("\n  <Comercial> \n <Corporativo> \n <Vendas> \n <SAC> \n <Financeiro> \n <Administrativo> \n <Operações> \nEste equipamento é proveniente de  qual setor(Digite o Nome do setor): "),input("\nQual o Modelo deste equipamento de rede? "),input("\nQual a Marca deste equipamento de rede? "),input("\nQuantas portas ethernet este equipamento possuí? "),input("\nQual o IP deste equipamento? "),input("\nQual o Preço deste equipamento? "))
            print(inventario)
            continuar = input("\n DIGITE EXIT SE VOCÊ TIVER TERMINADO DE CADASTRAR OU APERTE ENTER PARA CONTINUAR")
            if continuar == "exit":
                break
    elif funcao == 2:
        segundaescolha = int(input("Digite <1> se deseja pesquisar ou digite <2> se deseja ver todos os resultados: "))
        if segundaescolha == 1:
            pesquisa = inventario.get(input("Qual o serial do equipamento?: "))
            print(pesquisa)
            setor = print ("Este equipamento atualmente está no Setor: " + pesquisa[0])
            modelo = print ("O Modelo deste equipamento é o:  " + pesquisa[1])
            marca = print("Este equipamento pertence a marca: " + pesquisa[2])
            portas = print("Este equipamento atualmente possuí: " + pesquisa[3] + " Portas Ethernet's")
            ip = print("Este equipamento foi configurado com o Endereço IP: " + pesquisa[4])
            preco = print("Este equipamento custa: " + pesquisa[5] + " R$")
        if segundaescolha == 2:
            with open("inventario.json", "w") as arq_json:
                json.dump(inventario, arq_json)
            for chave,dados in inventario.items():
                print("\n                      ------------")
                print("Este Equipamento foi registrado com o número de série: " + chave)
                setor = print ("Estes equipamentos atualmente estão no Setor: " + dados[0])
                modelo = print ("O Modelo deste equipamento é o:  " + dados[1])
                marca = print("Este equipamento pertence a marca: " + dados[2])
                portas = print("Este equipamento atualmente possuí: " + dados[3] + " Portas Ethernet's")
                ip = print("Este equipamento foi configurado com o Endereço IP: " + dados[4])
                valor = print("Este equipamento custa: " + dados[5] + " R$")





