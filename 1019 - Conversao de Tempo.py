# -*- coding: utf-8 -*-
'''Autor: Alessandra Souza
Data:  06/05/2017
Objetivo: Leia um valor inteiro e informe-o expresso no formato hora:minuto:segundo.
ID Urionlinejudge: 1019'''

N=int(input())

if N<3600:
     h=0
     m=N/60
     s=N%60
else:
     h=N/60**2
     if h>0:
          m=(N%60**2)/60
          s= N%60
     else:
          m=N/60
          s= N%60

print("%d:%d:%d" %(h,m,s))
