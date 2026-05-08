---
name: event-prep-orchestrator
description: 주말 행사 준비 하네스의 팀장 Skill. 6명의 에이전트를 순서에 맞게 조율해 종합 계획서, 안전 체크리스트, 회고록을 완성한다.
triggers:
  - "행사 준비"
  - "주말 행사"
  - "event-prep-orchestrator"
---

# 주말 행사 준비 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 6명의 팀원(rule-writer, supply-planner, role-assigner, schedule-builder, safety-inspector, event-retrospector)이 올바른 순서로 일하도록 조율합니다.

## 필수 입력

- 행사 종류 (바베큐 파티, 운동회, 동네 모임 등) — 필수
- 날짜 및 시작 시간 — 필수
- 장소 — 필수
- 예상 인원 — 필수
- 테마 또는 특별 요청 — 없으면 "없음"으로 진행

## 입력 확인

시작 전 반드시 확인합니다:
- 행사 종류, 날짜, 장소, 인원 중 하나라도 없으면 → 먼저 물어봅니다.
- 시작 시간이 없으면 → 타임라인 작성 전에 요청합니다.
- 나머지 정보는 없으면 가정 사실을 명시하고 진행합니다.

## 실행 흐름

### 1단계: 기본 규칙 작성 (rule-writer)

rule-writer subagent를 사용해서:
- `write-event-rules` Skill: 행사 기본 규칙 정리
- 산출물: `event/artifacts/01-rules.md`

### 2단계: 동시 작성 (Fan-out)

`01-rules.md`가 완성되면 세 에이전트를 동시에 실행합니다.

**[2a] supply-planner subagent:**
- `plan-event-supplies` Skill: 카테고리별 준비물 목록
- 산출물: `event/artifacts/02-supplies.md`

**[2b] role-assigner subagent:**
- `assign-event-roles` Skill: 역할 분담표
- 산출물: `event/artifacts/03-roles.md`

**[2c] schedule-builder subagent:**
- `build-event-schedule` Skill: 당일 타임라인
- 산출물: `event/artifacts/04-schedule.md`

### 3단계: 종합 계획서 병합

4개 artifacts를 읽어 `event/plan.md`를 작성합니다.

병합 형식:
```md
# [행사 이름] 종합 계획서

## 기본 규칙 요약
(01-rules.md 핵심 발췌)

## 준비물 체크리스트
(02-supplies.md 전체)

## 역할 분담표
(03-roles.md 전체)

## 당일 타임라인
(04-schedule.md 전체)
```

### 4단계: 안전 점검 (safety-inspector)

safety-inspector subagent를 사용해서:
- `inspect-safety` Skill: 위험 요소 + 구급용품 + 비상 연락처
- 입력: `event/plan.md`
- 산출물: `event/safety.md`

### 5단계: 회고 (event-retrospector) — 행사 후 별도 호출

사용자가 `/event-prep-orchestrator 회고` 또는 `회고 작성해줘`와 함께 실행 메모를 제공하면:
- event-retrospector subagent를 실행합니다.
- `write-retrospect` Skill: 회고록 작성
- 입력: 실행 메모 + `event/plan.md`
- 산출물: `event/retrospect.md`

## 파일 기반 산출물

```
event/
├── artifacts/
│   ├── 01-rules.md        ← 행사 기본 규칙
│   ├── 02-supplies.md     ← 준비물 목록
│   ├── 03-roles.md        ← 역할 분담표
│   └── 04-schedule.md     ← 당일 타임라인
├── plan.md                ← 종합 행사 계획서
├── safety.md              ← 안전 점검 체크리스트
└── retrospect.md          ← 행사 후 회고록 (행사 후 별도 실행)
```

## 실패 처리

- 입력에 필수 정보가 없으면 → 먼저 질문하고 받은 뒤 진행합니다.
- 2단계 중 하나가 비어 있으면 → 해당 에이전트만 다시 실행합니다.
- 회고 메모 없이 회고 요청이 오면 → 실행 메모를 먼저 요청합니다.

## 완료 보고 형식

```
행사 준비 계획이 완성되었습니다.

저장 위치: event/

종합 계획서: event/plan.md
안전 체크리스트: event/safety.md

지금 바로 할 일:
1. event/plan.md를 열어 기본 규칙과 역할 분담 확인
2. event/safety.md에서 비상 연락처 칸 직접 채우기
3. 행사 후: /event-prep-orchestrator 회고 + 실행 메모로 회고록 작성
```
