#http://code.activestate.com/recipes/577225-union-find/

class unionfind_Tree:

    def make_set(x):
        x.parent = x
        x.rank = 0

    def find(x):
        if x.parent == x:
            return x
        else:
            return find(x.parent)

    def union(x,y):
        x_root = find(x)
        y_root = find(y) 
        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        elif x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root != y_root:
            y_root.parent = x_root
            x_root.rank = x_root.rank + 1

'''        
import itertools

class Node:
    def __init__ (self, label):
        self.label = label
    def __str__(self):
        return self.label
    
l = [Node(ch) for ch in "abcdefg"]      #list of seven objects with distinct labels
print ""
print "objects labels:\t\t\t", [str(i) for i in l]

[make_set(node) for node in l]       #starting with every object in its own set

sets =  [str(find(x)) for x in l]
print "set representatives:\t\t", sets
print "number of disjoint sets:\t", len([i for i in itertools.groupby(sets)])

assert( find(l[0]) != find(l[2]) )
union(l[0],l[2])        #joining first and third
assert( find(l[0]) == find(l[2]) )

assert( find(l[0]) != find(l[1]) )
assert( find(l[2]) != find(l[1]) )
union(l[0],l[1])        #joining first and second
assert( find(l[0]) == find(l[1]) )
assert( find(l[2]) == find(l[1]) )

union(l[-2],l[-1])        #joining last two sets
union(l[-3],l[-1])        #joining last two sets

sets = [str(find(x)) for x in l]
print "set representatives:\t\t", sets
print "number of disjoint sets:\t", len([i for i in itertools.groupby(sets)])

for o in l:
    del o.parent
'''
