# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_data = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_data['name'])

# Output: 26
print(my_data.get('age'))

my_data['age'] = 27
print(my_data.get('age'))

my_data['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_data)


squares = {1:1, 2:4, 3:9, 4:16, 5:25}

#removes 4:16
print(squares.pop(4))

# delete a particular item
del squares[5]

# remove all items
squares.clear()




# clear()	Remove all items form the dictionary.
# copy()	Return a shallow copy of the dictionary.
# fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])	Return the value of key. If key doesnot exit, return d (defaults to None).
# items()	Return a new view of the dictionary's items (key, value).
# keys()	Return a new view of the dictionary's keys.
# pop(key[,d])	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
# popitem()	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
# setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
# update([other])	Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()	Return a new view of the dictionary's values