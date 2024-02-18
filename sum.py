# Sum all the numbers of a given array ( cq. list ), except the
# highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at 
#each edge, even if there are more than one with the same value.

#my solution
def sum_array(arr):
    if arr is None or len(arr) == 1 or len(arr)==0: 
        return 0
    else:
        arr.sort()
        return sum(arr) - arr[0] - arr[-1] 