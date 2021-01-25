'''
https://www.borntodev.com/grader/?quizNo=416
ตัวอย่าง
n = 10
นาย X จำเป็นต้องใช้ลูกดอกอย่างน้อย 2 ดอก กล่าวคือ นาย X จะปาลงช่องที่มี 5 คะแนน ถึง 2 ครั้ง (5+5=10)

10->2
13->3
27->6
'''
import math

a=int(input())
print(math.ceil(a/5))