x1,y1 = (input()).split(",")
x2,y2 = (input()).split(",")

y1,x1,y2,x2 = map(float, [y1,x1,y2,x2])
distancia= ((x1-x2)**2+(y1-y2)**2)**(1/2)
print (f'{distancia:.4f}')
