# 함수(function)
'''
함수(function)은 독립적으로 설계된 프로그램 코드의 집합

함수는 반복 사용되는 코드를 용도에 맞게 함수 바디에 모아두고 재사용 가능하도록 호출 가능하게 만든 것

코드의 중복을 줄일 수 있어서 유지보수에 좋다.
코드를 목적에 맞게 사용
중복에서 오는 실수 줄일 수 있음
재사용 가능

함수 -> positional parameter와 keyword parameter가 존재한다. 

parameter => 정의된 함수의 고정된 인자를 의미
arguments => 정의된 함수를 실제로 사용할 때 parameter 부분에 적용할 실제 값을 의미 


'''
# 함수 정의 1
def greeting(name, age):    # parameters : name, age
    print(f"{name} 씨 안녕하세요. 약 {age*365.25} 일 되었습니다.")

# 함수 정의 2                
    #=> 파라미터중에 default값이 있는경우 non-default인 파라미터가 먼저 나와야한다.
def greeting_1(age, name="default"):
    print(f"{name} 씨 안녕하세요. 약 {age*365.25} 일 되었습니다.")

# 함수 정의 3                
#  위치 전용 인자(positional only parameter)는 오직 위치 인수(positional arguments)만 값의 전달이 가능.
#  슬래시(/)를 인자 값으로 넣고 좌측 부분에 위치 전용 인자를 선언하면 된다. 
#  키워드 인수를 전달하면 error 발생 
def positional_only(posonly,/):
    print(posonly)

positional_only("값만 입력해야 합니다.")

# 함수 정의4
#  키워드 전용 인자(keyword only parameters)는 오직 키워드 인수만 값의 전달이 가능.
#  *를 인자 값으로 넣고 우측 부분에 키워드 전용 인자를 선언하면 된다.
def keyword_only(*,keyonly):
    print(keyonly)

keyword_only(keyonly="키워드로만 입력해야 합니다.")

# 함수 정의5
# 가변-위치 인자(var-positional parameters)
# 가변-위치 인자는 명시된 인자 외에 추가적으로 위치인수를 개수에 상관없이 유연하게 전달 받을 수 있다. 
# 즉, 개수의 상관없이 argument를 사용할 수 있다는 의미
# 가변 변수(파라미터)로 사용할 변수명 앞에 *를 하나 붙여 표기한다.

def var_positional(*args):
    print(type(args))   
 # 결과를 보면 tuple인 것을 알 수 있다. 즉, 개수에 상관없이 전달받은 arguments를 튜플로 묶어 전달하여 함수내에서 다른 연산에 적용된다.
    return sum([_ for _ in args])

print(var_positional(1,2,3,4,5))

# 함수 정의6
# 가변-키워드 인자(var-keyword parameters)
# 가변-키워드 인자는 가변-위치 인자와 동일하게 명시된 인자 외에 추가적인 키워드 인수를 개수 상관없이 전달 받을 수 있다.
# 변수명 앞에 **를 붙인다.

def var_keyword(**kargs):
    print(type(kargs))                # 결과를 보면 dictionary인 것을 알 수 있다. 
    return kargs
print(var_keyword(key="value",key2="value2"))
 
## 함수호출
# using positional parameter => 정의된 함수의 파라미터 순서를 고려해야함 
greeting("파이썬", 32)      # arguments : "파이썬", 32

# using keyword parameter    => 키워드 인자는 순서를 고려할 필요 없이 매개변수 명을 사용하여 인자를 대입하면 된다.
greeting(name="파이썬", age=32) # 
greeting(age=32, name="파이썬")

# using positional and keyword parameters => 정의된 함수의 파라미터 순서를 고려해야함,, 위치 인수가 키워드 인수보다 먼저 위치해야한다. 
greeting("파이썬", age=32)


# # 실습

# def add(a,b):
#     """두 개의 숫자를 더해서 그 값을 반환합니다. """
#     return a+b;

# def subtract(a,b):
#     """두 개의 숫자를 빼서 그 값을 반환합니다. """
#     return a- b;

# def multiply(a,b):
#     """두 개의 숫자를 곱해서 그 값을 반환합니다."""
#     return a*b;
# def divide(a,b):
#     """두 개의 숫자를 나눠서 그 값을 반환합니다. """
#     return a/b;

# add_result = add(5,3)
# subtract_result = subtract(2,3)
# multiply_result = multiply(a=5,b=3) # keyword argument
# divide_result = divide(5,b=3)       # positional + keyword argument 
# print(add_result, subtract_result, multiply_result, divide_result)

# help(add)