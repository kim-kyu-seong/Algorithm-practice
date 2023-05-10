X = int(input())
N = int(input())
count = 0

for i in range(0, N):
    a, b = map(int, input().split())
    count = count + (a*b)

if count == X:
    print("Yes")

else:
    print("No")
    