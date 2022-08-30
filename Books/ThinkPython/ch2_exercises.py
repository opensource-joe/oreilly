# Answer files for all chapters - https://www.greenteapress.com/thinkpython2/code/

# https://learning.oreilly.com/library/view/think-python-2nd/9781491939406/ch02.html#:-:text=Exercises

# Exercise 2-1.
# Repeating my advice from the previous chapter, whenever you learn a new feature, you should try it out in interactive mode and make errors on purpose to see what goes wrong.

# We’ve seen that n = 42 is legal. What about 42 = n?

# Results in SyntaxError: cannot assign to literal

# How about x = y = 1?

# Works and x and y both print out 1

# In some languages every statement ends with a semicolon, ;. What happens if you put a semicolon at the end of a Python statement?

# A semi-colon in Python denotes separation, rather than termination. It allows you to write multiple statements on the same line. 

# What if you put a period at the end of a statement?

# Results in SyntaxError: invalid syntax

# In math notation you can multiply x and y like this: xy. What happens if you try that in Python?

# Results in Traceback error: 'xy' is not defined

# Exercise 2-2.
# Practice using the Python interpreter as a calculator:

# The volume of a sphere with radius r is . What is the volume of a sphere with radius 5?

# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

# book = 24.95
# discount = .4
# ship_cost_one = 3
# ship_cost_more = .75
# wholesale_cost = ((24.95 * .4) + 3) + .75 * 59
# print(wholesale_cost)
# 57.230000000000004

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I get home for breakfast?