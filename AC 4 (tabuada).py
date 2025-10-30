primeiro = int(input())
segundo = int(input())

if primeiro > segundo:
    print("Nenhuma tabuada no intervalo!")
else:
    for x in range(primeiro, segundo+1):
        for y in range(1, 11):
            print(f"{x} x {y} = {x*y}")
        print("----------")
