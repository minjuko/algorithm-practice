"""코딩 테스트용 Python 3 문법.

Ctrl+F 키워드: 입력, 출력, 숫자, 문자열, 리스트, 튜플, 딕셔너리, 집합,
조건문, 반복문, 함수, 정렬, deque, Counter, heapq, itertools, bisect,
수학, 소수, 진법, 비트, 복사, BFS, DFS, 격자, 시간 복잡도.

외부 입력 없이 파일 전체를 그대로 실행할 수 있다.
"""

from bisect import bisect_left, bisect_right, insort
from collections import Counter, defaultdict, deque
import copy
from functools import reduce
import heapq
from itertools import (
    accumulate, combinations, combinations_with_replacement, permutations, product,
)
import math
import sys


# =============================================================================
# 1. 입력 / 출력
# =============================================================================

# text = input().strip()                       # 문자열 한 줄
# input = sys.stdin.readline                   # 빠른 입력('\n' 주의)
# n = int(input())
# a, b = map(int, input().split())
# numbers = list(map(int, input().split()))
# matrix = [list(map(int, input().split())) for _ in range(n)]
# lines = [input().rstrip() for _ in range(n)] # 오른쪽 개행 제거
# for line in sys.stdin: ...                   # EOF까지 입력

print("출력:", 1, 2, 3)
print(*[1, 2, 3], sep=", ")
print("같은 줄", end=" -> ")
print("이어 쓰기")

name, score = "민수", 92.3456
print(f"{name}: {score:.2f}점 / {1234567:,} / {7:03d}")
output = [str(x) for x in range(3)]
print("대량 출력:\n" + "\n".join(output))       # 모아서 한 번에 출력


# =============================================================================
# 2. 변수 / 자료형 / 형 변환 / 연산자
# =============================================================================

integer, real, boolean, nothing, text = 10, 3.14, True, None, "123"
print(type(integer), int(text), float(text), str(integer))
print(bool(0), bool(""), bool([]), bool(1))     # 빈 값과 0은 False

