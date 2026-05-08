---
name: party-plan-orchestrator
description: 아이 생일파티 기획 하네스의 팀장 Skill. 5명의 에이전트를 순서에 맞게 조율하고 Feedback Loop를 실행해 3개 파티 파일을 완성한다.
triggers:
  - "생일파티 기획"
  - "파티 계획 만들어줘"
  - "party-plan-orchestrator"
---

# 생일파티 기획 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 5명의 팀원(idea-generator, budget-evaluator, venue-food-planner, guest-list-reviewer, final-editor)이 올바른 순서로 일하고, Feedback Loop가 작동하도록 조율합니다.

## 필수 입력

- 아이 나이 (필수)
- 예산 상한 (필수)
- 파티 날짜 (있으면 포함)
- 테마 또는 아이 관심사 (없으면 idea-generator가 제안)
- 예상 초대 인원 (없으면 10명 이하로 가정)
- 알레르기 또는 식이 제한 (없으면 "없음"으로 가정)

## 입력 확인

시작 전 반드시 확인합니다:
- 아이 나이가 없으면 → 나이를 먼저 물어봅니다.
- 예산이 없으면 → 예산을 물어봅니다.
- 나머지는 없으면 가정 사실을 명시하고 진행합니다.

## 실행 흐름

### 1단계: 아이디어 생성 (idea-generator)

idea-generator subagent를 사용해서:
- `generate-party-ideas` Skill: 아이디어 초안 3가지 작성
- 산출물: `party/artifacts/01-ideas.md`

### 2단계: 평가 + Feedback Loop (budget-evaluator)

budget-evaluator subagent를 사용해서:
- `evaluate-budget` Skill: Rubric 5개 기준으로 채점
- 산출물: `party/artifacts/02-evaluation.md`

**Feedback Loop 규칙:**
- FAIL → idea-generator에 수정 요청 → 재평가 (최대 2회)
- 2회 후에도 FAIL → 사용자에게 조건 완화 요청
- WARN → 다음 단계로 진행 (WARN 내용은 이후 단계에서 반영)
- PASS → 바로 3단계로 진행

### 3단계: 장소·음식 + 명단 (동시 진행)

**[3a] venue-food-planner subagent:**
- `plan-venue-food` Skill: 장소·음식 구체화
- 산출물: `party/artifacts/03-venue-food.md`

**[3b] guest-list-reviewer subagent:**
- `review-guest-list` Skill: 초대 명단 점검
- 산출물: `party/artifacts/04-guest-list.md`

### 4단계: 최종 편집 (final-editor)

final-editor subagent를 사용해서:
- `finalize-party-plan` Skill: 4개 artifacts 합산
- 산출물: `party/plan.md`, `party/checklist.md`, `party/budget.md`

## 파일 기반 산출물

```
party/
├── artifacts/
│   ├── 01-ideas.md        ← 아이디어 초안
│   ├── 02-evaluation.md   ← Rubric 평가 결과
│   ├── 03-venue-food.md   ← 장소·음식 계획
│   └── 04-guest-list.md   ← 초대 명단
├── plan.md                ← 메인 파티 계획서
├── checklist.md           ← 준비 체크리스트
└── budget.md              ← 예산 요약
```

## 실패 처리

- 1단계 결과가 비어 있으면 → idea-generator를 한 번 더 실행합니다.
- Feedback Loop 2회 후 FAIL → 사용자에게 예산 또는 조건 완화를 요청합니다.
- 3단계 파일 중 하나가 비어 있으면 → 해당 에이전트를 다시 실행합니다.

## 완료 보고 형식

```
✅ 생일파티 계획이 완성되었습니다.

📁 저장 위치: party/

메인 계획서: party/plan.md
준비 체크리스트: party/checklist.md
예산 요약: party/budget.md

지금 바로 할 일:
1. party/plan.md를 열어 파티 개요 확인
2. party/checklist.md에서 D-14 항목부터 시작
3. party/budget.md에서 실제 비용 업데이트
```
