N = int(input())

num2 = list(map(int, input().split()))

h = 0

for i in num2:
    num = []
    for j in range(1, i + 1):
        if i % j == 0:
            num.append(j)
    if len(num) == 2:
        h += 1

print(h)
