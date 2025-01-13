# <class 'str'>
string = "Hi"
print(type(string))

# 문자열 안에서 따옴표, 쌍따옴표 사용하기
print("문자열은 문자, 단어들의 '집합'입니다.")  # ''내부에서는 쌍따옴표 "" 사용
print('문자열은 문자, 단어들의 "집합"입니다.')  # ""내부에서는 따옴표 '' 사용

# 이스케이프 문자 \\

# 1. \n : 줄바꿈
print("첫 번째 줄\n두 번째 줄")

# 2. \t : 수평탭
print("이것은\t탭입니다.")

# 3. \ : 백슬래시
print("이것은 백슬래시(\\)입니다.")

# 4. '또는": 작은따옴표 또는 큰 따옴표 자체를 문자열 안에서 사용할 때는 백슬래쉬를 이용
print('작은따옴표(\')와 큰따옴표(")는 문자열을 감싸는 데 사용됩니다.')
print("작은따옴표(')와 큰따옴표(\")는 문자열을 감싸는 데 사용됩니다.")

# 5. \r: 캐리지 리턴 (커서를 현재 줄의 맨 앞으로 이동)
print("이것은\r캐리지 리턴입니다.")

# 6. \b: 백스페이스 (한 글자 삭제)
print("abc\bde")  # 출력: ade

## 문자열 연산


hi = "안녕"

more_politely = "하세요"

print(hi + more_politely) # 안녕하세요

print(hi*10) # 안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕

# 문자열의 길이
print(len(hi)) # 2

# 문자열의 인덱싱과 슬라이싱
print(hi[0]) # 안
print(hi[-1]) # 녕
print(more_politely[:2]) # 하세
print(more_politely[2]) # 요

# 문자열 바꾸기
# 문자열.replace(타겟문자, 바꿀문자)
print(more_politely.replace("하세요", "요세하")) # 요세하

# 문자열 포멧팅
age = 10

print("%s%s, 저는 누구누구입니다" %(hi, more_politely))

print("%s%s, 저는 누구누구입니다. %d살이에요" %(hi, more_politely, age))

# format 함수를 이용한 포멧팅
print("{0}{1}, 저는 누구누구입니다".format(hi, more_politely))

# f-string
print(f"{hi}{more_politely}, 저는 누구누구입니다.")

# 소수점 표현 f-string
pi = 3.1415926535

# f"{실수:몇번째자리까지}" 
print(f"{pi:0.2f}") # 소수점 3번째 자리에서 반올림됩니다. 3.14
print(f"{pi:0.3f}") # 소수점 4번째 자리에서 반올림됩니다. 3.142

# 문자열 관련 함수들
string = "aabbaeda"

# 개수 세기
print(string.count("a")) # 4

# 위치 찾기
print(string.find("e")) # 5
print(string.find("b")) # 찾는 문자가 여러개라면 가장 첫번째자리를 반환합니다. 2
print(string.find("z")) # -1 존재하지 않으면 -1을 반환합니다.

# 문자열 삽입 
print(".".join(string)) # 각각 문자 사이에 "."을 삽입 a.a.b.b.a.e.d.a

# 대문자 소문자 변환
print(string.upper()) # AABBAEDA
print("AABBAEDA".lower()) # aabbaeda

# 공백 지우기
blank_string = "    blank string   "

# 오른쪽 공백 지우기
print(blank_string.rstrip()) # "   blank string"
# 왼쪽 공백 지우기
print(blank_string.lstrip()) # "blank string   "
# 양쪽 공백 지우기
print(blank_string.strip()) # "blank string"

# 문자열 나누기
split_string = "this : split string"

# split(기준으로나눌문자)
# split() 공백을 기준으로 나누겠다.
# split(":") : 을 기준으로 나누겠다
print(split_string.split()) # ['this', ':', 'split', 'string']
print(split_string.split(":")) # ['this ', ' split string']
