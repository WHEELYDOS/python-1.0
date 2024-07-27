#funtion = a block of code which is executed only when it is called.

def hello(x):
    print ("hellow "+ x)
    print(type(x))


def helo(x,y):
    print("helow " + x + " "  + y)


first_name = input("what is your first name ")
last_name = input("what is your middle name ")
hello(first_name)#to call a funtion
print (int(first_name) +9)
helo(first_name,last_name)