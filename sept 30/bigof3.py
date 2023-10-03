x=int(input("enter number1:"))
y=int(input("enter number2:"))
z=int(input("enter number3:"))
if(x==y)and (y==z):
    print("all numbers are equal")
elif(x>y) and (x>z):
      big=x

elif(y>x) and (y>z):
      big=y9

else:
    big=z
print("biggest number is",big)
