#   Kids drink toddy.
# 	Teens drink coke.
# 	Young adults drink beer.
# 	Adults drink whisky.
# 	Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".

def age(n):
    if n>0 and n<14:
        a="drink toddy"
        return a
    elif n>=14 and n<18:
        a="drinks coke"
        return a
    elif n>=18 and n<21:
        a="drinks beer"
        return a
    elif n>=21 and n<100:
        a="drinks whisky"
        return a
n=int(input("enter the number:"))
print(age(n))

    

    