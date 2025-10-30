idade = int(input('Qual a sua idade? ')) 

if idade >=18: #bloco true
    print("Você pode ser preso ", end= '')
    print("Te desejo uma boa sorte")

else: #bloco false (caso o true não acontecer ele vira o else)
    print('little kid ', end= '')
    print('portanto você não pode ter uma CNH')
print('fim')

#end='' ira juntar as duas prints
