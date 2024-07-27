#keyword arguments = arguments preceded by an identifier when we pass them to a funtion
#                    the order of the arguments dose'nt matter ,unlike positional arguments 
#                    Pyhton knows the names of the arguments that our funtion recieve

def helo(first , middle , last ):
    print("hello"+" "+first + " " +middle+" "+last)

print(helo(last="sahu",middle="vardhan",first="harsh"))