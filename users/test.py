import sys
import os
  
# adding Folder_2 to the system path
sys.path.insert(0, '~/Projects/django/charoit/')
  
# importing the add and odd_even 
# function
# from test import odd_even, add
import test
  
# calling odd_even function
test.odd_even(5)

# calling add function
print("Addition of two number is :", test.add(2, 2))