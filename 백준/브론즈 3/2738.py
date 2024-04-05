N, M = map(int, input().split())

list1 = []

for i in range(N * 2):
    list1.append(list(map(int, input().split())))

for i in range(N):
    array1 = list1[i]
    array2 = list1[N + i]
    for i in range(M):
        print(array1[i] + array2[i], end=" ")
    print("")