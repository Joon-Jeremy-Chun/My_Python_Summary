# recursive function practice
def recureive_function():
    print("clls re_f")
    recureive_function()
    
#recureive_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object

#2nd practice

def recursive_f2(n):
    if n == 100 :
        return
    else:
        print(n, ' funcion will calls:', n+1, ' funtion')
        recursive_f2(n+1)
        print(n, ' funcion close')
    
#recursive_f2(1)
    

# Factorial function by loop

def factorial_loop(n) :
    if n == 0:
        print(1)
    else:
        a=1
        for i in range(1,n+1):
            a = a*i
            
        print(a)

#factorial_loop(10)






# Factorial by recureive function

def factorial_recursive(n) :
    
    if n <= 1:
        print( 1)
    
    else:
    
        b = n*factorial_recursive(n-1)
        print(b)
        
        
#factorial_recursive(5)

def factorial_recursive1(n) :
    
    if n <= 1:
        return 1
    return n * factorial_recursive1(n - 1)
        
        
factorial_recursive(5)
