#scope = The region that a variable is recognized a variable is only available from 
#        inside the region it is created a global and locality scoped versions of a 
#        variable can be created 

def display_name():
    name = "harsh"#it is a local scope variable and cannot be called outside the funtion
    print(name)

#print(name)    #it will show error cause name is a local scope variable 

display_name()

name1 = "wheelydos" #it is a global scope variable(available inside and outside a function)

print (name1)