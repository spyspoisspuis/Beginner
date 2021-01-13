import math
num = int(input())
cnt = 0
isprime = issuperprime = False
if num < 2 :
    print("Nope")
elif num == 2 :
    print("is Prime")
else :
    for i in range(2,int(math.sqrt(num))+1) :
        if num % i == 0 :
            break;
    else :
        isprime = True
    if isprime : 
        for i in range(2,num+1) :
            check = True
            for j in range(2,int(math.sqrt(i))+1) :
                if i%j == 0 :
                    check = False
                    break;
            if check :
                cnt += 1 
        for i in range(2,int(math.sqrt(cnt))+1) :
            if cnt % i == 0:
                break;
        else :
            issuperprime = True
    
    if issuperprime :
        print("is Super Prime")
    elif isprime :
        print("is Prime")
    else :
        print("Nope")