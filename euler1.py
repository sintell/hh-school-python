summ = 0
for x in xrange(1,1000):
  if x%3 == 0 or x%5 == 0:
    summ += x
  pass

print summ