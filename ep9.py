n = int(input())
isPrime  = recheckPrime = True 
isSuperprime = False
cnt = 0
for i in range(2,n//2) :
    if n%i == 0 :
        isPrime = False

if isPrime :
    isSuperprime =True
    for i in range(2,n//2):
        recheckPrime = True
        for j in range(2,i):
            if i%j == 0 :
                recheckPrime = False
        if recheckPrime :
            cnt += 1
    for i in range(2,(cnt+1)//2):
        if cnt%i == 0:
            isSuperprime =False
if n==1 :
    print("Nope")
elif n==2 :
    print("is Prime")
elif isSuperprime:
    print("is Super Prime")
elif isPrime :
    print("is Prime")
else :
    print("Nope")

