def reverse_string(string):
    '''base solution'''
    #return string[::-1]
    i = 0
    j = len(string)-1
    
    listing = []
    for i in range(j,-1,-1):
        listing.append(string[i])
    print(listing)
    new_string = ''.join(listing)
    return new_string

print(reverse_string('This is a boy'))

#first solution is O(n) time with O(1) space
# second solution is O(n) with O(n) space
