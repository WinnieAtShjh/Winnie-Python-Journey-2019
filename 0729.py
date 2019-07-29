c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )

print( reversed(sorted( [ (v,k) for k,v in c.items() ] ) ) )
