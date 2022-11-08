
n = int(input('Informe um número : '))

def ehPrimo(numero):
    if(numero>1):
        if(numero==2): return True
        else:
            divisor = 2
            while(divisor < numero):
                if(numero%divisor==0):
                    return False
                divisor = divisor +1
            return True
    else:
        return False

print(ehPrimo(n))