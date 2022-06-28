runInut = False
if runInut:
    # 입력
    ## 데이터 갯수 입력
    n = int(input())
    ## 각 데이터를 공백으로 구분해 입력
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data)
    ## 정해진 적은 수의 데이터 입력 받기
    n, m, k = map(int, input().split())
    print(n, m, k)
    ## 하지만 input()은 느리기에 유사시엔 아래 방법을 사용
    import sys
    ### rstript으로 끝에 줄바꿈 문자 제거
    sys.stdin.readline().rstrip()

    data = sys.stdin.readline().rstrip()
    print(data)

# 출력
print(1, 2)
answer = 12
print("정답은 " + str(answer))  # 수와 문자열 사이에 + 안 됨

## f-string(문자열 보간)
print(f"정답은 {answer}입니다.")

# 라이브러리 함수
## 내장 함수(import 없이 사용)
# input()
print()
result = sum([1, 2, 3, 4, 5])
result = min([1, 2, 3, 4, 5])
result = max([1, 2, 3, 4, 5])
result = eval("(3 + 5) * 7")
result = sorted([9, 2, 6, 1, 8], reverse=True)
result = sorted([('A', 30), ('B', 80), ('C', 11)],
                key=lambda x: x[1],
                reverse=True)

## itertools
### permutations(iterable에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산)
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print(result)

### combinations(iterable에서 r개의 데이터를 순서를 고려하지 않고 뽑아 나열하는 모든 경우(조합)를 계산)
from itertools import combinations

result = list(combinations(data, 2))
print(result)

### product(permutations + 중복 허용)
from itertools import product

result = list(product(data, repeat=2))
print(result)

### combinations_with_replacement(combinations + 중복 허용)
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
print(data)

## heapq(PriorityQueue보다 빠름, 최소 힙, 삽입 시 O(NlogN)으로 오름차순 정렬 완료, 가장 위가 제일 작은 원소)
import heapq

def minHeapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = minHeapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

### 최대 힙은 제공 안하므로 아래 같은 방법을 이용
def maxHeapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = maxHeapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

## bisect(이진탐색용, O(logN))
### bisect_left(a,x), bisect_right(a,x) - 정렬 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽/오른쪽 인덱스를 찾음
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

### left <= x <= right 를 정렬된 리스트에서 빠르게 찾을 수 있음
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

## collections
### deque, Counter가 잘 쓰임
### Queue는 특수한 용도라고 함
### deque은 맨 앞, 뒤 삽입, 제거시 O(1) 보장
### 인덱싱 불가
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(list(data))

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue'])

print(counter['blue'], dict(counter))

## math
import math
print(math.factorial(5))
print(math.sqrt(16))
print(math.gcd(21, 14))
print(math.pi)
print(math.e)