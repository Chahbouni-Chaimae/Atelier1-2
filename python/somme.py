def somme(n):
  int(input("entrez un nombre:"))
  if n == 0:
      return 0
  else:
    return n + somme(n - 1)