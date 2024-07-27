# set = collection which is unordered , unindexed .noduplicate values

classs = {"knife","ramesh","suresh","lupper ganju","ana","fork","fork","fork","fork","fork"}#duplicate fork wont be repeated 
newset = {"helow","hemlo","hue hue hue ","knife"}


classs.add("helow")
classs.remove("knife")
newset.update(classs)#joins two sets
new_set2 = newset.union(classs) #joins the class too 


#classs.clear()

for x in classs:
    print(x) #the rsesultant irder is randomized 

for i in newset:
    print(i)

for j in new_set2:
    print (j)

print(classs.difference(newset))#prints what is not common in classs 
print(newset.difference(classs))

print(classs.intersection(newset))
