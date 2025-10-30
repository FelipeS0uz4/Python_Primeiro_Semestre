Pa,Pb = input().split()
Pc,Pd = input().split()

Pa = float(Pa)
Pb = float(Pb)
Pc = float(Pc)
Pd = float(Pd)

distancia = ((Pa - Pc)**2 + (Pb - Pd)**2)**(1/2)
print (f'{distancia:.4f}')
