while True :
    num = int(input())
    space = ((num-1)//2)-1
    for i in range((num-1)//2):
        print(" "*i+"\\"+" "*space+"|"+" "*space+"/")
        space -= 1
    print("-"*((num-1)//2)+"+"+"-"*((num-1)//2))
    space += 1
    for i in range(((num-1)//2)-1,-1,-1):
        print(" "*i+"/"+" "*space+"|"+" "*space+"\\")
        space+=1
