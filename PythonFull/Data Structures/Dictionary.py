x = {"100": "colombo", "12500": "kaluthara"}  # Initial dictionary
x["1200"] = "moratuwa"  # Add new key-value pair
print(x)

#Return view objects
print(x.keys())    # dict_keys(['100', '12500', '1200'])
print(x.values())  # dict_values(['colombo', 'kaluthara', 'moratuwa'])

#Return as list
print(list(x.keys()))
print(list(x.values()))

#Nested dictionary :storing another dictionary as a value — this is a nested dictionary. You can access inner values like:
x['cities'] = {1: '789456', 2: '123456'}#add new key 'cities' and values {1: '789456', 2: '123456'}
#x['cities']=inner dictionary

"""
x = {
    'cities': {
        1: '789456',
        2: '123456'
    }
}
"""

y = x["cities"]
print(y)
print(x['cities'][1])  # Output: 789456






#Dictionaries are not index based
print(x.get("9999", "Not found"))  # Output: Not found

#Pass by Reference vs Value
a = {
    "name": ["amal", "nimal", "kamal"],  # list (mutable)
    "age": [1, 2, 3],                    # list (mutable)
    "c": 16                              # int (immutable)
}
b=a["name"]
b.append("mahinda mahattaya")
print(b)
##b and a["name"] point into same list in memory
c = a["c"]
c += 1
print(a["c"])  # Still 16

##c is immutable and not change even +1


