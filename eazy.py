str_1 = input("enter sting 1 :")
str_2 = input("enter sting 2 :")
e1 = set(*[str_1])
e2 = set(*[str_2])
set_1 = set()
set_2 = set()


a = list(e1.intersection(e2))
a.sort()
for i in a :
    print (i ,end="")

