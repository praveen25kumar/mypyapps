------------list---------
--------remove_duplicate----------
-->string
def dul(s):
  c=[]
  for i in s:
    if i not in c:
      c.append(i)
  return c
  

