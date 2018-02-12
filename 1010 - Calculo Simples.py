# -*- coding: utf-8 -*-
'''Autor: Alessandra Souza
Data:  05/05/2017
Objetivo: Calcular o Total. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
ID Urionlinejudge: 1010'''

pc1=input().split()

cod1=int(pc1[0])
qtd1=int(pc1[1])
val1=float(pc1[2])

pc2=input().split()

cod2=int(pc2[0])
qtd2=int(pc2[1])
val2=float(pc2[2])

tot=(qtd1*val1)+(qtd2*val2)
print("VALOR A PAGAR: R$ %.2f" %tot)
