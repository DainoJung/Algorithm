A = int(input())
B = int(input())
C = int(input())

sum = str(A * B * C)

for i in range(0, 10):
    count = 0
    for n in sum:
        if (n == str(i)):
            count += 1
    print(count)