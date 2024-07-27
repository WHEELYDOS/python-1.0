#looop control statements 

#break  = used to terminate loops entirely 
#continue= skips the next interation 
#pass = does nothing ,acts as a place holder

while True:
    name = input("enter yout name ")
    if name != "":
        break

phone_number = "8858-7766-91"
for i in phone_number:
    if i=="-":
        continue
   
    print(i, end="")  

for i in range(1,11):
    if i== 7:
        pass
    else :
        print(" ",i,end="")