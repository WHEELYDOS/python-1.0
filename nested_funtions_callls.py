#nested funtions calls = funtions calls inside other funtion calls
#                        intermost funtion calls are resolved first 
#                        returned value is used as argument for the next 
#                        outer funtion

num = input("enter a wholepositive number: ")
num= float(num)
num= abs(num)#makes the value positive 
num= round(num)
print(num)

#can be written as 

print(round(abs(float(input("enter a wholepositive number: ")))))