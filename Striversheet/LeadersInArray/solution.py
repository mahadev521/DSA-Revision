def leaders(arr):
    n = len(arr)
    i = n-1
    ret = [arr[i]]
    maxiElem = arr[i]
    while i > 0:
        i-=1
        if arr[i]>=maxiElem:
            ret.insert(0,arr[i])
        maxiElem=max(maxiElem,arr[i])

    return ret 

arr=[16,17,4,3,5,2]
print(leaders(arr))