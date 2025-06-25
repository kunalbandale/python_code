# wap program to check the given number is odd or even
# different ways to do this code
# using %

#==========================

# using // floor division

#=========================
a = 13
if (a//2)*2 == a:
    print("Even Number")
else:
    print("Odd Number")

#==============================#

# using bitwise operator and
# a & 1 == 0

#==============================#

b = 12
if (b&1)==0:
    print("Even Number")
else:
    print("Odd Number")
