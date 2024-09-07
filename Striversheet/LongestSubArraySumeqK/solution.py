def longestSubArraySumeqK(array,k):
    csum = 0 # storing sum at each index
    hm = {} # storing sum as key and index as value
    ret = 0 # returning value
    arr = []
    for i in range(len(array)):
        csum += array[i]
        #if the sum == k it's the longest but you need current stats for future calculations so we are not using continue here
        if csum==k:
            ret = i+1
        
        # if pre sum already have sum that byproduct of removing required then the edge if presum must be excluded
        # cursum = k + presum => cursum-k = presum. reason why we are not adding +1 for the index subtraciton
        if abs(k-csum) in hm:
            if ret < i - hm[abs(k-csum)]:
                ret = i - hm[abs(k-csum)]
                arr = array[hm[abs(k-csum)]+1:i+1]

        # we want longest distance so we aren't updating the pre existing sum
        if csum not in hm:
            hm[csum]=i
    print(arr)
    return ret


print(longestSubArraySumeqK(array=[1,2,0,0,0,4,5,6,2,3,-2,-1,0,-1,2,2,5,6,2,3,1,3,4,5],k=3))