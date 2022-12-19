def func(a):
    b=[]
    i=0
    while i<len(a):
        c=a[i]**2
        d=c%10
        b.append(d)
        i+=1
    print(b)
func([1,2,3,4,5,6])