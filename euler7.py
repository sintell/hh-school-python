def primes(size, display=0):
  a = set(range(2,size))
  arr = range(size)
  res = []
  l = 0
  while 1:
    a = a - set(arr[::min(a)])
    yield min(a)

p = primes(1000000)

for x in xrange(1,10002):
  print p.next()