def squress(var):return var**2

print(squress(3))


#instead of using a for loop, to square all the elements in the list
#we use map(func,var) and list it to see the output
seq=[1,2,3,4,5,6,7]
output=(map(squress,seq))
print(list(output))

#lambda expressions 
#is same like function but we will not define
#instead we will use it like

a = lambda num: num*3
print(a(9))

output1=(map(a,seq))
print(list(output1))

#filters are usually used to filter things from the list
print(list(filter(lambda num: num%2==0,seq)))
#basically the above lambda fuction is checking each element in the seq for num%2==0(for even)
#it will filtered by filter function and listed


x = 'hello i am nithin' 
print(x.split())
