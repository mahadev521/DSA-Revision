def longestSubArraySumeqK(arr,k):
    lp=rp=0
    ret = 0 
    cursum = 0
    n=len(arr)
    while rp<n:
        cursum+=arr[rp]
        if cursum==k:
            ret = max(ret,rp-lp+1)
        elif cursum>k:
            cursum-=arr[lp]
            lp+=1
        rp+=1
    return ret


print(longestSubArraySumeqK(arr=[4,3,4,5,1,1,1,1,1,1,1,1,1,1,0,0,0,0,3,0,0,0,1,0,0,0,2,0,0,0],k=3))