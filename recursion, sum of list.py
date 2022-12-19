
sum=0
def func(n):
    global sum
    if n>0:
        sum+=a[n-1]
        func(n-1)
    return sum
a=[12,45,67,34,22,98]
func(len(a))
print(sum)


