
str_1 = str(input("enter sting 1 :"))
str_2 = str(input("enter sting 2 :"))
a=int()
for i in range(len(str_1)):
       print(str_1[i] , end="")
       print(str_2[i] , end="")
       a=i
while a<len(str_2)-1:
       print(" " +str_2[a+1], end="")
       a+=1
  