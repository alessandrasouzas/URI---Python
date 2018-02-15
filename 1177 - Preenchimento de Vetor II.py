T = int(input())
N = 0
while N < 1000:
    cont = 0
    while cont < T and N < 1000:
        print("N[" + str(N) + "] = " + str(cont))
        cont += 1
        N += 1
    cont = 0
