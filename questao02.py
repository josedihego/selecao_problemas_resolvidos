arquivo_entrada = open('entrada_saida.txt', 'r')
arquivo_saida = open('compilado.txt', 'w')

linhas = arquivo_entrada.readlines()

for l in linhas:
    partes = l.split(' ')
    arquivo_saida.write(partes[0])
    soma = 0
    for e in partes[1:]:
        soma = soma + eval(e)
    arquivo_saida.write(' ' + str(soma)+'\n')

arquivo_saida.close()
arquivo_entrada.close()