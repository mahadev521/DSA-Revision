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
        if csum-k in hm:
            if ret < i - hm[csum-k]:
                print(csum-k,i)
                ret = i - hm[csum-k]
                arr = array[hm[csum-k]+1:i+1]

        # we want longest distance so we aren't updating the pre existing sum
        if csum not in hm:
            hm[csum]=i
    print(arr)
    return ret


print(longestSubArraySumeqK(array=[8,-9,10,-2,-10,6,18,17],k=17))