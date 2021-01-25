'''
คำอธิบาย
จงเขียนโปรแกรมรับค่าจำนวนเต็ม 1 จำนวนจากแป้นพิมพ์(N) จากนั้นให้วน loop รับค่าจำนวนเต็มอีกทั้งหมด n ค่า
จากนั้นหาว่าตัวเลขใดมีค่าที่น้อยที่สุดให้แสดงผลทางหน้าจอ
'''

count=int(input())
min=0
for i in range(count):
    number=int(input())
    if i==0 :
        min =number
    if number<min:
        min=number
print(min)