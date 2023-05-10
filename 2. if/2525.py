A, B = map(int, input().split())
C = int(input())

if A == 23 and B + C > 59:
    A = 0
    print(A+(((B+C)//60)-1), (B+C)%60)

elif B + C > 59:
    if A+((B+C)//60) >= 24:
        print((A+((B+C)//60)-24), (B+C)%60)
    else:
        print(A+((B+C)//60), (B+C)%60)

else:
    print(A, B+C)
