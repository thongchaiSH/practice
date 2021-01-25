'''
คำอธิบาย
ให้หาว่าจากที่ list ของเลขที่กำหนดให้ ตัวไหนบ้างที่หารด้วย 7 ลงตัวและหารด้วย 11 ไม่ลงตัว

รูปแบบ Input
list ของเลขจำนวนหนึ่ง

รูปแบบ Output
list ของเลขที่หารด้วย 7 ลงตัว แต่หารด้วย 11 ไม่ลงตัว (ถ้าใน list ที่กำหนดให้มีเลข 1 ให้แสดงใน output ด้วย)
'''
# number="7,17,27,37,47,57,67,77"
number=input()
result=""
for num in number.split(","):
    num=int(num)
    if (num%7==0 and num%11 !=0) or num==1:
        result+=str(num)+","

result=result[:-1]
print(result)