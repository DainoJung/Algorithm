import math
A, B, V = map(int, input().split())

day = (V -B) / (A - B)

print(math.ceil(day))

# i = 0
# s = 1
# while True:
#     i += A
#     if i >= V:
#         print(s)
#         break
#     i -= B
#     s += 1