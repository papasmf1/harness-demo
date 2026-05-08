---
name: hobby-plan-orchestrator
description: 새 취미 시작 계획 하네스의 팀장 Skill. 6명의 에이전트를 순서에 맞게 조율하고 예산 Guardrail Loop를 실행해 종합 계획서를 완성한다.
triggers:
  - "취미 계획"
  - "취미 시작"
  - "hobby-plan-orchestrator"
---

# 취미 시작 계획 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 6명의 팀원(goal-setter, method-picker, gear-advisor, hobby-budget-guard, routine-builder, progress-checker)이 올바른 순서로 일하고, 예산 Guardrail이 작동하도록 조율합니다.

## 필수 입력

- 취미 종류 — 필수
- 예산 한도 — 필수 (Guardrail 작동 기준)
- 목표 기간 — 없으면 6개월로 가정
- 주당 가용 시간 — 없으면 "3회, 1시간"으로 가정 후 명시

## 입력 확인

시작 전 반드시 확인합니다:
- 취미 종류가 없으면 → 먼저 물어봅니다.
- 예산 한도가 없으면 → Guardrail을 실행할 수 없으므로 반드시 물어봅니다.
- 나머지는 없으면 가정 사실을 명시하고 진행합니다.

## 실행 흐름

### 1단계: 목표 설정 (goal-setter)

goal-setter subagent를 사용해서:
- `set-hobby-goal` Skill: SMART 목표 작성
- 산출물: `hobby/artifacts/01-goal.md`

### 2단계: 학습 방식 선택 (method-picker)

method-picker subagent를 사용해서:
- `pick-learning-method` Skill: 3가지 방식 비교 + 추천
- 입력: `hobby/artifacts/01-goal.md`
- 산출물: `hobby/artifacts/02-method.md`

### 3단계: 장비 조사 + 예산 Guardrail Loop

**[3a] gear-advisor subagent:**
- `research-gear` Skill: 장비 목록 + 총 예상 비용
- 산출물: `hobby/artifacts/03-gear.md` (초안)

**[3b] hobby-budget-guard subagent:**
- `check-hobby-budget` Skill: PASS/BLOCK 판정
- 결과를 `03-gear.md` 맨 아래에 추가

**Guardrail Loop 규칙:**
- PASS → 4단계로 진행
- PASS with 주의 → 경고 메모 포함 후 4단계로 진행
- BLOCK → gear-advisor에 조정 제안 전달 후 재작업 (최대 2회)
- 2회 후 BLOCK → 사용자에게 예산 상향 또는 항목 제외 확인 요청

### 4단계: 연습 루틴 작성 (routine-builder)

routine-builder subagent를 사용해서:
- `build-practice-routine` Skill: 주간 루틴 + 월간 마일스톤
- 입력: `hobby/artifacts/01-goal.md`, `hobby/artifacts/02-method.md`
- 산출물: `hobby/artifacts/04-routine.md`

### 5단계: 종합 계획서 병합

4개 artifacts를 읽어 `hobby/plan.md`를 작성합니다.

```md
# [취미 이름] 시작 계획서

## 목표 요약 (01-goal.md 핵심 발췌)

## 학습 방식 (02-method.md 추천 결과)

## 장비 목록 (03-gear.md 전체)

## 연습 루틴 (04-routine.md 전체)
```

### 6단계: 진도 점검 (progress-checker) — 매달 별도 호출

사용자가 `/hobby-plan-orchestrator 점검: [이번 달 실행 메모]`를 입력하면:
- progress-checker subagent를 실행합니다.
- `check-hobby-progress` Skill: 월간 보고서 작성
- 산출물: `hobby/progress.md` (누적 추가)

## 파일 기반 산출물

```
hobby/
├── artifacts/
│   ├── 01-goal.md       ← SMART 목표 문서
│   ├── 02-method.md     ← 학습 방식 비교 + 추천
│   ├── 03-gear.md       ← 장비 목록 + 예산 판정 결과
│   └── 04-routine.md    ← 주간 루틴 + 월간 마일스톤
├── plan.md              ← 종합 취미 시작 계획서
└── progress.md          ← 월간 진도 점검 보고서 (누적)
```

## 실패 처리

- 입력에 취미 종류나 예산이 없으면 → 먼저 질문합니다.
- Guardrail 2회 BLOCK 후 → 사용자에게 조건 확인을 요청합니다.
- 진도 점검 메모 없이 점검 요청 오면 → 메모를 먼저 요청합니다.

## 완료 보고 형식

```
취미 시작 계획이 완성되었습니다.

저장 위치: hobby/

종합 계획서: hobby/plan.md

지금 바로 할 일:
1. hobby/plan.md 열어서 장비 목록 확인 후 구매 시작
2. 이번 주부터 연습 루틴 시작
3. 한 달 후: /hobby-plan-orchestrator 점검: [실행 메모]
```
