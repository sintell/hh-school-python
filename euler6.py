def g():
  for x in xrange(1,101):
    yield x*x
    pass

gen = g()
print
print pow(sum(xrange(1,101)),2) - (sum(gen))
