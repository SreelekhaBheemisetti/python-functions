#  Write a flowchart which takes an input N. Then input N numbers. 
# Then for each of the N numbers, print “even” if the number is even or and “odd” if the number is odd.
# Sample input:
# 7
# 1
# 4
# 23
# 95
# 1203
# 403
# 84
# Sample output:
# Odd
# Even
# Odd
# Odd
# Odd
# Odd
# Even

def func(n):
    a=[]
    i=0
    while i<n:
        list=int(input("enter the list:"))
        a.append(list)
        i+=1
    i=0
    while i<len(a):
        if a[i]%2==0:
            print("Even")
        else:
            print("Odd")
        i+=1
n=int(input("enter the n:"))
func(n)

    
