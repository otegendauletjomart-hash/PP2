i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#My example
i = 0
while i < 5:
  print("Count:", i)
  i += 1

i = 1
while i <= 10:
  print(i)
  if i == 5:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i % 2 == 0:
    continue
  print("Odd number:", i)

i = 1
while i <= 3:
  print("i is", i)
  i += 1
else:
  print("Loop finished!")

i = 1
while i <= 5:
  print(i)
  if i == 6:
    break
  i += 1
else:
  print("This will run")
