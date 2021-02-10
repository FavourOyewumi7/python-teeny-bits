def selection_sort(lst):

    for i in range(len(lst)):
        min_index= i

        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        lst[i],lst[min_index]  =lst[min_index], lst[i]

lst = [3, 2, 1, 5, 4]

selection_sort(lst)

print(lst)

        
