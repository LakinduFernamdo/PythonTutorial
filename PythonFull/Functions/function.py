def myFunction():
    print("Hi !")

myFunction()#call function

def getGrade(subject,marks):
    
    if(marks<=35):
        grade='fail'
        print(subject,grade)
    else:
        grade='pass'
        print(subject,grade)  

getGrade('maths',80)#call  function

#default argument

def getGrade(marks,subject="Unkown"): #Note: If Unknown use then  apply this rule
    
    if(marks<=35):
        grade='fail'
        print(subject,grade)
    else:
        grade='pass'
        print(subject,grade)  

getGrade(80)#call  function


