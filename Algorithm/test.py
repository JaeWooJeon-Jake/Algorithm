def f(idx):
    pass


n = int(input())
graph = []

for i in range(n):
    a = int(input())
    graph.append(a)

print(f(n-1))

# [10, 20, 15, 25, 10, 20]
# [False, False, False, False, False, False, False, False, False, ... ]
# 5 - 3 - 1 -0

# 0 2 4 - 35
# 1 2 4 - 45