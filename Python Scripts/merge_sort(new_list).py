import sys
print(sys.getrecursionlimit())
def merge_sort(lst):
    if len(lst) > 1:
        half = len(lst)//2
        left = lst[:half]
        right = lst[half:]

        merge_sort(left)
        merge_sort(right)

        new_array = [None] *len(lst)
        index_left = 0
        index_right = 0
        index_all = 0
    
    

        while index_left<len(left) and index_right<len(right):
            if left[index_left] < right[index_right]:
                lst[index_all] = left[index_left]
                index_left += 1
            else:
                lst[index_all] = right[index_right]
                index_right += 1
            index_all += 1
        while index_left <len(left):
            lst[index_all] = left[index_left]
            index_left += 1
            index_all += 1
        while index_right <len(right):
            lst[index_all] = right[index_right]
            index_right += 1
            index_all += 1
        return lst
    


print(merge_sort([3,1,2,4,5,8]))
        
            
        
    
