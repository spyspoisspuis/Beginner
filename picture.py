n = int(input())

for i in range(n) :
    for j in range (n-i):
        print(j,end="")
    for j in range(i+1):
        if j == 0 :
            print("X",end = "")
        elif i == n-1 and j == n-1 :
            print("x",end ="")
        else :
            print("o",end ="")
    for j in range(i) :
        if i-1 == j :
            print("X",end = "")
        else :
            print("o",end ="")
    for j in range(n-1-i,-1,-1):
        print(j,end="")
    print("")
for i in range(n+1) :
    if i == 0 or i== n :
        print("X")
    elif i== n or i==n+1 or i==n+2 :
        print("x")
    else :
        print("o")
print("")
for i in range (n) :
    for j in range (i):
        print(j,end="")
    for j in range (n-1-i,-1,-1):
        if j==0:
            print("X")
        elif j==n-1 and i==0 :
            print("x")
        else :
            print("o")
    print("")