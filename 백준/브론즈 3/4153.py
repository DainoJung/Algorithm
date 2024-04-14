while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    else:
        if A*A + B*B == C*C or B*B + C*C == A*A or A*A + C*C == B*B:
            print("right")
        else:
            print("wrong")