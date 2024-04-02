H, M = map(int, input().split())

T = int(input())

if(M + T > 60):
    if((H + int((M+T)/60)) >= 24):
        print(int((H + int((M+T)/60))%24), int((M+T)%60))
    else:
        print(H + int((M+T)/60), int((M+T)%60))
elif(M + T < 60):
    print(H, M + T)
elif(H + int((M+T)/60) != 24):
    print(H + int((M+T)/60), 0)
else:
    print(0, 0)