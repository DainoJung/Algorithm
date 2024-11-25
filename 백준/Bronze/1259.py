while True:
    N = str(input())
    if N == '0':
        break
    elif N[::-1] == N:
        print('yes')
    else:
        print('no')