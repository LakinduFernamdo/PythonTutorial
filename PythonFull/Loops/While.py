x=[12,5,44,7,74,8,128]


count=0

while(count<10):
    
    count+=1
    print(count)
    

while True:
    print("count",count)
    count+=3
    if count >= 10:
        break ##Breake function 

for i in x:
    if(i%2==0):
        continue
    print(i)