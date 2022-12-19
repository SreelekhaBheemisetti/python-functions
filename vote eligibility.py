#  Write a function to tell user if he/she is able to vote or not.
#  ( Consider minimum age of voting to be 18. )

def vote(age):
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
age=int(input("enter the age:"))
vote(age)