test=str(input("enter a string"))
print("string is",str(test))
res= [char for char in test if char.isupper()]
print("the uppercase letters in string are:" +str(res))
