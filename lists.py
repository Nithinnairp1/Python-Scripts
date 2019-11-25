my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])
print(my_list[-1])

n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1])
print(n_list[1][3])

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

odd = [1, 3, 5]
odd.append(7)
print(odd)

odd = [1, 3, 5]
print(odd + [9, 7, 5])

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)
print(my_list.pop(1))




# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list