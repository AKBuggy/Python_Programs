from moduleTesting import *

# Calling functions

# 1> Taking user from input
user_lst = take_user_input()
print("Your List: ", user_lst)

# 2> Even and Odd counter
even, odd = count(user_lst)
print("Even: {} and odd: {}".format(even, odd))
