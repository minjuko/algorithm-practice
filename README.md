# Algorithm Practice

Python 중심의 알고리즘·자료구조 학습 저장소입니다. 온라인 저지 풀이와 코딩테스트 교재 예제를 출처별로 나눠 관리합니다.

## 저장소 구조

```text
.
├─ solutions/
│  ├─ baekjoon/             # 브론즈·실버·골드 난이도별
│  ├─ programmers/          # 프로그래머스 레벨·유형별
│  └─ joonlab/              # 백준 학습용 문제 묶음
├─ books/
│  └─ this-is-coding-test/  # 『이것이 취업을 위한 코딩 테스트다』 장별 예제
├─ education/               # 교육 프로그램 문제 풀이 (Git 추적 제외)
├─ playground/              # 짧은 코드 실험
└─ test-prac/               # 문법·라이브러리 연습
```

## 풀이 파일 이름

온라인 저지는 `{문제번호}_{문제명}.py`로 저장하고, 같은 문제의 다른 풀이는 뒤에 풀이 방법을 덧붙입니다.

```text
solutions/baekjoon/silver/1012_유기농_배추.py
solutions/programmers/level-2/42861_섬_연결하기_kruskal.py
```

백준 풀이 폴더는 브론즈·실버·골드로 나눕니다. 새 문제를 추가할 때 현재 백준 난이도를 기준으로 폴더를 선택하고, 난이도가 바뀌면 파일을 해당 폴더로 옮깁니다. 문제명은 백준의 공식 제목을 사용합니다. 자세한 기준은 [백준 풀이 안내](solutions/baekjoon/README.md)를 참고하세요.

교재 예제는 출처와 장 번호를 유지합니다. 같은 절에 예제가 여러 개 있으면 `03-02-1`, `03-02-2`처럼 번호를 붙여 서로 다른 예제 파일로 둡니다. 장별 구성과 예제 목록은 [교재 README](books/this-is-coding-test/README.md)를 참고하세요.

## 실행

Python 파일은 Python 3에서 개별 실행합니다. 온라인 저지 제출 코드는 문제 형식에 맞는 입출력을 포함하고, 프로그래머스 제출 코드는 요구된 `solution` 함수를 유지합니다. 학습 원칙은 [STUDY_GUIDE.md](STUDY_GUIDE.md)에 정리했습니다.
