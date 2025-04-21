# bounce.py
#
# Exercise 1.5

#1.5: The Bouncing Ball
#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.

height = 100
index  = 0
count  = 10

print("index:height")
for i in range(count):
  height *= (3/5)
  rounded_height = round(height, 2)
  print(f"{i}:{rounded_height}")


