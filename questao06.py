import datetime
import random

lista = []
resposta = 0
for i in range(10):
    x = random.randint(1,20)
    resposta = resposta + x
    lista.append(x)

print('Informe a soma dos números: {}'.format(lista))
inicio = datetime.datetime.now()
tentativa = int(input('Sua resposta: '))
fim =  datetime.datetime.now()
if(fim-inicio).seconds <=30:
    if(tentativa == resposta):
        print('Você acertou a resposta')
    else:
        print('Você errou. Resposta correta: {}'.format(resposta))
else:
    print('Tempo esgotado')