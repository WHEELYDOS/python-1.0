#logical operator(and,or,not)=used to check two or more conditoinal statement
a= int( input("enter a number"))
if not(a>=10 and a<=20):
    print("teens")
elif a==10 or a==25:
    print("hehe")
elif not(a == 22) :
    print("haha")
#not operator flips false from true and true to false