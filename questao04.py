
def fibonacci(indice):
    if(indice==0): return 0
    elif(indice==1): return 1
    else:
        return fibonacci(indice-1) + fibonacci(indice-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(14))
print(fibonacci(19))
print(fibonacci(30))