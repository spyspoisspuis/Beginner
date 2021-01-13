level = int(input())
pah = input()
speed = int(input())
zoomaster = input()

if zoomaster == 'Y' :
    level+=2
if level < 4 or  (pah == 'N' and speed > 2) : 
    print("try again")
if level >= 4 :
    if pah == 'Y' or speed <= 2:
        print("Normal Moly!!!")     
if level>=6 :
    if pah == 'Y' or speed <= 1 :
        print("Rare Moly!! How cute!!!")


