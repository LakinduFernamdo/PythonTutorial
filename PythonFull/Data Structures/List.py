#list
x=[12,58,18,44,73]
print(x)

print(x[0]) #get valou index 0

#change x[0]=100
x[0]=100
print(x)

y=x.append(90) #add element finally
z=x.insert(2,20) #(index,value)
a=x.remove(18)#element remove
b=x.pop(2)#index remove

#list can  be add
u=[1,2,3,4]
c=[1,8]
print(x+u+c)

#check elemnts are in the list
f=44 in x
g=44 not in c
print(f)
print(g)
