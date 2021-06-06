n=3

a = [0]*n
used = {}

def backtrack(pos, a, used):
    if(pos == n):
        print(a)
    else:
        for elem in range(1,n+1):
            if(elem not in used):
                a[pos] = elem
                used[elem] = True
                backtrack(pos+1, a, used)
                del used[elem]


backtrack(0, a, used)