def longestSubArraySumeqK(array,k):
    csum = 0 # storing sum at each index
    hm = {} # storing sum as key and index as value
    ret = 0 # returning value
    arr = []
    for i in range(len(array)):
        csum += array[i]
        if csum==k:
            ret = i+1
        
        if abs(k-csum) in hm:
            print(k-csum)
            if ret < i - hm[abs(k-csum)]:
                ret = i - hm[abs(k-csum)]
                arr = array[hm[abs(k-csum)]:i+1]
        
        if csum not in hm:
            hm[csum]=i
    print(hm)
    print(arr)
    return ret


print(longestSubArraySumeqK(array=[1,2,0,0,0,4,5,6,2,3,-2,-1,0,-1,2,2,5,6,2,3,1,3,4,5],k=3))