# Stack
# 후입선출 (Last In First Out)
# 즉, 나중에 입력된 값이 먼저 출력되는 구조
# 리스트를 활용

stacck = []

stacck.append(1)
stacck.append(2)
stacck.append(3)

stacck.pop()
stacck.pop()

print(stacck) # 1입력->2입력->3입력->3출력->2출력 