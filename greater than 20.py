# You have to define a function named isGreaterThan20 
# in which you have to pass two parameters to the function and 
# the first parameter by default should be 20.And then output should be True 
# if both values are greater than 20 and False if any one is equal to 20 or less than 20.

def isGreater_Than20(a,b=20):
    if a>20 and b>20:
        print("True")
    else:
        print("False")
isGreater_Than20(10)
    
    