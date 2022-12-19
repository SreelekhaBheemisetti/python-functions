#  Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user
# and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
# 	23
# 	42 
# 	41 
# 	1
# Sample Output:
# 	-23 
# 	4200 
# 	-41 
# 	-1


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
            print(100*a[i])
        else:
            print(-a[i])
        i+=1
n=int(input("enter the n:"))
func(n)

