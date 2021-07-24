def binary_search(lst, value):
    init = 0
    final = len(lst)
    while init < final :
        dist = final-init
        half = (dist //2)+init
        

        if lst[half] ==value:
            return half
        
        if lst[half] > value:
            final = half
        
        else:
            init = half
        
    return False

lst = [1,2,3,4,5,6]

print(binary_search(lst, 5))


    
    
