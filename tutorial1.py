# 타입

## 수
### 정수
a = 1000
a = -1000
a = 0

### 실수(IEEE754)
a = 17.93
a = -137.2
a = -.8
a = 432e9  #432*10^9
a = 1234e-3  #1.234
print(a)

#### 0.8999999999999999
print(0.3 + 0.6, round(0.3 + 0.6, 2))

### 수 연산
a = 7
b = 3
#### 나누기, mod, 몫, pow
print(a / b, a % b, a // b, a**b)

## 리스트(동적 배열 구현)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, a[4], a[1:4], a[-2])
print(["세", "번"] * 3)

print(list(), [])

### 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)
array = [i * i for i in range(1, 10)]
print(array)
### 다차원 배열 할당(리스트 컴프리헨션을 써야함)
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
### 잘못된 다차원 배열 할당
# [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]
array = [[0] * m] * n
array[1][1] = 5
print(array)

### 리스트 메서드
a = [1, 4, 3]
a.append(2)  # [1, 4, 3, 2], O(1)
a.sort()  # [1, 2, 3, 4]
a.sort(reverse=True)  # [4, 3, 2, 1]
a.reverse()  # [1, 2, 3, 4]
a.insert(2, 3)  # [1, 2, 3, 3, 4], O(N)
a.count(3)  # 2
a.remove(1)  # [2, 3, 3, 4], O(N)

### 리스트에서 특정 원소값 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

## 문자열
data = 'Hello World'
data = "Don't you know \"Ray\"?"

### 문자열 연산
print("Hello" + " " + "World!")
print("Hi" * 3)
a = "ABCDEFG"
print(a[1:3])

## 튜플
print((1, 2, 3, 4))
# a[2] = 7 X

## 딕셔너리(해시 테이블 구현)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

print(data)

if '사과' in data:
    print("is")

### 딕셔너리 연산
print(data.keys(), data.values())
for key in data.keys():
    print(data[key])

## 집합
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

## 집합 연산
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)  # 합
print(a & b)  # 교
print(a - b)  # 차

## 집합 메서드
data = set([1, 2, 3])
data.add(4)
data.update([5, 6])
data.remove(3)


# 조건문

score =85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

## 비교 연산자
### ==, !=, >, <, >=, <=
## 논리 연산자
### and, or, not
## in 연산자
### in, not in

    
# 반복문

## while
i = 1
result = 0
while i < 10:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

## for
result = 0
for i in range(1, 10):
    result += i
print(result)

result = 0
for i in range(10): # from 0
    result += i
print(result)


# 함수
def add(a, b):
    return a + b

print(add(3,7))

def addAndPrint(a, b):
    print(a+b)

addAndPrint(3,7)
addAndPrint(b = 3, a = 7)

## 스코프 외 데이터 변경

a = 0
def func():
    global a
    a += 1

func()
print(a)

print((lambda a, b: a + b)(3,7))