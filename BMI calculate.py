# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"



def function(weight,height):
    bmi=(weight/(height*height))*10000
    if bmi<=18.5:
        c= "Underweight"
        return c
    elif bmi<=25.0:
        c= "Normal"
        return c
    elif bmi<=30.0:
        c= "Normal"
        return c
    elif bmi>30:
        c= "Normal"
        return c
        
weight=int(input("enter the weight:"))
height=int(input("enter the height:"))
print(function(weight,height))