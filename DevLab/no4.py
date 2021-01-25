'''
 พีระมิด (ระดับ 3)
 https://www.borntodev.com/grader/?quizNo=4
'''
n=3
# n=n+1
for x in range(1,n):
  for y in range(n - x):
    print (" ",end="")
  for y in range(1,x + 1):
    print(y,end="")
  for y in range(2,x + 1):
    print(x - y + 1,end="")
  print()
#============================
for x in range(4,0,-1):
  for y in range(n - x):
    print (" ",end="")
  for y in range(1,x + 1):
    print(y,end="")
  for y in range(2,x + 1):
    print(x - y + 1,end="")  
  print()