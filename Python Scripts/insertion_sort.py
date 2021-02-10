def insertion_sort(lst):
    for i in range(1,len(lst)):
        j = i-1
        key  = lst[i]

        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

print(insertion_sort([3,1,2,4,5]))
