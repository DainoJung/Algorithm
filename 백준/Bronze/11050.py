import math

N, K = map(int, input().split())

C = math.factorial(N)/(math.factorial(K) * math.factorial(N - K))

print(int(C))