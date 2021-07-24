def vacuum_route(route):
    '''
    direction = [0,0]
    for i in range(len(route)):
        if route[i] == 'U':
            direction[0] = direction[0]+1
        elif route[i] == 'D':
            direction[0] = direction[0]-1
        elif route[i] == 'R':
            direction[1] = direction[1]+1
        elif route[i] == 'L':
            direction[1] = direction[1]-1
    print(direction)
    if direction == [0,0]:
        return True
    else: return False'''
    if route.count('L') != route.count('R') != route.count('U')!=route.count('D'):
        return False
    else: return True

print(vacuum_route('UDLRUDLR'))