# 산술: + - * / // % **, 비교: == != < <= > >=, 논리: and or not
print(7 / 3, 7 // 3, 7 % 3, 2**10)
quotient, remainder = divmod(17, 5)
x, y = 3, 7
x, y = y, x                                    # 값 교환
print(quotient, remainder, x, y, 0 <= x < 10)  # 연쇄 비교

# None은 is None으로 확인한다. 값 비교는 ==, 동일 객체 비교는 is.
value = None
if value is None:
    value = 0
nickname = "" or "익명"                        # 0, "", []도 거짓임에 주의


# =============================================================================
# 3. 숫자 / 부동소수점
# =============================================================================

print(abs(-5), round(3.14159, 2), min(3, 1), max(3, 1), pow(2, 10))
print(float("inf"), float("-inf"))
print(math.isclose(0.1 + 0.2, 0.3))            # 실수는 ==보다 isclose
print(math.ceil(3.1), math.floor(3.9), math.trunc(-3.9), math.sqrt(16))


# =============================================================================
# 4. 문자열(str) - 불변 자료형
# =============================================================================

s = "  Hello Python  "
print(s.strip(), s.lstrip(), s.rstrip())
print(s.lower(), s.upper(), s.swapcase())
print("banana".replace("a", "A", 2))
print("a,b,c".split(","), "-".join(["2026", "09", "25"]))

word = "algorithm"
print(word[0], word[-1], word[1:4], word[:4], word[4:], word[::-1])
print(len(word), "go" in word, word.count("i"))
print(word.find("r"), word.find("z"))           # 없으면 -1(index는 오류)
print("42".isdigit(), "abc".isalpha(), "a1".isalnum())
print("hello".startswith("he"), "main.py".endswith(".py"), "7".zfill(3))
print(ord("A"), chr(65))                       # 문자 <-> 코드 포인트

chars = list("cat")                            # 문자열 수정 방법
chars[0] = "b"
print("".join(chars))


# =============================================================================
# 5. 리스트(list) - 가변, 순서 있음, 중복 허용
# =============================================================================

arr = [3, 1, 4]
arr.append(1)                 # 끝에 한 개 추가 O(1)
arr.extend([5, 9])            # 여러 개 추가
arr.insert(1, 2)              # 특정 위치 삽입 O(N)
last = arr.pop()              # 끝 제거/반환 O(1)
at_one = arr.pop(1)           # 특정 위치 제거 O(N)
arr.remove(1)                 # 해당 값을 처음 한 번 제거(없으면 오류)
print(arr, last, at_one)
print(arr[0], arr[-1], arr[1:3], arr[::-1])
print(len(arr), sum(arr), min(arr), max(arr), arr.count(4), arr.index(4))

arr.sort()                    # 원본 변경, 반환값 None
arr.sort(reverse=True)
ascending = sorted(arr)       # 새 리스트 반환
print(arr, ascending)

squares = [x * x for x in range(10) if x % 2 == 0]
matrix = [[0] * 3 for _ in range(2)]            # 올바른 2차원 리스트
bad_matrix = [[0] * 3] * 2                      # 내부 리스트를 공유하므로 주의
bad_matrix[0][0] = 1
print(squares, matrix, bad_matrix)

first, *middle, last = [1, 2, 3, 4, 5]          # 언패킹
stack = []                                      # 스택: append / pop
stack.append(10)
stack.append(20)
print(first, middle, last, stack.pop())


# =============================================================================
# 6. 튜플(tuple) - 불변, 딕셔너리 키로 사용 가능
# =============================================================================

point, single = (3, 4), (1,)                   # 한 원소는 쉼표 필수
px, py = point
print(point, single, px, py, tuple([1, 2]))


# =============================================================================
# 7. 딕셔너리(dict) - 평균 O(1) 조회/삽입/삭제
# =============================================================================

scores = {"kim": 90, "lee": 80}
scores["park"] = 100
scores["kim"] += 5
print(scores["kim"], scores.get("choi"), scores.get("choi", 0))
print("kim" in scores, list(scores.keys()), list(scores.values()))
for key, val in scores.items():
    print(key, val)

deleted = scores.pop("lee", None)               # 기본값을 주면 없어도 안전
scores.setdefault("choi", 70)                   # 없을 때만 추가
merged = scores | {"kim": 100}                  # 3.9+, 오른쪽 값 우선
square_map = {x: x * x for x in range(5)}
print(deleted, merged, square_map)


# =============================================================================
# 8. 집합(set) - 중복/순서 없음, 평균 O(1) 조회
# =============================================================================

a, b = {1, 2, 3}, {3, 4, 5}
print(a & b, a | b, a - b, a ^ b)              # 교/합/차/대칭차
print(a <= {1, 2, 3, 4})                        # 부분집합
a.add(4)
a.update([5, 6])
a.discard(100)                                  # 없어도 안전(remove는 오류)
empty_set = set()                               # {}는 빈 dict
print(a, len(set([1, 1, 2])), empty_set)


# =============================================================================
# 9. 조건문 / 반복문
# =============================================================================

n = 7
if n < 0:
    category = "음수"
elif n == 0:
    category = "0"
else:
    category = "양수"
parity = "짝수" if n % 2 == 0 else "홀수"
print(category, parity)

print(list(range(3)), list(range(2, 8, 2)), list(range(3, 0, -1)))
for index, item in enumerate(["a", "b"], start=1):
    print(index, item)
for left, right in zip([1, 2], [10, 20]):
    print(left + right)

# break는 종료, continue는 이번 반복 건너뛰기. 반복문의 else는 break 없을 때 실행.
for item in [1, 2, 3]:
    if item == 4:
        break
else:
    print("4 없음")
print(any(x > 3 for x in [1, 4, 2]), all(x > 0 for x in [1, 4, 2]))


# =============================================================================
# 10. 함수 / 람다 / 스코프
# =============================================================================

def add(a: int, b: int = 0) -> int:
    """타입 힌트는 실행 시 자료형을 강제하지 않는다."""
    return a + b


def total(*numbers: int) -> int:                 # 위치 인자 -> tuple
    return sum(numbers)


def build_info(**kwargs: object) -> dict[str, object]:  # 키워드 인자 -> dict
    return kwargs


def append_safely(value: int, items: list[int] | None = None) -> list[int]:
    """가변 기본값(items=[])은 공유되므로 None을 사용한다."""
    if items is None:
        items = []
    items.append(value)
    return items


print(add(3, b=4), total(1, 2, 3), build_info(name="kim"))
print((lambda x: x * 2)(5), sorted(["bbb", "a", "cc"], key=len))


# =============================================================================
# 11. 정렬
# =============================================================================

records = [("kim", 90), ("lee", 90), ("park", 80)]
# 점수 내림차순, 이름 오름차순(숫자는 -를 붙여 역순)
print(sorted(records, key=lambda item: (-item[1], item[0])))
print(sorted(records, reverse=True))             # 전체 기준 역순
print(sorted(zip(["b", "a"], [80, 90])))        # 배열 함께 정렬


# =============================================================================
# 12. collections - deque / Counter / defaultdict
# =============================================================================

queue = deque([1, 2, 3])                        # 양끝 연산 O(1), BFS 큐
queue.append(4)
queue.appendleft(0)
print(queue.popleft(), queue.pop(), list(queue))
queue.rotate(1)
print(list(queue))

counter = Counter("banana")                     # 없는 키는 0
print(counter, counter["a"], counter.most_common(2), list(counter.elements()))
groups: defaultdict[str, list[int]] = defaultdict(list)
groups["odd"].append(1)
frequency: defaultdict[str, int] = defaultdict(int)
frequency["a"] += 1
print(dict(groups), dict(frequency))


# =============================================================================
# 13. heapq - 최소 힙(우선순위 큐)
# =============================================================================

heap = [5, 1, 3]
heapq.heapify(heap)                              # O(N)
heapq.heappush(heap, 2)                         # O(log N)
print(heapq.heappop(heap), heap[0], heap)        # O(log N)
print(heapq.nsmallest(2, heap), heapq.nlargest(2, heap))

max_heap = []                                   # 최대 힙: 부호 반전
for item in [3, 1, 5]:
    heapq.heappush(max_heap, -item)
print(-heapq.heappop(max_heap))

priority_queue = [(2, "B"), (1, "A")]          # 튜플은 앞부터 비교
heapq.heapify(priority_queue)
print(heapq.heappop(priority_queue))


# =============================================================================
# 14. itertools - 순열 / 조합 / 곱집합 / 누적합
# =============================================================================

items = [1, 2, 3]
print("순열", list(permutations(items, 2)))
print("조합", list(combinations(items, 2)))
print("중복조합", list(combinations_with_replacement(items, 2)))
print("곱집합", list(product([0, 1], repeat=2)))
print("누적합", list(accumulate(items)))
print("누적최댓값", list(accumulate([3, 1, 4, 2], max)))


# =============================================================================
# 15. bisect - 정렬 리스트 이분 탐색
# =============================================================================

ordered = [1, 2, 2, 2, 4, 5]
left, right = bisect_left(ordered, 2), bisect_right(ordered, 2)
print(left, right, "2의 개수", right - left)
insort(ordered, 3)                              # 정렬 유지 삽입(삽입 자체 O(N))
print(ordered)


# =============================================================================
# 16. 수학 / 소수
# =============================================================================

print(math.gcd(12, 18), math.lcm(12, 18))
print(math.factorial(5), math.comb(5, 2), math.perm(5, 2), math.isqrt(17))


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, math.isqrt(number) + 1))


