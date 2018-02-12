# -*- coding: utf-8 -*-
'''Autor: Alessandra Souza
Data:  05/05/2017
Objetivo: Leia os quatro valores correspondentes a p1(x1,y1) e p2(x2,y2). Calcule a distância entre eles, mostrando 4 casas decimais após a vírgula.
ID Urionlinejudge: 1015'''

val1=input().split()
x1=float(val1[0])
y1=float(val1[1])

val2=input().split()
x2=float(val2[0])
y2=float(val2[1])

Distancia=((x2-x1)**2 + (y2-y1)**2)**(0.5)
print("%.4f" %Distancia)
