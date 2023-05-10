a = 1
while a:
    A, B = map(int, input().split())
    if A and B != 0:
        print(A + B)
    else:
        a = 0
        break