

def add(a,b):
    """두 개의 숫자를 더해서 그 값을 반환합니다. """  # doc string
    return a+b;

def subtract(a,b):
    """두 개의 숫자를 빼서 그 값을 반환합니다. """
    return a- b;

def multiply(a,b):
    """두 개의 숫자를 곱해서 그 값을 반환합니다."""
    return a*b;
def divide(a,b):
    """두 개의 숫자를 나눠서 그 값을 반환합니다. """
    return a/b;

add_result = add(5,3)
subtract_result = subtract(2,3)
multiply_result = multiply(a=5,b=3) # keyword argument
divide_result = divide(5,b=3)       # positional + keyword argument 
print(add_result, subtract_result, multiply_result, divide_result)

print(add.__doc__)              # 함수의 doc string을 출력
                                # help함수를 통해 특정 함수의 document를 검색할 수 있다. 