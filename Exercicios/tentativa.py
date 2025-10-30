def exibir():
    print(f'NOTAS ALTERADAS: {notas_alteradas}')
    N = min(len(lista), len(lista2))
    for i in range(N):
        notas_originais_i = lista[i]
        notas_finais_i = lista2[i]
        if notas_finais_i > notas_originais_i:
            print(f"*{i+1:03}: {notas_originais_i:05.2f} | {notas_finais_i:05.2f}")
        else:
            print(f"-{i+1:03}: {notas_originais_i:05.2f} | {notas_finais_i:05.2f}")


qtd_alunos = int(input())
lista=[]
lista2=[]
notas_alteradas = 0
          
for repeticao in range(1, 2*qtd_alunos + 1):
    entrada = float(input())
    if repeticao <= qtd_alunos:
        lista.append(entrada)
    else:
        idx = repeticao - qtd_alunos - 1
        lista2.append(entrada)
        if entrada > lista[idx]:
            notas_alteradas += 1

exibir()
