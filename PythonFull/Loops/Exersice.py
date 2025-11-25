x=[12,23,567,123,88]

#find total of List
total=0

for i in x:
    total+=i
print("Total",total) 
print("Avg",total/len(x))   

#what is the biggest number? Using For Loop

max=x[0]
for i in x:
   
    if(max<i):
        max=i
print("max is :",max)        


#Using While loop
count=0
total=0
while(count<len(x)):
    total+=x[count]
    count+=1
print("sum: ",total)

#min and max using while loop

count=0
min=x[0]
max=x[0]
while(count<len(x)):
    item=x[count]
    if(max<item):
        max=item
    count+=1
print("max by while loop : ",max)        
