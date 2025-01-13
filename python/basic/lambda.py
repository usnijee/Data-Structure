'''
1. lambda
호출될 떄 값이 구해지는 하나의 표현식

정의 -> lambda[parameters]:expression -> 이름이 없는 인라인 함수
호출 -> (lambda[parameters]:expression)(argument) 
호출2 -> 변수에 저장 ,,     파이썬에서는 함수를 변수에 저장할 수 있다.!!
ex. twice = lambda x : x*2
    print(twice(10))

주의할 점 > lambda는 변수 없이 식 한 줄로 표현 가능(인라인)이므로 lambda 표현식 안에 새로운 변수를 만들 수 없다. 

2. 조건 표현식, inline if else
-> if else를 한 줄로 작성할 수 있는 방법
-> lambda에 사용하면 활용도가 아주 탁월
-> 반드시 else와 같이 사용
-> 중첩해서 사용이 가능하나 중첩이 많아지면 가독성이 떨어져 그냥 일반 if-else 문을 사용하는 것이 낫다

True일때 값 if 조건식 else False일때 값

ex. 
score = 90
'A' if 90<score<=100 else 'B' if 80<score<=90 else 'C'

3. map()과 lambda 같이 사용하기

 3-1. map() : 주어진 함수를 순회 가능한(iterable)객체의 각 요소에 적용하여 새로운 순회 가능한 객체를 생성하는 함수 
      map(function, iterable1,iterable2,...)

      ex. 
      a = [_ for _ in range(1,6)]
      b = [_ for _ in range(2,11,2)]
      print(list(map(lambda x,y:x*y, a, b)))   -> 순회가능한 객체인 a,b리스트를 map함수를 통해 lambda x,y:x*y 의 argument로 사용하여 반환 값으로 새로운 순회가능한 객체를 list()를 통해 리스트화한다

      map()에 lambda가 유용한 이유는 call back 함수의 역할을 하는 1회성 함수를 굳이 함수 선언을 하지 않고 lambda를 통해 사용할 수 있기 때문. 

4. filter()와 lambda 같이 사용하기 

 4-1. filter() :  주어진 순회 가능한(iterable) 객체에서 특정 조건을 만족하는 요소들만 선택하여 반환하는 파이썬의 내장 함수
      filter(function, iterable1,iterable2,...)

      ex. 
      a = [3,2,8,22,10,7,0,11,9,9]
      list(filter(lambda x: x%3 == 0 and 0 < x < 10, a)) -> filter의 경우 특정 조건을 만족하는 요소만 선택하여 반환하기에 특정 조건이 True, False로 판별이 가능한 함수에 적용됨 

'''

# lambda : 호출될 때 값이 구해지는 하나의 표현식
# 익명 함수 (anonymous function0)
some_func = lambda param: param**2  # parameter(인자) : expression(표현식) 구조
print(some_func(5))

# map(function, *iterable) 내장 함수
a = list(range(6))
b = [_var*2 for _var in a]          # list comprehension
map_result = map(lambda x,y:x+y, a, b)
print(list(map_result))