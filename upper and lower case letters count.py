# Write a Python function that accepts a string 
# calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def string(a):
    uc=0
    lc=0
    i=0
    while i<len(a):
        if a[i].isupper():
            uc+=1
        if a[i].islower():
            lc+=1
        i+=1
    print("No. of Uppercase characters :",uc)
    print("No. of Lower case Characters :",lc)
string('The quick Brow Fox')