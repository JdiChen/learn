a = [2,9,4,8,1,3,5,10,6,7]
for i in range(1,len(a)):
    t = a[i]
    j=i-1
    while j>=0:
        if a[j] > t:
            a[j+1]=a[j]
            a[j]=t
        j-=1
print(a)