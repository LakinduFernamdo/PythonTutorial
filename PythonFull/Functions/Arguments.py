#Packed Arguments
#Usually this type not working but this case * means get each arguments as one.This is packed arguments.
#Type:tupple
def getTotal(*marks):
    total=0
    for i in marks:
        total += i
    print(total)
getTotal(100,85,95) 

#All parameters are supported
#Dictionary type
def my_form(**params):
    if 'name' not in params:
        print('Error name required')
    print(params)

my_form(name="lakindu",age=23,city="panadura")
my_form(name="lakindu",age=23)

#Reverse
def myfunction(name,height,city):
    print(name,height,city)
args={
    'name':"lakindu",
    'height':176,
    'city':"panadura"
}    
myfunction(**args)