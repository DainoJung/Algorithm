N, M = map(int, input().split())

for i in range(min(N, M), 0, -1):
    if N % i == 0 and M % i == 0:
        print(i)
        j = i * M / i * N / i
        print(int(j))
        break