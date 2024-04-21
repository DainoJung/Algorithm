N = int(input())
number = 1
cnt = 1

while N > number:
    number += 6 * cnt
    cnt += 1
print(cnt)