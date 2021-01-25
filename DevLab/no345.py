'''
https://www.borntodev.com/grader/?quizNo=345
input:
python
output:
pYtHoN
'''
txt=input()
# txt="tank"
txt.lower()

for i in range(len(txt)):
    if i%2==0 :
        print(txt[i],end="")
    else:
        print(txt[i].upper(),end="")
