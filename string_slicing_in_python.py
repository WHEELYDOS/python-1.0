#slicing=creat a substing by extracting elements from a sting
#       indexing[]or slicing()
#       [start:stop:step]

name = "wheelydos harsh"
first_name = name[:10]#will automatically asume starting from 0
print (first_name)
last_name= name[10:]#will automatically assume the ending 
print(last_name)
funny_name= name[::2]#skips every two steps  
print(funny_name)
reversed_name=name[::-1]
print(reversed_name)

website1 = "https://www.google.com"
website2="https://www.youtube.com"
slicing = slice(12,-4)#last digit  is considered as -1
print(website1[slicing])
print(website2[slicing])