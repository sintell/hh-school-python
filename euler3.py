def primes(size, display=0):
  a = set(range(2,size))
  arr = range(size)
  while min(a)  < 600851475143 and len(a):
    if 600851475143 % min(a) == 0:
      res = min(a)
    a = a - set(arr[::min(a)])
  return res


print(primes(1000000))