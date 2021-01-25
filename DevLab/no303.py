'''
https://www.borntodev.com/grader/?quizNo=303
3+5+1+8+9
output:
1+3+5+8+9

input:
1+2+3+1+2+3+1+2+3+1+2+3
output:
1+1+1+1+2+2+2+2+3+3+3+3
'''
number="4+7+9+2+1+0+1+4564+421"
# number=input()
number=number.split("+")
#Convert list string to int
map_object = map(int, number) 
number=list(map_object)
number.sort()
# print(number)
result=""
for i in number:
    result+=str(i)+"+"
result=result[:-1]
print(result)
