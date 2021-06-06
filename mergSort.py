a = [1,2,3,7,8]
b = [2,3,4,5,9]
c = []

i=0
j=0

n=len(a)
m=len(b)

while(i<n or j<m):
    if(a[i]<=b[j]):
        c.append(a[i])
        i = i+1
    else:
        c.append(b[j])
        j = j+1


print(c)