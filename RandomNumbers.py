# A biblioteca random ela é responsável por gerar numeros aleatórios e  é pseudo-aleatória isso significa que ela não é totalmente aleatória ja que o funcionamento dela é de tal forma em que ela irá pegar uma dado de entrada e apartir deste dado gerar um OUtput aleatório, o dado de entrada são os mili-segundos do relógio,
import random
random.seed(10) # com o método seed é possível definir um Input para retornar então o valor desejado, ele irá inserir o input e retornar aquele valor esperado(Neste exemplo é o mesmo que considerar o input como 10 milisegundos do relógio)

numero_random = random.random() * 100
print(int(numero_random))
round(numero_random) # Função responsável por Arredondar os dados geraddos

aleatorio = random.randint(0,10)
print(aleatorio)




lista = [1123,123,231,113,2,21,4523,54,37,648,5,97,2546,2,345]
numero = random.choice(lista)

print(numero)