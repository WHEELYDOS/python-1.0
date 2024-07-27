# index operator [] = gives access to a sequence's element (str,list ,tuples)
name = "hArsH vardhan Sahu ^"

if name[0]:
    name = name.capitalize()#makes the first character in uper case and all the other to lower case 
print(name)


if (name.islower()):
    print("true")

first_name = name[0:5]
print (first_name) 


last_name = name[14:]
print(last_name)

last_character = name[-1::]
print(last_character)