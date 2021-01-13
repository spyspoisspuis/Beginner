donut = int(input())
largeCount = mediumCount = smallCount = packCount = grabcounter = price = 0  
while donut >= 12:
    donut -= 12
    price += 269
    largeCount += 1
    grabcounter += 1
while donut >= 7:
    grabcounter+=1
    for i in range(2) :
        if donut >= 7:
            donut-=7
            price+= 159
            mediumCount += 1
while donut >= 3:
    grabcounter+=1
    for i in range(4) :
        if donut >= 3:
            donut-=3
            price+= 79
            smallCount += 1
if donut > 0 :
    grabcounter += 1
    price += (donut * 25)
    packCount += donut
if largeCount > 0 :
    print("Large Box : ",largeCount," box(es)")
if mediumCount > 0 :  
    print("Medium Box :" ,mediumCount," box(es)") 
if smallCount > 0 :
    print("Small Box :",smallCount," box(es)") 
if packCount > 0 :
    print("Pack :",packCount," pack(s)") 
print("Price :",price," Baht")
print("Grab :",grabcounter," times")
