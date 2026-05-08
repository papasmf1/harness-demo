---
name: morning-routine-orchestrator
description: 아침 루틴 개선 하네스의 팀장 Skill. 설정 모드(초기 계획 수립)와 기록 모드(실패 원인 누적) 두 가지로 동작하며, Feedback Loop로 루틴이 점진적으로 개선된다.
triggers:
  - "morning-routine-orchestrator"
  - "아침 루틴"
  - "아침 준비 계획"
---

# 아침 루틴 개선 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 6명의 팀원(morning-planner, alarm-advisor, outfit-checker, breakfast-preparer, departure-timer, failure-analyst)이 올바른 순서로 일하고, 기록이 쌓일수록 루틴이 점점 개선되도록 Feedback Loop를 조율합니다.

## 두 가지 모드

### 설정 모드

`/morning-routine-orchestrator 설정: [조건]`

예시: `/morning-routine-orchestrator 설정: 출근, 기상 6:30, 출근 9:00, 지하철 30분`

### 기록 모드

`/morning-routine-orchestrator 기록: [오늘 아침 실패 메모]`

예시: `/morning-routine-orchestrator 기록: 오늘 아침 옷 못 찾아서 10분 지각했어`

## 필수 입력 (설정 모드)

- 목적 (출근/등교) — 없으면 묻습니다.
- 기상 목표 시간 — 없으면 묻습니다.
- 도착 목표 시간 — 없으면 묻습니다.
- 이동 시간 — 없으면 묻습니다.

나머지는 없으면 가정값을 명시하고 진행합니다.

## 실행 흐름 (설정 모드)

### 1단계: Environment Audit + 종합 계획 (morning-planner)

morning-planner subagent를 사용해서:
- `plan-evening-prep` Skill: 전날 저녁 점검 7개 항목 작성
- `morning/progress.md`가 있으면 읽어서 반복 실패 항목을 [중점 점검] 구역에 배치
- 산출물: `morning/artifacts/00-audit.md`

### 2단계: 세 에이전트 동시 실행 (Fan-out)

`00-audit.md`가 완성되면 세 에이전트를 동시에 실행합니다.

**[2a] alarm-advisor subagent:**
- `set-alarm-plan` Skill: 기상 시간 + 알람 전략
- 산출물: `morning/artifacts/01-alarm.md`

**[2b] outfit-checker subagent:**
- `check-outfit-bag` Skill: 전날 준비할 옷·가방 체크리스트
- 산출물: `morning/artifacts/02-outfit.md`

**[2c] breakfast-preparer subagent:**
- `plan-breakfast` Skill: 15분 이내 식사 계획 + 전날 사전 준비
- 산출물: `morning/artifacts/03-breakfast.md`

### 3단계: 출발 시간 역산 (departure-timer)

departure-timer subagent를 사용해서:
- `plan-departure` Skill: 출발 = 도착 - 이동 - 여유 10분 공식
- 입력: `morning/artifacts/01-alarm.md`
- 산출물: `morning/artifacts/04-departure.md`

### 4단계: 종합 계획서 병합

5개 artifacts를 읽어 `morning/plan.md`를 작성합니다.

```md
# 아침 루틴 계획서

> 작성일: [날짜] | 목적: [출근/등교] | 기상: [  ] | 출발: [  ] | 도착: [  ]

## 전날 저녁 Environment Audit
(00-audit.md 전체)

## 알람 계획
(01-alarm.md 핵심 시간표)

## 옷·가방 체크리스트
(02-outfit.md 전체)

## 아침 식사 계획
(03-breakfast.md 전체)

## 출발 타임라인
(04-departure.md 전체)
```

## 실행 흐름 (기록 모드)

failure-analyst subagent를 실행합니다:
- `log-morning-failure` Skill: 실패 원인을 A~E 카테고리로 분류
- `morning/progress.md`가 없으면 새로 만들고, 있으면 맨 아래에 추가
- 누적 통계 표를 업데이트

## Feedback Loop 동작 방식

```
기록 모드 실행
     ↓
failure-analyst → morning/progress.md에 카테고리 추가
     ↓
다음 설정 모드 실행
     ↓
morning-planner가 progress.md를 읽음
     ↓
2회 이상 실패 카테고리 → Environment Audit [중점 점검]에 배치
     ↓
루틴이 실패 원인에 맞게 점진적으로 개선됨
```

## 파일 기반 산출물

```
morning/
├── artifacts/
│   ├── 00-audit.md      ← Environment Audit 체크리스트
│   ├── 01-alarm.md      ← 알람 계획
│   ├── 02-outfit.md     ← 옷·가방 체크리스트
│   ├── 03-breakfast.md  ← 식사 계획
│   └── 04-departure.md  ← 출발 시간 역산 + 타임라인
├── plan.md              ← 종합 아침 루틴 계획서
└── progress.md          ← 실패 원인 누적 기록 (Feedback Loop 원천)
```

## 실패 처리

- 설정 모드에서 필수 입력 누락 → 먼저 질문합니다.
- 기록 모드에서 메모 없이 기록 요청 → 메모를 먼저 요청합니다.
- progress.md 없이 기록 모드 첫 실행 → 새 파일을 만듭니다.

## 완료 보고 형식 (설정 모드)

```
아침 루틴 계획이 완성되었습니다.

저장 위치: morning/

종합 계획서: morning/plan.md

지금 바로 할 일:
1. morning/plan.md 열어서 오늘 저녁 Environment Audit 실행 (00-audit.md 체크리스트)
2. 내일 아침: 계획서대로 진행
3. 늦거나 실패하면: /morning-routine-orchestrator 기록: [실패 메모]
```

## 완료 보고 형식 (기록 모드)

```
기록 완료되었습니다.

저장 위치: morning/progress.md

카테고리: [A/B/C/D/E]
다음 번 시도할 것: [한 가지 구체적 행동]

다음 설정 모드 실행 시 이 기록이 루틴에 반영됩니다.
```
