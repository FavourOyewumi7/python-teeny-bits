def oned_candy(word):
    stack = []
    val = len(word)
    
    stack.append(word[0])
    for i in range(1, val):
        p = stack.pop()
        print('yo')
        if p == word[i]:
            print(i)
            #do something
            i+=1
        else:
            stack.append(p)
            stack.append(word[i])
            print(stack)
            
    res = ''.join(stack)
    return res

print(oned_candy("deeedbbcccbdaa"))
