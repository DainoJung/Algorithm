def veriNum(a, b, c, d, e):
   return (a**2 + b**2 + c**2 + d**2 + e**2)%10

A, B, C, D, E = map(int, input().split())

print(veriNum(A, B, C, D, E))