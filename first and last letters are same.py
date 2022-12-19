# Write a Python program to count the number of strings where the string length is 2 or more 
# and the first and last characters are the same from a given list of strings.
# List=['abc', 'xyz', 'aba', '1221']
# result= 2.
            
# List=['abc', 'xyz', 'aba', '1221']
# c=0
# i=0
# while i<len(List):
#     if List[i][0]==List[i][-1]:
#         c+=1
#     i+=1
# print(c)

def list_name(List):
    c=0
    i=0
    while i<len(List):
        if List[i][0]==List[i][-1]:
            c+=1
        i+=1
    print("result:",c)
list_name(list(['abc', 'xyz', 'aba', '1221']))