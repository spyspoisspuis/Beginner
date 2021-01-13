while True :
    num = list(input())
    cnt = cnt2 = 0
    check1= False
    check2 = False
    idx = 0
    for i in range(len(num)) :
        if num[i] == '-' :
            check1 = True
        if cnt >= 1: 
            if num[i] == '0' :
                check2 = True
            else :
                check2 = False
            num[i] = '0'     
            cnt+=1 
        if  num[i] == "." :
            cnt = 1   
            idx = i 
    if check1 and num[1] == '0' :
        num.remove('-')
    if  check2 :
        check1 = False
    if check1 and cnt != 0 :
        temp = int(num[idx-1])
        temp += 1
        num[idx-1] = temp
    if cnt == 0 :
        num.append(".")
    if cnt <= 2 :
        for i in range(3-cnt):
            num.append("0")
    for i in num:
        if cnt2 >=1 :
            cnt2+=1 
        if  cnt2 <=3 :
            print(i,end="")
        if i == "." :
            cnt2 = 1