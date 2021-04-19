# ====== PYTHON SYNTAX ====== #
# Create a variable and initialize it with a string

my_variable = "My first variable."

# Create a constant and initialize it with a string 

MY_CONSTAT = 'My first constant.'

# Create a "protected" variable and write a multi-line comment explaining what this variabke represents.

# This variable represents a magic number.
# It was created because we didn't have anything better to do at this point
# to showcase how to write multi-line comments.
_mine = 10

# Create a "private" variable

__my_private_variable = 'Can\'t touch this! Ta na na na'

# ====== MODULES & PACKAGES ====== #
# Print today's date using the sample_package
import packages.sample_package.sample_module as my_module

print(my_module.TODAY)

# import modules.sample_module.TODAY
# print(TODAY)

# ====== DATA TYPES & OPERATORS ====== #
# Create a list of integers from 0 to 5
L1 = [0, 1, 2, 3, 4, 5]
print(len(L1))

# Add an element to the list
L1.append('Test')
print(L1)

# Print different elements from the list
print(L1[3:2])
print(L1[0])
print(L1[-1])

# Modify a list element
L1[3] = "New"
print(L1)

# Concatenate two lists 
L2 = ["text", "c", 1, 2]
L1.extend(L2)
print(L1)

# Create a set 
s1 = set(L1)
print(s1)

s2 = (1, 2, 4, 5)
print(s2)

s3 = ([1,2], 3)
print(s3)

# Add an element to the set 
# s2.add(3)
# print(s2)

s3[0].append('3')
print(s3)

# Modify a set element
# s1[0] = 'New'
# print(s1)

s3[0][1] = 'New'
print(s3)

# Create a dictionary of (index, day) for the days of the week
d = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}

# Get keys, values from the dictionary
print(d.keys())
print(d.values())

# Print days starting with "t" from the dictionary
for value in d.values():
    if value[0] == "t":
        print(value)

# Replace one dict item
d[1] = 'Monday'
print(d)

# Add new item
d['test'] = 'test item'
print(d)
print(d.keys())
print(d.values())

# ====== CONTROL STRUCTURES ====== #
# IF / ELSE
# Print "It's bootcamp day!" if today is 'monday' or 'friday' and 'Other week day.' otherwise. 
today = 'monday'
if today == 'monday' or today == 'friday':
    print('It`s bootcamp day!')
else:
    print('Other week day.')

# IF / ELIF / ELSE
# Print "It's bootcamp day!" if today is 'monday' or 'friday';
# Print "Weekend!!!" if today is 'saturday' or 'sunday'
# Print 'Other week day.' otherwise. 
if today == 'monday' or today == 'friday':
    print('It`s bootcamp day!')
elif today == 'saturday' or today == 'sunday':
    print('Weekend!!!')
else:
    print('Other week day.')

# FOR
# Loop through a list with the days of the week and print each day.
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
for day in days:
    print(day)

# Loop through the numbers between 0 and 10 and print the even numbers.
for number in range(0, 10):
    if number % 2 == 0:
        print(number)
    
# WHILE
# Keep adding succesive numbers, starting from 0, until the sum is divisible by 19.
# Prin the sum at the end.
sum = 0
num = 1
while sum % 19 != 0:
    sum = sum + num
    num += 1
print(sum)