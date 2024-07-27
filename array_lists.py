#liste = is used to store multiple item in a single variable 

food =["noodles","momo","chines","japaniese"]

print(type(food))
print(food)
print(food[0])



food[0]= "khana"
food.append("icecream")#ades the stoff to the list 
food.remove("momo")#removes the element
food.pop()#removes the last element 
food.insert(2,"food")#insert the elementa at the designated place
food.sort()#sorts the list alphabatically
food.clear()#clears the whole list 

for x in food :
    print (x)