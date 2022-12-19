# Your task is to create function is Divided By (or is_divide_by) 
# to check if an integer number is divisible by each out of two arguments.

# A few cases:
# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false
# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true
# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

# def func():
    

# a=int(input("enter the a:"))
# func()
def func(a,b,c):
    if (a//b)==c or -c:
        print("true")
    else:
        print("false")
a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))
func(a,b,c)
