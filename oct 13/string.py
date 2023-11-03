n = str(input("Enter the string"))
if len(n)<2:
    print("Length is short")
else:
    fchar=n[0]
nstring = fchar+n[1:].replace(fchar, "$")
print("new string:",nstring)
