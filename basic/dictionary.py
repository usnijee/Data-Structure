dictionary = {
    "이름": "누구",
    "나이": "10살",
    "성별": "남"
    }

print(dictionary["이름"]) # 누구

# ket value 추가, 삭제
dictionary["생일"] = "03-02" 
print(dictionary) # {'이름': '누구', '나이': '10살', '성별': '남', '생일': '03-02'}

del dictionary["성별"]
print(dictionary) # {'이름': '누구', '나이': '10살', '생일': '03-02'}

# 이미 존재하는 key에 value를 할당하면 값이 업데이트 됩니다.
# 중복키를 허용하지 않습니다.
dictionary["이름"] = "최양임"
print(dictionary) # {'이름': '최양임', '나이': '10살', '생일': '03-02'}

# 딕셔너리 관련 함수

# key 값만 모아 dict_key 객체를 리턴합니다.
print(dictionary.keys()) # dict_keys(['이름', '나이', '생일'])

# value 값만모아 dict_values 객체를 돌려줍니다
print(dictionary.values()) # dict_values(['최양임', '10살', '03-02'])

# key ,value 쌍을 튜플로 묶어 dict_items 객체로 돌려줍니다
print(dictionary.items()) # dict_items([('이름', '최양임'), ('나이', '10살'), ('생일', '03-02')])

# key 값으로 value값을 가져옵니다
# dictionary["생일"] 과 같은 결과를 리턴하지만
# 차이로는 dictionary["생일"] 키가 없을때 에러를 발생시킵니다
# .get() 없을시 None을 반환합니다.
print(dictionary.get("생일")) # 03-02

# "이름" 이라는 ket 가 딕셔너리 안에있는지 학인
print("이름" in dictionary) # True

# 딕셔너리 비우기
print(dictionary.clear()) # None**