s = input()

a = s.split("_")

b = a[0] + ''.join(x.capitalize() for x in a[1:])
print(b)