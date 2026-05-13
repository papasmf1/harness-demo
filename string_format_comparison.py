"""
Python 문자열 포맷팅 방식 비교
: %, str.format(), f-string, Template

각 방식의 사용법·성능·기능 차이를 한눈에 확인한다.
"""

import timeit
from string import Template

# 비교에 사용할 샘플 데이터
name = "Alice"
age = 30
score = 95.678


# ── 1. % 포맷팅 ─────────────────────────────────────────────────────────────
# C 언어 printf 스타일에서 유래한 가장 오래된 방식.
# %s(문자열), %d(정수), %f(실수) 등 타입 지정자를 사용한다.
# 인수가 하나일 때는 튜플 없이 쓸 수 있지만, 여러 값이면 반드시 튜플로 묶어야 한다.
def percent_format():
    return "이름: %s, 나이: %d, 점수: %.2f" % (name, age, score)


# ── 2. str.format() ─────────────────────────────────────────────────────────
# Python 2.6에서 도입된 방식으로 % 포맷의 단점을 보완한다.
# {} 자리표시자에 순서(인덱스) 또는 키워드 이름을 지정할 수 있다.
def str_format():
    # 위치 기반: 순서대로 {} 에 값이 채워진다.
    return "이름: {}, 나이: {}, 점수: {:.2f}".format(name, age, score)


def str_format_named():
    # 키워드 기반: {변수명} 으로 가독성을 높이고 순서에 의존하지 않는다.
    return "이름: {name}, 나이: {age}, 점수: {score:.2f}".format(
        name=name, age=age, score=score
    )


# ── 3. f-string ─────────────────────────────────────────────────────────────
# Python 3.6에서 도입된 리터럴 문자열 보간 방식.
# 변수·수식을 {} 안에 직접 작성하므로 가독성이 가장 높고 실행 속도도 빠르다.
# 새 코드를 작성할 때 기본으로 선택해야 할 방식이다.
def f_string():
    return f"이름: {name}, 나이: {age}, 점수: {score:.2f}"


def f_string_expr():
    # {} 안에 임의의 파이썬 수식을 쓸 수 있다.
    return f"내년 나이: {age + 1}, 점수 반올림: {round(score)}"


# ── 4. Template ─────────────────────────────────────────────────────────────
# string 모듈의 Template은 $변수명 형태로 치환한다.
# 코드 실행이 불가능하므로 외부 입력(사용자·설정 파일)을 다룰 때 안전하다.
# substitute()는 키가 없으면 KeyError, safe_substitute()는 그대로 남긴다.
def template_format():
    t = Template("이름: $name, 나이: $age")
    return t.substitute(name=name, age=age)


# ── 포맷 결과 출력 ───────────────────────────────────────────────────────────
print("=" * 55)
print(" 포맷 결과 비교")
print("=" * 55)
print(f"{'방식':<20} {'결과'}")
print("-" * 55)
print(f"{'% 포맷':<20} {percent_format()}")
print(f"{'str.format()':<20} {str_format()}")
print(f"{'str.format(named)':<20} {str_format_named()}")
print(f"{'f-string':<20} {f_string()}")
print(f"{'f-string(수식)':<20} {f_string_expr()}")
print(f"{'Template':<20} {template_format()}")

# ── 성능 벤치마크 ────────────────────────────────────────────────────────────
# timeit은 GC를 일시 정지하고 반복 실행해 순수 실행 시간을 측정한다.
# f-string은 컴파일 시점에 바이트코드로 변환되므로 런타임 파싱 비용이 없다.
N = 100_000
benchmarks = {
    "% 포맷":        "\"이름: %s, 나이: %d\" % (name, age)",
    "str.format()":  "\"이름: {}, 나이: {}\".format(name, age)",
    "f-string":      "f\"이름: {name}, 나이: {age}\"",
}

print("\n" + "=" * 55)
print(f" 성능 벤치마크 ({N:,}회 반복)")
print("=" * 55)
setup = "name='Alice'; age=30"
for label, stmt in benchmarks.items():
    elapsed = timeit.timeit(stmt, setup=setup, number=N)
    print(f"  {label:<18} {elapsed:.4f}s")

# ── 기능 비교표 ──────────────────────────────────────────────────────────────
# 방식별 주요 특성을 한눈에 정리한 표.
# '안전한 치환': 외부 입력이 코드로 실행될 위험이 없는지 여부.
print("\n" + "=" * 55)
print(" 기능 비교")
print("=" * 55)
features = [
    ("가독성",       "보통",  "좋음",  "매우 좋음", "보통"),
    ("수식 포함",    "X",     "X",     "O",         "X"),
    ("안전한 치환",  "X",     "X",     "X",         "O"),  # Template만 해당
    ("Python 버전",  "전체",  "2.6+",  "3.6+",      "전체"),
]
header = f"  {'항목':<14} {'%':<8} {'format':<10} {'f-string':<12} {'Template'}"
print(header)
print("  " + "-" * 51)
for row in features:
    print(f"  {row[0]:<14} {row[1]:<8} {row[2]:<10} {row[3]:<12} {row[4]}")
