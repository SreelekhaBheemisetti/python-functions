# Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3


def func(list1):
    pos=0
    neg=0
    i=0
    while i<len(list1):
        if list1[i]>=0:
            pos+=1
        else:
            neg+=1
        i+=1
    print("positives=",pos)
    print("negatives=",neg)
list1 = [2, -7, 5, -64, -14]
func(list1)