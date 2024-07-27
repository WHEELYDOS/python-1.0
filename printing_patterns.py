
columns= int(input("how many columns"))
#triangle
for i in range(1,columns+1):
    for k in range(columns-i):
        print(" " , end= "")

    for j in range(1,2*i):
        print("*", end="")
    print("\n")
    

    
#left triangle
for i in range(0,columns):
    for j in range(0,i):
        print(" * " , end="")
    print("\n")

#right triangle
for i in range(0,columns):
    for k in range(0,columns-i,):
        print("   ",end="")
    for j in range(0,i):
        print(" * " , end ="")
    print("\n")
    