# Draw a flowchart to take a list of 7 numbers from the user, 
# print True if the complete list consists of consecutive numbers with 
# any constant difference between numbers. Print False otherwise.
 
# Sample Input:
# 2 4 6 8
# Sample Output:
# True
# Sample Input:
# -5 -6 -7 -8
# Sample Output:
# True
# Sample Input:
# 1 2 4 6
# Sample Output:
# False
# Sample Input:
# 3 6 9 12 16
# Sample Output:
# False

n=int(input("enter the n:"))
a=[]
i=0
while i<n:
    list=int(input("enter the list:"))
    a.append(list)
    i+=1
i=0
t=0
f=0
while i<len(a)-2:
    if a[i+1]-a[i]==a[i+2]-a[i+1]:
        t+=1
    else:
        f+=1
    i+=1
if f==1:
    print("false")
else:
    print("true")
    