def sieve(limit: int) -> list[int]:
    """limit 이하 소수 목록(에라토스테네스의 체)."""
    prime = [False, False] + [True] * max(0, limit - 1)
    for number in range(2, math.isqrt(limit) + 1):
        if prime[number]:
            for multiple in range(number * number, limit + 1, number):
                prime[multiple] = False
    return [number for number, ok in enumerate(prime[: limit + 1]) if ok]


print(is_prime(97), sieve(30))


# =============================================================================
# 17. 진법 / 비트
# =============================================================================

print(bin(10), oct(10), hex(255))               # 접두사 포함
print(format(10, "b"), format(10, "08b"))       # 접두사 없음 / 8자리
print(int("1010", 2), int("ff", 16), int("z", 36))
# &: AND, |: OR, ^: XOR, ~: NOT, << >>: 시프트
mask = 0
mask |= 1 << 2                                  # 2번 비트 켜기
print(bool(mask & (1 << 2)))                    # 확인
mask &= ~(1 << 2)                               # 끄기
print(mask, (13).bit_count())                   # 1 비트 개수


# =============================================================================
# 18. 얕은 복사 / 깊은 복사
# =============================================================================

original = [[1, 2], [3, 4]]
shallow = original[:]                           # 내부 리스트 공유
deep = copy.deepcopy(original)                  # 내부까지 복사
original[0][0] = 99
print("원본/얕은/깊은", original, shallow, deep)


# =============================================================================
# 19. BFS / DFS 뼈대
# =============================================================================

sample_graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}


def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    order, visited, queue = [], {start}, deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)                 # 큐에 넣을 때 방문 처리
                queue.append(nxt)
    return order


def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    order, visited, stack = [], set(), [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph[node]))       # 작은 번호부터 방문 예시
    return order


print("BFS/DFS", bfs(sample_graph, 1), dfs(sample_graph, 1))
# 재귀가 깊은 문제에서만: sys.setrecursionlimit(200_000)


# =============================================================================
# 20. 2차원 격자 이동
# =============================================================================

grid = [[0, 0, 1], [1, 0, 0]]
rows, cols = len(grid), len(grid[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
row, col, neighbors = 0, 0, []
for dr, dc in directions:
    nr, nc = row + dr, col + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        neighbors.append((nr, nc))
print("격자 이웃", neighbors)


# =============================================================================
# 21. 예외 / 클래스 / 기타(알고리즘 사용 빈도 낮음)
# =============================================================================

try:
    parsed = int("123")
except ValueError:
    parsed = 0


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def distance_squared(self) -> int:
        return self.x**2 + self.y**2


print(parsed, Point(3, 4).distance_squared())
print(reduce(lambda acc, item: acc * item, [1, 2, 3, 4], 1))


# =============================================================================
# 22. 실전 제출 템플릿(주석 해제 후 사용)
# =============================================================================

# import sys
# input = sys.stdin.readline
#
# def solve() -> None:
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     print(sum(numbers))
#
# if __name__ == "__main__":
#     solve()


# 시간 복잡도 메모
# list: arr[i], append, pop() O(1) / 탐색, insert, pop(i) O(N)
# dict/set: 조회·삽입·삭제 평균 O(1)
# deque: 양끝 삽입·삭제 O(1)
# heap: push/pop O(log N), heapify O(N)
# sort/sorted O(N log N), bisect 검색 O(log N)

print("\n모든 예제가 정상적으로 실행되었습니다.")
