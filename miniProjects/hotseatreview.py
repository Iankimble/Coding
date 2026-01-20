fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  print("this is a " + x)
  if x == "bananna":
    fruits.remove(x)
print(fruits)