# str.format() = optional methord that gives users 
#              more control whendisplaying output

number = 1000 

print ("The number pi is {:.3f}".format(number))#will display the first 3 degit after the decimal if 2f then first 2 digit
print ("The number is {:,}".format(number))#will add comma afer every 1000,s palce
print ("The number is {:b}".format(number))#displays the number in binary 
print ("The number is {:o}".format(number))#displays the no in octa
print ("The number is {:X}".format(number)) #displays the number in hexa decimal
print ("The number is {:E}".format(number))#displas the number in scientific notation


animal = "cow"
item= "moon"

print("the " +animal + " jumped over the "+item)

print("the {} jumped over the {}".format("cow","moon")) #cow and moon can also be written as animal and item in this line 

print("the {1} jumped over the {0}".format("cow","moon"))#positional arguments 

print("the {first} jumped over the {second}".format(second="cow",first="moon"))#keyword arguments

text="the {} jumped over the {}"
print(text.format(animal,item))

name = " harsh "

print("hello , my name is {}".format(name) ) 
print("hello , my name is {name:10}".format(name) ) 
print("hello , my name is {:<10}".format(name) ) #text to the left 
print("hello , my name is {:>10}".format(name) ) #text to the right
print("hello , my name is {:^10}".format(name) ) #text in the middle