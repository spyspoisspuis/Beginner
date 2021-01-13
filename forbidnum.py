e = ""
n = int(input())
if 1 <= n <= 100 :
    for i in range(n):
        if i<10 :
            e += ("0"+str(i))
        else :
            e+= str(i)
    q = int(input())
    if 0 <= q <= n:
        for i in range(q):
            newst = ""
            j = int (input())
            if j < 10 :
                newst = "0"+str(j)
            else :
                 newst = str(j)
            if newst in e :
                e = e.replace(newst,"")
 
        cnt = 0
        cnt2=0
        for k in range(n):
            newst= ""
            if cnt == 5:
                print("")
                cnt = 0
            if k < 10:
                newst = "0"+str(k)
            else :
                newst = str(k)
            if newst in e :
                if cnt2 != n-q-1 :
                    print(newst+" ",end="")
                    cnt += 1
                    cnt2+=1
                else :
                    print(newst)

        