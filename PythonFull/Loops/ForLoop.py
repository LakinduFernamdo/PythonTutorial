myList=[12,45,6,9,78,10]
index=0

#The for loop has Index loop and enhanced loop both.
#for i in x              means enhanced loop   i means value
#for i in range(len(x))  means enhanced loop   i means index

for i in myList:
    print(index,i)
    index+=1

for i in enumerate(myList):#enumerate() is a built-in Python function that lets you loop with both index AND value at the same time.
    print(type(myList),i)

r=range(0,10)
for item in r:
    print(item)


