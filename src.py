from math import sqrt 
x=25 
y=0 
prevtup=(5,0) 
c=0 
while x>=0: 
    x-=0.0001 
    if x<0: 
        pass 
    else: 
        mx=sqrt(x) 
    y+=0.0001 
    my=sqrt(y) 
    curtup=(mx,my) 
    d=((curtup[0]-prevtup[0]))**2+((curtup[1]-prevtup[1]))**2 
    d=sqrt(d) 
    c+=d 
    prevtup=curtup 
cir=c*4 
pie=cir/10.00 
print(pie)
