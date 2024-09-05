'''

1. 객체 ( = 인스턴스) => 특정 클래스로 만들어진 실체
instance_variable = ClassName() 형식으로 생성

2. 메서드(method): 클래스 바디 안에서 정의되는 함수
   클래스의 인스턴스가 생성되고 어트리뷰트(attribute)로서 호출되면, 클래스내에 정의된 메소드는 첫 번째 인자로 self를 통해 인스턴스 객체를 받는다 -> 첫번째 인자를 self로 안하면 에러가 발생
   즉, method의 self는 메모리에 저장되어 있는 인스턴스 자체라고 봐도 무방 

3. 클래스 속성(attribute)
   클래스 속성을 만들 때는 __init__메서드 안에서 self.속성에 값을 할당하면 된다.
   def __init__(self)는 '생성자'라고 하며 클래스의 객체가 선언되는 순간 최초로 1번만 호출된다. 

   ex. 
   class Person:
    def__init__(self):   # 객체가 생성되는 순간 생성자 호출, self는 Person class 객체라고 봐도 무방
        self.hello = "안녕하세요." # 객체의 hello라는 속성을 "안녕하세요"라고 최초 초기화
    
    def greeting(self):
        print(self.hello)

   james = Person()  # Person class 객체 생성 
   james.greeting()  # Person class의 greeting 메소드 호출 -> 객체를 생성시 생성자에서 hello 속성에 "안녕하세요"를 저장했고 greeting 메소드는 hello속성을 출력하는 기능을 가진 메소드

   ex2. 
   Class ClassName:
    def __init__(self,param1,param2):  # 생성자는 디폴트 요소이기에 이 클래스가 만들어짐과 동시에 생성됨 ,, 객체가 생성되면 최초로 1번 실행
        self.attr1 = param1
        self.attr2 = param2
   
   jinsu = ClassName(arg1,arg2)

'''

class Person:
    def __init__(self):            # __init__(self)는 생성자를 나타내며, 클래스로 하여금 인스턴스가 생성될 때 최초 한 번 실행되는 특수한 매직 매소드 
        self.hello = "안녕하세요"

    def greeting(self):
        print(self.hello)
 
jinsu = Person()
jinsu.greeting()


class Person2:
    def __init__(self, name, age, address, wallet): 
        self.hello = "안녕하세요."
        self.name = name      
        self.age = age      # 속성명 앞에 __를 붙이면 비공개 속성으로 바뀌어 클래스 밖에서 속성 재할당이 불가능하다.
        self.address = address
        self.__wallet = wallet
    
    def greeting(self):
        print(f"{self.hello}. 제 이름은 {self.name}입니다.")

    def pay(self, amount):
        if self.__wallet < amount:
            print("돈이 모자랍니다.")
            return
        self.__wallet -= amount
        print(f"이제 {self.__wallet}원 남았네요.")


maria = Person2("마리아", 20, "서울시 노원구", 10000)
maria.greeting()

maria.age = 50                 # maria.age = 50을 진행하면 속성인 age에 50이 재할당된다. --> 속성 값을 재할당 즉 변경하지 못하게 하려면 비공개 속성을 사용해야한다. 

print(f"이름 : {maria.name}")  # 클래스 바깥에서 속성에 접근할 때는 객체.속성을 진행하면 속성 조회가 가능하다 
print(f"나이 : {maria.age}")
# print(f"내 보유 자산 : {maria.__wallet}") # -> 오류 발생 ,, 비공개 속성은 class 외부에서는 접근 자체가 불가능하다. 비공개 속성은 오직 class 내부에서만 사용가능하다 
maria.pay(3000)


