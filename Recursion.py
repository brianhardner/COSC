def recurse(n, s):
  if n == 0:
    print(n, s)
  else:
   print(n, s)
   recurse(n-1, n+s)

recurse(3, 0)



