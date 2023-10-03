sum=0
print("enter the limit:")
lim=int(input())
print("enter"+str(lim)+"numbers:")
for i in range(lim):
      lim=int(input())
      sum=sum+lim
      avg=sum/lim

print("sum of entered numbers:",sum)
print("average of entered numbers is:",avg)
