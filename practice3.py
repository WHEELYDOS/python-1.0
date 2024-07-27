str_1 = input("enter sting 1 :")
str_2 = input("enter sting 2 :")
e1 = list(*[str_1])
e2 = list(*[str_2])

a= int()
while len(e1)<len(e2):
    e1.extend(" ")
while len(e2)<len(e1):
    e2.extend(" ")
for i in range(len(e1)):
    if e1[i]==" ":
        print(e2[i],end="")
    else:
        print(e1[i],end="")
    a=i




