discountcode = input()
num = ""
for i in discountcode :
   if i.isdigit() :
       num += i
discountpercent = 1- float(int(num)/100)

x,y = input().split()
x = int(x)
y = int(y)
aream = x*y

xprice,yprice = input().split()
xprice = int(xprice)
yprice = int(yprice)

workerhour = int(input())

yamount = xamount = aream//2
if aream%2 == 1 :
    xamount+=1
tileprice = (yamount*yprice) + (xamount*xprice)

areaw = float(aream/4)
workerprice = workerhour*areaw
print(type(workerprice))
totalprice = tileprice+workerprice
discountprice = (tileprice*discountpercent)+workerprice

print(totalprice)
print(discountprice)
print(aream)
print(workerprice)

for i in range(x):
    for j in range(y):
        if (i+j)%2 == 0 :
            print("X",end="")
        else :
            print("Y",end="") 
    print("")