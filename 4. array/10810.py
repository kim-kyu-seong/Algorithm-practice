N, M = map(int, input().split())

basket = list(0 for i in range(0, N))

for i in range(0, M):
    q, r, s = map(int, input().split())
    for i in range(q-1, r):
        basket[i] = s

for i in range(0, N):
    print(basket[i], end=' ')