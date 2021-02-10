def mergeSort(a,b):
    lena = len(a)
    lenb = len(b)
    lenab = len(a) + len(b)
    
    merge_lenab = [None] * lenab

    index_a = 0
    index_b = 0
    index_ab = 0

    while index_ab < lenab:
        is_exhausted_a = index_a >= lena
        is_exhausted_b = index_b >= lenb
        #if a is not exhausted and b is exhausted or a[index_a] is smaller
        #than b[index_b]

        if(not is_exhausted_a and (is_exhausted_b or (a[index_a] < b[index_b]))):
            merge_lenab[index_ab] = a[index_a]

            index_a += 1
        else:
        #if b is not exhausted and a is exhausted or b[index_b] is smaller than
        # a[index_a]
            merge_lenab[index_ab] = b[index_b]

            index_b += 1

            
        index_ab += 1
    print(merge_lenab)
        
    return merge_lenab




mergeSort([1,3,5,6], [2,4,7,8])
                                      
