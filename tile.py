discountcode = input()
percent =""
for e in discountcode :
    if e.isdigit() :
        percent += e
if not percent:
    percent ="0"
discountpercent = 1 - float(int(percent)/100)

x,y = input().split()
x=int(x)
y=int(y)
xprice,yprice = input().split()
xprice = int(xprice)
yprice = int(yprice)

areameter = x*y
xtile = ytile = areameter//2
if areameter%2 != 0 :
    xtile += 1

workersalary = int(input())
areawah = float (areameter)/4
workerpay = areawah * workersalary

tileprice = (xtile*xprice) + (ytile*yprice)
totalprice = workerpay + tileprice
realprice = (tileprice*discountpercent) + workerpay

print(totalprice)
print(realprice)
print(areameter)
print(workerpay)
for i in range (x) :
    for j in range (y) :
        if (i+j) % 2 == 0 :
            print("X",end="")
        else :
            print("Y",end="")
    print("")