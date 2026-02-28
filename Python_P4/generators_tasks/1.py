def gen1(n):
  for i in range(n+1):
    yield i * i

s = int(input())


for v in gen1(s):
  print(v)