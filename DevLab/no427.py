'''
https://www.borntodev.com/grader/?quizNo=427
คำอธิบาย

รับinput 2 ตัว เป็นเลขจำนวนเต็ม ให้หาว่าระหว่างเลขนั้นมีเลข 9 อยู่กี่ตัว

เช่น 0-10 มี 9 อยู่ 1 ตัว คือ 9

80 - 100 มี 9 อยู่ 12 ตัว คือ 89 90 91 92 93 94 95 96 97 98 99(นับเป็น 2)

ex
input: 
10
30

output:
3

'''
a= int(input())
b= int(input())
sum9=0
for i in range(a,b+1):
    sum9+=str(i).count("9")
print(sum9)
