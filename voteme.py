num = int(input())
mid = (num-1)//2
for i in range(mid) :
    for j in range(mid) :
        if i == 0 or j == 0 or i == j:
            print("*",end="")
        else :
            print(" ",end="")
    if i== 0 :
        print("*",end="")
    else :
        print(" ",end="")
    for j in range(mid) :
        if i == 0 or j== mid-1 or i+j == mid-1 :
            print("*",end="")
        else :
            print(" ",end="")

    print("")
for i in range(num) :
    if i== 0 or i == mid or i == num-1 :
        print("*",end="")
    else :
        print(" ",end="")
print("")
for i in range (mid) :
    for j in range (mid) :
        if i == mid-1 or j== 0 or i+j == mid-1 :
            print("*",end = "")
        else :
            print(" ",end="")
    if i == mid -1 :
        print("*",end="")
    else :
        print(" ",end= "")
    for j in range(mid) :
        if i == mid-1 or j== mid-1 or i==j:
            print("*",end = "")
        else :
            print(" ",end ="")

    print("")