# Your goal is to return multiplication table for number that is always an integer from 1 to 10.
# For example, a multiplication table (string) for number == 5 looks like below:- 
#           1 * 5 =5 
# 			2 * 5 =10
# 			3 * 5 =15
# 			.
# 			.
# 			10 * 5=50.


def multi(n):
    i=1
    while i<=n:
        print(m,"*",i,"=",m*i)
        i+=1
n=int(input("enter the n:"))
m=int(input("enter the m:"))
multi(n)