x = [1,2,3,4]
out = []
for num in x:
	out.append(num**2)
print(out)

#above code can also be return in one line as
#in comprehensions method we write the condition first later give it to a for loop
#output is printed in [] because the command is given inside []
out = [num**2 for num in x]
print(out)
