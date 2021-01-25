'''
Input a numbers : 65 66 67
ABC
'''
text="Input a numbers : 84 85 78"
# text=input()
for item in text.split():
    if item.isnumeric():
        print(chr(int(item)),end="")