# a = "Chicken rice"
# b = "Noodle"
# c = "Noodle"
# d = "Noodle"

a = "Chicken rice"
b = "Noodle"
c = "Noodle"
d = "ChickEn Rice" #Noodle

# a = input()
# b = input()
# c = input()
# d = input()

lis = [a.lower(), b.lower(), c.lower(), d.lower()]
dicc = {"count": 0, "value": ""}

if lis.count("noodle") == 2:
    print(d.capitalize())
else :
    for item in lis:
        if lis.count(item) > dicc['count']:
            dicc['count'] = lis.count(item)
            dicc['value'] = item
    print(dicc['value'].capitalize())
