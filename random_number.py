import random
x = random.randint(1,6) #prints a random no. in range of 1 to 6 
y= random.random()#this will give a random number between 0 and 1
print (x)
print (y)

list = ["rock", "paper" ,"scissors" ]
print(random.choice(list))


cards = [1,2,3,4,5,6,7,8,"j","k","q","a"]

random.shuffle(cards)
print(cards)
