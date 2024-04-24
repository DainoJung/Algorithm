K = int(input())

num = []

for i in range(K):
    j = int(input())
    if j == 0:
        if num:
            num.pop()
    else:
        num.append(j)

S = sum(num)

print(S)