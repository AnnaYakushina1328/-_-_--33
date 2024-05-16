# 3 вариант 
# 1 - 1/3 + 1/5 - 1/7

def fun1(n):
  return 1/(2*n -1)

def trace(func):
  def wrapper(*args, **kwargs):
    result=func(*args, **kwargs)
    print(f"Function {func,__name__} called with result: {result}")
    return result
return wrapper

@trace
def calculate_series(n_values):
  result_sum=0
  sign=1
  for n in n_values:
    result_sum += sign * fun1(n)
    sign *= -1
  return result_sum

n_values = (3, 5, 7)
result = 1 - calculate_series(n_values)
print(result)
