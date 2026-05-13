"""
Python 문자열 포맷팅 방식 비교
: %, str.format(), f-string, Template
"""

import timeit
from string import Template

name = "Alice"
age = 30
score = 95.678


# ── 1. % 포맷팅 (구식) ──────────────────────────────────────────────────────
def percent_format():
    return "이름: %s, 나이: %d, 점수: %.2f" % (name, age, score)


# ── 2. str.format() ─────────────────────────────────────────────────────────
def str_format():
    return "이름: {}, 나이: {}, 점수: {:.2f}".format(name, age, score)


def str_format_named():
    return "이름: {name}, 나이: {age}, 점수: {score:.2f}".format(
        name=name, age=age, score=score
    )


# ── 3. f-string (Python 3.6+, 권장) ─────────────────────────────────────────
def f_string():
    return f"이름: {name}, 나이: {age}, 점수: {score:.2f}"


def f_string_expr():
    return f"내년 나이: {age + 1}, 점수 반올림: {round(score)}"


# ── 4. Template (외부 입력 안전 처리용) ────────────────────────────────────
def template_format():
    t = Template("이름: $name, 나이: $age")
    return t.substitute(name=name, age=age)


# ── 출력 ────────────────────────────────────────────────────────────────────
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
print("\n" + "=" * 55)
print(" 기능 비교")
print("=" * 55)
features = [
    ("가독성",       "보통",  "좋음",  "매우 좋음", "보통"),
    ("수식 포함",    "X",     "X",     "O",         "X"),
    ("안전한 치환",  "X",     "X",     "X",         "O"),
    ("Python 버전",  "전체",  "2.6+",  "3.6+",      "전체"),
]
header = f"  {'항목':<14} {'%':<8} {'format':<10} {'f-string':<12} {'Template'}"
print(header)
print("  " + "-" * 51)
for row in features:
    print(f"  {row[0]:<14} {row[1]:<8} {row[2]:<10} {row[3]:<12} {row[4]}")
