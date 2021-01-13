n = int(input())
time = (n-1)//2
half = ((n+1)//2)-1
for i in range(time) :
    for j in range(n):
        if j == half :
            print("|",end="")
        elif i == j :
            print("\\",end="")
        elif n-i-1 == j :
            print("/",end="")
        else :
            print("+",end="")
    print("")
for i in range(n) :
    if i == half:
        print("+",end="")
    else :
        print("-",end="")
print("")
for i in range(time) :
    for j in range (n) :
        if j == half :
            print("|",end="")
        elif j == half-i-1:
            print("/",end="")
        elif j == half+i+1 :
            print("\\",end="")
        else :
            print(" ",end="")
    print("")
