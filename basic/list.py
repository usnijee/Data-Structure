

string_list = ["a", "b", "c", "d"]
number_list = [1, 2, 3, 4]

# 인덱싱
print(string_list[0]) # a
print(number_list[2]) # 3

# 슬라이싱
print(string_list[:2]) # ['a', 'b']
print(number_list[1:3]) # [2, 3]

# 더하기
print(string_list + number_list) # ['a', 'b', 'c', 'd', 1, 2, 3, 4]

# 반복하기
print(number_list * 2) # [1, 2, 3, 4, 1, 2, 3, 4]

# 길이 구하기
print(len(number_list)) # 4

# 값 수정하기
number_list[1] = 5
print(number_list) # [1, 5, 3, 4]

# 요소 삭제하기
del number_list[1]
print(number_list) # [1, 3, 4]

# 요소 추가
number_list.append(0)
print(number_list) # [1, 3, 4, 0]

# 리스트 정렬
number_list.sort()
print(number_list) # [0, 1, 3, 4]

# 리스트 뒤집기
number_list.reverse()
print(number_list) # [4, 3, 1, 0]

# 리스트 인덱스 반환
# index(x) x값이 있으면 x의 인덱스값 반환
# 없으면 에러가 발생합니다.
print(number_list.index(3)) # 1

# 리스트 요소삽입
# insert(a, b) a번째에 b를 넣어라
number_list.insert(0, 10)
print(number_list) # [10, 4, 3, 1, 0]

# 리스트 요소제거
# remove(x) 첫번째로 나오는 x를 제거해라
number_list.remove(10)
print(number_list) # [4, 3, 1, 0]

# 리스트 요소 꺼내기
# pop() 제일 마지막 요소를 꺼냄
print(number_list.pop()) # 0
print(number_list) # [4, 3, 1]

# 리스트 요소 개수 세기
# count(x) 리스트 안에 x가 몇개인가
print(number_list.count(3)) # 1

# 리스트 확장
# extend(list)
number_list.extend([5,6,7])
print(number_list) # [4, 3, 1, 5, 6, 7]