'''
รูปแบบ Input
รับค่า n ซึ่งเป็นจำนวนนับ

รูปแบบ Output
คำตอบว่ารากที่ 2 ของ n เป็นจำนวนเต็มหรือทศนิยม
'''
import math
# number=174
number=int(input())
print("Float") if math.sqrt(number) % 1 >0 else print("Integer")
    
