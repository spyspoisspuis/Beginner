skillName = input()
level = int(input())
itemName = input()
itemPrice = int(input())
newPrice = 0
if level < 10 :
    newPrice = itemPrice * ((5+(2*level))/100)
else :
    newPrice = itemPrice * (24/100)

if skillName == 'DC':
    if itemPrice == 1 :
        print("[DC LV.",level,"]"," ",itemName,": ",itemPrice," z -> 1 z")
    else :
        print("[DC LV.",level,"]"," ",itemName,": ",itemPrice," z -> ",itemPrice - newPrice," z")
else :
    print("[OC LV.",level,"]"," ",itemName,": ",itemPrice," z -> ",itemPrice + newPrice," z")