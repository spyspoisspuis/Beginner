w,w2 = input("Enter w : ").split()
h,h2 = input("Enter h : ").split()
w,h = float(w),float(h)
if w2 == 'lbs' :
    wei = w/2.205
elif w2 == 'kg' :
    wei = w 

if h2 == 'cm' :
    hei = h / 100
elif h2 == 'ft' :
    hei = h/3.2808399
elif h2 == 'm' :
    hei = h 

bmi = wei/(hei**2)
print(w,wei,h,hei,bmi,wei/(hei**2))
    
    
    
