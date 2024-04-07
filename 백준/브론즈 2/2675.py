T = int(input())

for i in range(T):
    list1 = list(map(str, input().split()))
    for i in list1[1]:
        print(i * int(list1[0]), end="")
    print("")