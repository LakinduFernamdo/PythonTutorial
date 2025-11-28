## What is a List of Lists?

##In Python, a list of lists is essentially a 2D structure (like a matrix or table). 
# Each element of the outer list is itself another list.

#Python doesn’t have generics in the same way, 
# but you can achieve the same with nested lists:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print(col,end="")


