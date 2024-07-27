# args = a parameter that will pack all arguments into a tuple
#       usefull so that a funtion can accept a varying amount of arguments

def add(*nums): #'*'is important to denote a args
    sum = 0
    #args are inchangable to change them we need to change it into list 
    nums = list(nums)
    nums[1]=11



    for i in nums:
       sum+=i
    return sum

print(add(5,6,7,3,2,1))