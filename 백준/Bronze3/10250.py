import math

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N%H == 0:
        print(str(H)+ "{0:02}".format(math.ceil(N/H)))
    else:
        print(str(N%H) + "{0:02}".format(math.ceil(N/H)))