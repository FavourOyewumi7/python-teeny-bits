def merge_sort(lst):
    half = len(lst)//2
    left = lst[:half]
    right = lst[half:]

    merge_sort(left)
    merge_sort(right)

    new_array = [None] *len(lst)
    index_left = 0
    index_right = 0
    index_all = 0
    
    

    while index_all < len(lst):
        truety_left = index_left > len(left)
        truety_right = index_right > len(right)
        if (not truety_left and (truety_right or
                                 left[index_left] < right[truety_right])):
            new_array[index_all] = left[index_left]
            index_left += 1
        else:
            new_array[index_all] = right[index_right]
            index_right += 1

        index_all += 1
        
            
        
    
