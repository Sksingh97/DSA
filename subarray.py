arr = [10, 15, 6, 18, 22, 4, 19]

b = [0].(len(arr)+1)

n = len(arr)
target = 44

ht = {}

for(i=0;i<n;i++):
    b[i+1] = arr[i]+b[i]

for j in range(len(b)):
    if((b[j]-target) in ht):
        print("Subarray index : ",j,ht[b[j]-target])
        break
    else:
        ht[b[j]]=j
