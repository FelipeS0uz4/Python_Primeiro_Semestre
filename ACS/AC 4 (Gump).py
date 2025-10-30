tempo = []
quantos = 0
n2 = 0
while True:
    n1 = int(input())
    if n1 < 0:
        break
    tempo.append(n1)
    quantos +=1
    n2 += n1
    

media =  n2/quantos
print(f"MEDIA: {media:.2f}")

abaixo_da_media = [n1 for n1 in tempo if n1 < media]
for tempo in abaixo_da_media:
    print(tempo)
