def printTree(n):
  for i in range(0, n):
    space = n - i - 1
    stars = i
    while (space > 0):
      print("", end=" ")
      space -= 1
    while (stars >= 0):
      print("*", end=" ")
      stars -= 1
    print()

printTree(7)

