import random as r
def pivot_select(left, right):
    v1 = left+r.randint(0, (right-left))
    v2 = left+r.randint(0, (right-left))
    v3 = left+r.randint(0, (right-left))

    #median of 3
    return max(min(v1,v2), min(max(v1,v2),v3))

def partition(lst, left, right):
    pivot_index = pivot_select(left, right)

    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]

    pivot = lst[right]

    i = left -1

    for j in range(left,right):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right] , lst[i+1]
    return i+1

def quick_sort(lst, left, right):
    if left < right:
        pi = partition(lst,left,right)

        quick_sort(lst, left, pi-1)
        quick_sort(lst,pi+1, right)
    return(lst)

print(quick_sort([3,1,2,4,5,6], 0,5))
