N = str(input())

S = ""

for i in N:
    if(i.isupper()):
       S += i.lower()
    else:
       S += i.upper()

print(S)