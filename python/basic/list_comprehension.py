# list comprehension : list를 생성하는 방법 중 하나

list_var = [i for i in range(1,10)]
print(list_var)

list_var2 = [i for i in range(10) if i % 2 == 0]
print(list_var2)

# 출력문

# seq라는 keyword argument가 기본값(default)으로 " " 공백을 가지고 있다. seq는 구분 역할 
print(1,1.1,[1,"가",1.3], sep=" ")
print(1,1.1,[1,"가",1.3], sep="/")

# 출력되는 문자열 맨 뒤에 개행 문자(\n)를 기본 값(default)으로 사용하는데 end=문자열을 맨 뒤에 입력하여 변경할 수 있다. end는 마지막에 문자를 추가하여 변경하는 역할 
'''print("줄이 바뀌지 않습니다.", end="")
print("그 이유는 end=\"\\n\"과 같이 기본 설정된 값을 빈 스트링으로 변경했기 때문입니다.")
print("sep","end는 맨 뒤에 써야하며 둘 간 순서는 상관없습니다.", sep=", ", end="")'''

print("출력할 때 쓰는 print() 내장 함수는", end="\n")
print("기본적으로 개행 문자를 마지막 문자로 사용을 합니다.")

print("출력할 때 쓰는 print() 내장 함수는", end=" 마지막에 추가되는 문자를 다른 값으로 변경했습니다.")
print("기본적으로 개행 문자를 마지막 문자로 사용을 합니다.")