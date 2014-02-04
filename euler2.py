def even(x):
  return (x % 2 == 0)

def test():
  x=1
  y = 2
  while 1:
    if x > 4000000 or y > 4000000:
      raise StopIteration
    summ = x + y
    x = y
    y = summ
    if even(summ):
      yield summ

t = test()

res = 0
while 1:
  try:
    res += t.next()
  except Exception, e:
    break
  finally:
    print res
