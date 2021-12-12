#Longest_bitonic_subsequence
def long_bitonic_susequence(arr):
     
    for i in range(l-1):
        for j in range(i+1,l):
            if arr[i]<arr[j]:
               # for the forward check of longest subsequence
                forward[j] = max(forward[i]+1, forward[j])
            if arr[l-i-1]<arr[l-j-1]:
               # for the backward check of longest subsequence
                backward[l-j-1] = max(backward[l-i-1]+1, backward[l-j-1])
    res = 0
    for i in range(l):
        res = max(forward[i]+backward[i]-1,res)
    return res
                
    
    
    
arr = list(map(int,input().split()))
l = len(arr)
forward = [1]*l
backward = [1]*l
print(long_bitonic_susequence(arr))
