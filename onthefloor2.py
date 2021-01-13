num = list(input())
negative = False
cnt = cnt2 = idx = 0
allzero = True

if num[0] == '-': #เป็นลบหรือป่าว
    negative = True

for i in range (len(num)) :
    if cnt >= 1 and num[i] != '0' : #ถ้่าหลังจุดมีตัวไม่เท่ากับ 0 ก็ให้ตัวที่ใช้เช็คว่าเป็น 00 หรือป่าว เป็น false
        allzero = False 
    if cnt >= 1 : #เปลี่ยนทุกตัวหลังจุดเป็น 0
        num[i] = '0'
        cnt += 1
    if num[i] == "." : #เก็บค่าตำแหน่งทีี่เป็น . และให้เริ่มงาน cnt 
        cnt = 1
        idx = i-1
if cnt > 0 : # ไม่ใช่จำนวนเต็ม
    if allzero and negative and num[1] == '0': # 0.0 หรือ 0.00 ลบ - ออก
         num.remove('-')
    elif negative and not allzero: #เป็นลบและไม่ใช่ .00 ก็เพิ่มค่าด้านหน้า เพราะลองปัดลงแล้วคะแนนน้อยครับ เช่น -1.5 ต้องตอบ -2.00
        temp = int(num[idx])
        temp += 1
        num[idx] = temp

if cnt == 0 : #append . if cnt = 0
    num.append('.')
    if negative and num[1] == '0' :
        num.remove('-')

if cnt <= 2 : #append 0
    for i in range (3-cnt) :
        num.append("0")

for i in num : #print 
    print(i,end="")
    if cnt2 >= 1 :
        cnt2 += 1
    if i == '.' :
        cnt2 = 1
    if cnt2 == 3 :
        break  