'''Pattern locks on a 9 digits keypad with just vert/horiz/diag moves and no digit reuse.'''

MOVE = {
    '1':'254', '3':'652', '9':'856', '7':'458',                 # Possible moves from corner
    '2':'36541', '6':'98523', '8':'74569', '4':'12587',         # Possible moves from middle
    '5':'12369874'                                              # Possible moves from center
    }

def code(path, many):                                           # Recursively research paths
    '''Count the codes starting with some path.'''
    #print(path)                                                # Un-comment for enumeration
    for move in MOVE[path[-1]]:                                 # Extend path with netx move
        if not move in path:                                    # Bypass already used digits
            many = code(path+move, many+1)                      # Count one path and recurse
    return many                                                 # Return the number of paths

print(code('1', 1)*4+code('2', 1)*4+code('5', 1), __doc__)      # 4 symmetries except center
#print(sum([code(base, 1) for base in MOVE.keys()]), __doc__)   # Alternate counting formula

