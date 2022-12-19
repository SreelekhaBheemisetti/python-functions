# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".

def string_name(string):
    rev=""
    i=-1
    while i>=-len(string):
        rev=rev+string[i]
        i-=1
    print(rev)
string_name("1234abcd")
    