# Write a function named check_numbers which takes two numbers and then 
# print "both are even" if both numbers are even (divide by 2) 
# otherwise print "both numbers are not even".

def check_numbers(a,b):
    if a%2==0 and b%2==0:
        print("both are even")
        print(a/2,b/2)
    else:
        print("both numbers are not even")
check_numbers(66,44)