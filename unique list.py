# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].
def list_name(list):
    a=[]
    i=0
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i+=1
    print(a)
list_name([1,2,3,3,3,3,4,5])