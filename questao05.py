
def fatorial(n):
    if(n==0): return 1
    else:
        return n * fatorial(n-1)

print(fatorial(0))
print(fatorial(5))
print(fatorial(10))