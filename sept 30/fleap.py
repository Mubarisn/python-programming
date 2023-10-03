y=int(input("enter starting year"))
year=int(input("enter a future year"))
for i in range(y,year+1):         
    if(i%400==0) or (i%4==0 and i%100!=0):
        print(i,"leap year")
   
