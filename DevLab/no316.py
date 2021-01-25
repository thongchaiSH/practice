'''
name : Rati
password : 123456789
name(login) : Rati
password(login) : 123456789

Success
'''
name=input("name : ")
password=input("password : ")
while True:
    lname=input("name(login) : ")
    lpass=input("password(login) : ")
    if lname==name and lpass==password :
        print("Success")
        break
    else:
        print("Error")
print("")