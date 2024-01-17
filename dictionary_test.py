my_dict = {
    'Name':'Tim',
    'Nationality':'African',
    'Age' : 87,
    'is_tall' : True,
    'Qualification':'College',
    'friends' : ['Peter', 'Paul', 'Precious']
}
x = my_dict['Name']
'''
print(my_dict)
print(my_dict['Name'])
print(my_dict['Nationality'])
print(my_dict['Qualification'])
print(my_dict['Age'])
print(my_dict['is_tall'])
print(my_dict['friends'])

print(x)
'''
#print(len(my_dict.keys()))

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key, value in my_dict.items():
    print(key ,' ', value)

    
