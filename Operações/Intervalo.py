intervalo = float(input())

if 0 <= intervalo <=25:
    print ('Intervalo [0,25]')
elif 25 < intervalo <=50:
    print ('Intervalo (25,50]')
elif 50 < intervalo <=75:
    print ('Intervalo (50,75]')
elif 75 < intervalo <= 100:
    print('Intervalo (75,100)')
else:
    print('Fora de Intervalo')



