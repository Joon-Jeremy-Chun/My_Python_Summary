##Base
a = 0
b = 1
for a in range(5) :
  z = b + a
  print(z)

## start with 0,1 until 10000
x1 = 0
x2 = 1
x3 = x1 +x2
print(x1)
print(x2)
print(x3)
while True :
  x1 = x2
  x2 = x3
  x3 = x2 + x1
  if (x3 > 10000) :
    break
  else :
    print (x3)

# Define function    
## start with a1,a2 (both positive and negative) until n
def fibonacci_series(a1,a2,n) :


  x1 = a1
  x2 = a2
  x3 = x1 +x2
  print(x1)
  print(x2)
  print(x3)
  while True :
    x1 = x2
    x2 = x3
    x3 = x2 + x1
    if ( x3 > n or x3 < -n) :
      break
    else :
      print (x3)

# test
fibonacci_series(0, 1, 10000)

fibonacci_series(1, -2, 1000)

