#**kwargs = parameter that will pack all arguments into a dicitonary useful so that
#           a funtion can accept a varying amount of keyword arguments

def name_hello(**name):
    print("hello "+ name['first']+ " "+ name['middle']+ " " + name['last'] )
    #or 
    print ("hello",end=" ")
    for key, values in name.items(): #keys and values can be changed for enyother things but their working will be same 
        print(values,end= " ") # data like harsh vardhan sahu are valuse 
        print (key,end=" ")  #data like first middle and last are key 

print(name_hello(first="harsh", last ="sahu",middle="Vardhan"))