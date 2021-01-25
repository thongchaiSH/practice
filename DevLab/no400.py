'''
https://www.borntodev.com/grader/?quizNo=400
เรียงไพ่ (BLACKJACK)
คำอธิบาย

จงเขียนโปรแกรมเรียงไพ่จากน้อยไปมาก โดยมีเงื่อนไขว่า A < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < J < Q < K

input:
5 2 K J A
output
A 2 5 J K
'''
inp=input()
# inp="5 2 K J A"
dic={
    "A":0,
    "J":10,
    "Q":11,
    "K":12
}
result={}
for item in inp.split() :
    if item in dic:
        result[item]=dic[item]
    else:
        result[item]=int(item)

strResult=""
#sort key
for k,v in sorted(result.items(), key=lambda item: item[1]):
    strResult+=k+" "
print(strResult.strip())