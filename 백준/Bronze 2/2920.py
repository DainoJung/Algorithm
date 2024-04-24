note  = list(map(int, input().split()))

if note == list(range(1, 9)):
    print("ascending")
elif note == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")