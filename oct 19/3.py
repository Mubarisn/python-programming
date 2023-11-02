cl1=["Red","Green","Blue","Yellow"]
cl2=["Green","Orange","Blue"]
res=[color for color in cl1 if color not in cl2]
for color in res:
    print(color)
