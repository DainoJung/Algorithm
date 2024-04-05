N, X = map(int, input().split())

list = list(map(int, input().split()))

for i in list:
    if(i < X):
        print(i, end=" ")