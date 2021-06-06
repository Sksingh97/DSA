a = [11, 2, 5, 1, 3, 6, 2, 10, 1, 10, 10,2 , 1, 2, 6, 11]

start = 0

n = len(a)
k = 11
ans = 200000
sumVal = 0

for end in range(n):
    sumVal += a[end]
    print("Considering array : ",str(a[start:end+1]), " With sum :",str(sumVal))
    while (sumVal>=k):
        if(sumVal == k):
            ans = min(ans, end-start+1)
            print("Updating answer to  : ",str(ans)," Because of : ",str(a[start:end+1]))
        sumVal -= a[start]
        start += 1
        print("Shrinking array to : ",str(a[start:end+1]))
    
        
print(ans)