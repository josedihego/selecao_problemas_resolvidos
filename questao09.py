m = 15
n = 10
max = 0
ponto_max = (0,0)
for x in range(0,m):
    for y in range(0,n):
        exp = x * y - pow(x,2) + y
        if(exp > max):
            max = exp
            ponto_max = (x,y)
print(max)
print(ponto_max)