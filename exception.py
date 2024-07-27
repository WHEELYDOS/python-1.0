#exception = events detected during execution that interupts the flow of program

#deviding
try :
    numerator = int(input("enter a numerator : "))
    denominator = int(input("enter the denominator : "))
    result = numerator/denominator

except ZeroDivisionError as e :#if a numerator is divided by 0
    print(e)#prints and tells the user what exactly is wrong
    print("numerator cannot be devided by 0 ")

except ValueError as e:#if you enter leters and alphabet instead of values
    print(e)
    print("enter value only")

except Exception as e:#it is a general methord will give this statement for all unexpected values
    print(e)
    print("someting went wrong :-(") 

else:  # this else statement is added so that the program will only axecute the result after there are no excetions
    print(result)

finally: #whether or not we have an exception this block will always ezecute
    print("this will always execute")