#  Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]


a=[12, 67, 98, 34]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(str(a[i])):
#         c=int(a[i][j]+a[i][j+1])
#         b.append(c)
#         j+=1
#     i+=1
# print(b)

b=[]
sum=0
i=0
while i<len(a):
    c=a[i]%10
    sum+=c
    a[i]=a[i]//10
    b.append(sum)
    i+=1
print(b)

    