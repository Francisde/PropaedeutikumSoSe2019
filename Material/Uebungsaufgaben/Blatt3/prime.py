def prime(maximum):
  primes=[2]
  isdividable=False
  for count in range(2 , maximum+1):
    isdividable=False
    for innerCount in range(2,count):
      if(count % innerCount==0):
        isdividable=True
        break

    if(isdividable == False):
      primes.append(count)
  return primes

print(prime(100))
