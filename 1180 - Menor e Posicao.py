n = int(input())
a = input().split()
cont = 0
x = []
while cont < n:
    num = int(a[cont])
    x.append(num)
    cont += 1
print("Menor valor:",min(x))
print("Posicao:",x.index((min(x))))

