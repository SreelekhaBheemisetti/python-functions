# I would like to be able to pass an array with two elements to my swapValues function to swap the values.
# However it appears that the values aren't changing.
# Can you figure out what's wrong here?


def func(a,b):
    a,b=b,a
    return a,b
print(func(3,2))
# a=int(input("enter the a:"))
# b=int(input("enter the b:"))
# while a<=b:
#      j=1
#      count=0
#      while j<=a:
#           if a%j==0:
#                count+=1
#           j+=1
#      if count==2:
#           print(a)
#      a+=1
     
# i=1
# user=int(input("enter the number:"))
# while i<=user:
#      j=1
#      count=0
#      while j<=i:
#           if i%j==0:
#                count=count+1
#           j=j+1
#      if count==2:
#           print(i)
#      i+=1


# i=1
# count=0
# user=int(input("enter the number:"))
# while i<=user:
#     if user%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime number")
# else:
#     print("composite number")
