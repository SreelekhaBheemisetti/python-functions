# def func():
#     a=[]
#     sum=0
#     num=int(input("enter the number:"))
#     i=0
#     while i<=num:
#         a.append(i)
#         sum=sum+a[i]
#         i+=1
#     return sum
# print(func())


# def func(n):
#     func(n)=n*(n-1)
#     func(n)
# n=int(input("enter the num:")) 
# print(n)  
# func(n)

# a=[[2,3,4],[5,8,2],[4,9,2]]
# b=[]
# i=0
# while i<len(a):
#     s1=0
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             s1=a[i][j]+s1
#         elif i==1 and (j==1 or j==2):
#             s1=a[i][j]+s1
#         elif i==2 and j==0:
#             s1=a[i][j] 
#         j+=1
#     b.append(s1)
#     i+=1
# print(b)


# a=[2,3,4,6]
# i=0
# while i<len(a)-1:
#     if a[i+1]-a[i]!=1:
#         print(a[i]+1)
#     i+=1