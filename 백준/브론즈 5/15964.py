def calculate(a, b):
   return (a + b) * (a - b)
    

A, B = map(int, input().split())

print(calculate(A, B))