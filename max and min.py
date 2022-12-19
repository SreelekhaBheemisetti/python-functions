# Your task is to make two functions, max and min 
# (maximum and minimum in PHP and Python, maxi and mini in Julia) 
# that take a(n) array/vector of integers list as input and outputs, respectively, 
# the largest and lowest number in that array/vector.
# #Examples:-

# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5.
# minimun([42, 54, 65, 87, 0]) returns 0.



def func(n):
    a=[]
    i=0
    while i<n:
        list=int(input("enter the list:"))
        a.append(list)
        i+=1
    max=0
    min=0
    i=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        else:
            min=a[i]
        i+=1
    print("maximum number:",max)
    print("minimum number:",min)
n=int(input("enter the number:"))
func(n)