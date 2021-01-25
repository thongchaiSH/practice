'''
คำอธิบาย
จงคำนวณหาค่า 22+42+62+…+n2 โดยที่ค่า n คือ input ที่ได้รับ
'''

n=int(input())
sum=0
for i in range(0,n+1,2):
     sum+=i**2
print(sum)