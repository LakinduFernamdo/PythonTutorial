## Do not Duplicate data values
#Not Index based this is use map data structure
#if we add duplicate then only print ones time
#case sensitive

x={"Hellow","lakindu","machan",1,5}
y={"test",2,1,3}
print(x)
x.add("lakindu")
x.remove(5)
a=x.union(y)
b=y.union(x)
c=x-y
print(c)

print(1 in x)