#  Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. 
# print the last ‘N’ elements in reverse order.
# Sample Input:
# 2
# Sample Output:
# q
# b 
# Sample Input:
# 3
# Sample Output:
# q
# b 
# 5



def func(n):
    a=['a', 1, 2, 5, 'b', 'q']
    i=1
    while i<=n:
        print(a[-i])
        i+=1
n=int(input("enter the number:"))
func(n)