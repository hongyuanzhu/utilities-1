# Breadth First Search tree traversal
def BFS(t):
    Q = deque()
    t.visited = True
    Q.appendleft(t)
    while Q:
        t = Q.pop()
        # perform visit of t
        print (t.get_data())
        for c in t.get_children():
            if not c.visited:
                c.visited = True
                Q.appendleft(c)

# Depth First Search tree traversal
def DFS(t):
    if not t.visited:
        print (t.get_data())
        t.visited = False
        for c in t.get_children():
            DFS(c)
