# Draw a flowchart to take a list of N numbers from the user, 
# print True if the complete list consists of consecutive numbers with a difference of one. 
# Print False otherwise. 

# Sample Input:
# 1 2 3 4 5 6 7
# Sample Output:
# True
# Sample Input:
# 45 46 47 48 49 51 52
# Sample Output:
# False
# Sample Input:
# 4 5 6 7 8 9 10
# Sample Output:
# True

# Sample Input:
# -5 -6 -7 -8

# Sample Output:
# False
# Sample Input:
# -3 -2 -1 0 1
# Sample Output:
# True
def func(n):
    a=[]
    i=0
    while i<n:
        list=int(input("enter the list:"))
        a.append(list)
        i+=1
    i=0
    t=0
    f=0
    while i<len(a)-1:
        if a[i+1]-a[i]==1:
            t+=1
        else:
            f+=1
        i+=1
    if f==1:
        print("False")
    else:
        print("True")
n=int(input("enter the n:"))
func(n)
