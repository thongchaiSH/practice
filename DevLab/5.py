'''
คำนวณเกรด
คำอธิบาย
โดยการคำนวณเกรดนั้นจะมีการให้คะแนนตามเกรดแต่ละช่วงเป็น 80- 100 ได้เกรด A , 70 - 79 ได้เกรด B , 60 - 69 ได้เกรด C , 50 - 59 ได้เกรด D และ ต่ำกว่า 50 จะได้เกรด F โดยผู้ใช้จะต้องกรอกเป็นตัวเลขจำนวนเต็มเท่านั้น
'''

# num=69
num=int(input())
if num>=80 and num <=100:
    print("A")
elif num>=70:
    print("B")
elif num>=60:
    print("C")
elif num>=50:
    print("D")
else :
    print("F")