d={
    "praneeth":176,
    "saman":167,
    "sajith":450,
    "siri":100
}

# First step : This gives all key values
for i in d:
    print(i)
#Second : get both key and value
for i in d:
    height=d[i]
    print(i,height)

#Third method :tupple
for i in d.items():
    type(i)

for i,j in d.items():
    print(i,j)

for i,x in enumerate(d.items()):  
    print(i,x)  