N = int(input())
A = list(map(int, input().split()))
M = max(A)
B = []
sum = 0

for i in range(N):
    A[i]=A[i]/M*100
    sum+=A[i]

print(sum/N)