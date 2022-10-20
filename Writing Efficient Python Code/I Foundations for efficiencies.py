"""DEFINING EFFICIENT
---------------------
    - Fast runtime(- time)
    - Minimal resource consumption(- memory)
\\"""
  # Non pythonic
  doubled_numbers= []
  for i in range(len(numbers)):
     doubled_numbers.append(numbers[i]*2)
  # Pythonic
  doubled_numbers= [x * 2 for x in numbers]
#``````````````````````````````````````````````````````````````````````````````````````````````````
"""
Pop quiz: what is efficient
In the context of this course, what is meant by efficient Python code?

    # Code that executes quickly for the task at hand, minimizes the memory footprint and follows Python's coding style principles."""
#``````````````````````````````````````````````````````````````````````````````````````````````````
# A taste of things to come 1== Non-pythonic

 names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
    
# Print the list w/ Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
# A taste of things to come 2== more Pythonic way

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
# A taste of things to come 3== The Pythoniest way

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
# What is the 7th idiom of the Zen of Python?
import this
#The Zen of Python, by Tim Peters
        # Readability counts.
"""*********************************************************************************************************************
Built-in types
===============
    >>>>>> list, >>>>>> tuple, >>>>>> set, >>>>>> dict
    
Built-in functions
=================    
    >>>>>> print(), >>>>>> len(), >>>>>> range(), >>>>>> enumerate(), >>>>>> round(), >>>>>> map(), >>>>>> zip()
    
    map() === (returnedValue, toWhat)--- in iterables
    
Built-in modules
================= 
    >>>>>> os, >>>>>> sys, >>>>>> itertools, >>>>>> collections, >>>>>> math   
******************************************************************************************************************"""

## Built-in practice: range()
# Create a range object that goes from 0 to 5
nums = range(0,6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)] # start , end(exclusive), step
print(nums_list2)

#$$$ unpacking a range object(*) same as using-----nums_list = list(nums) $$$
# <class 'range'>
# [0, 1, 2, 3, 4]
# [1, 3, 5, 7, 9, 11]
