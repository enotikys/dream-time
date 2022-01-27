def input_f():
 #Макс

 
  
  
  
  
  
 def x2():
  return collatz(n // 2)
  
  
def x3_1():
 return collatz(n*3+1)

  
  
def collatz(n):
    result = [n]
    if n == 1
        pass 
    elif n % 2 == 0
        result.extend(x2(n))
    else:
        result.extend(x3_1(n))
    return result
