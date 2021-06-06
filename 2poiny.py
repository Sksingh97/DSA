a = [-30,-20,10,0,1,4,6,8,9]
left = 0
right = len(a)-1

while(left<right):
    if(a[left]*a[left]>a[right]*a[right]):
        print(a[left]*a[left])
        left += 1
    else:
        print(a[right]*a[right])
        right -= 1