num = int(input())
k = 1000
m = 1000000
b = 1000000000

if -1000 < num < 1000 :
    print(num)
else :
    kcount = float(num/k)
    kcountint = int(round(kcount))
    mcount = float(num/m)
    mcountint = int(round(mcount))
    bcount = float(num/b)
    bocountint = int(round(bcount))

    if (1 <= kcount < 1000) or (-1000 < kcount <= -1) :
        if kcount.is_integer() :
            print("%dK"%kcount)
        else :
            print("%.1fK"%kcount)

    
    if (1<= mcount < 1000) or (-1000 < mcount <= -1) or kcountint == 1000:
        if mcount.is_integer() :
            print("%dM"%mcount)
        else :
            print("%.1fM"%mcount)

    
    if bcount >= 1 or bcount <=-1 or mcountint == 1000:
        if bcount.is_integer() :
            print("%dB"%bocountint)
        else :
            print("%.1fB"%bcount)
       
