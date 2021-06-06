arr = [2,5,1,4,3,8,10]
st=[]
ans=[-1]*len(arr)
# print(arr,ans)
for i in range(len(arr)):
    if (len(st)==0 or arr[st[len(st)-1]]>arr[i]):
        st.append(i)
    else:
        while(len(st)>0 and arr[st[len(st)-1]]<arr[i]):
            pos = st.pop()
            ans[pos] = arr[i]
        st.append(i)
print(ans,st,arr)