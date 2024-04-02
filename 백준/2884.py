H, M = map(int, input().split())

if(H == 0 ):
    if(M == 45):
        print(0, 0)
    elif(M < 45):
        print(23, M + 15)
    else:
        print(H, M - 45)
elif(M > 45):
    print(H, M - 45)
elif(M < 45):
    print(H - 1, M + 15)
else:
    print(H, 0)