pedido=input().split()
cod=int(pedido[0])
qntd=int(pedido[1])

if cod==1:
     price=4.00*qntd
if cod==2:
     price=4.50*qntd
if cod==3:
     price=5.00*qntd
if cod==4:
     price=2.00*qntd
if cod==5:
     price=1.50*qntd

print("Total: R$ %.2f" %price)
