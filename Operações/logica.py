n1 = int(input())
n2 = int(input())

if n1%11 == 1:
    if n1 % n2 == 1:
        n1 = n2 + 10
    else:
        n2 = n1+10.5
else:
    n1 = n1%11
    if n1%n2 == 0 and n1%2 == 1:
        n2 = n1+5
        
n2 = n2//2+5*n2//3
print(n2)
print(n1)
print(n1+n2%2)


