---
name: travel-prep-orchestrator
description: 목적지·출발일·귀국일·예산을 받아 항공권, 숙소, 보험, 환전, 짐, 집 비우기, 점검 일정을 순서대로 완성하고 5개 파일로 저장합니다. 2주 해외여행 준비를 처음부터 끝까지 정리할 때 사용합니다.
---

# 여행 준비 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 4명의 팀원(logistics-agent, finance-agent, packing-agent, home-agent)이 올바른 순서로 일하도록 조율하고, 각 결과를 5개 파일로 엮습니다.

## 필수 입력

- 출발지 (기본: 서울/인천)
- 목적지 (도시 또는 국가)
- 출발일 (YYYY-MM-DD)
- 귀국일 (YYYY-MM-DD)
- 예산 (선택)

## 입력 확인

시작 전에 반드시 확인합니다:
- 목적지가 없으면 → 목적지를 먼저 물어봅니다.
- 출발일이 없으면 → 출발일을 물어봅니다.
- 귀국일이 없으면 → 귀국일 또는 여행 기간을 물어봅니다.
- 출발까지 30일 미만이면 → 일정이 촉박함을 알리고 가능한 항목부터 진행합니다.
- 모두 확인되면 바로 1단계로 넘어갑니다.

## 실행 흐름

### 1단계: 예약 (logistics-agent)

logistics-agent subagent를 사용해서:
- `research-flights` Skill: 항공권 비교 체크포인트 작성
- `check-accommodation` Skill: 숙소 확인 항목 작성
- Handoff 메모 포함 (항공사, 수하물 규정, 기간)
- 산출물: `travel/artifacts/01-logistics.md`

### 2단계: 재정 + 짐 (동시 진행)

**[2a] finance-agent subagent:**
- `plan-insurance` Skill: 보험 체크리스트
- `plan-currency` Skill: 환전 가이드
- 산출물: `travel/artifacts/02-finance.md`

**[2b] packing-agent subagent:**
- `01-logistics.md`의 수하물 규정 참조
- `build-packing-list` Skill: 카테고리별 짐 목록 (기내·위탁 구분)
- 산출물: `travel/artifacts/03-packing.md`

### 3단계: 집 정리 + 일정 (home-agent)

home-agent subagent를 사용해서:
- `prepare-home` Skill: Clean state 체크리스트
- `set-schedule` Skill: D-30~D-Day 점검 일정
- 산출물: `travel/artifacts/04-home.md`

### 4단계: 5개 파일 합산

위 4개 artifacts를 읽어 아래 파일들을 생성합니다:

**`travel/checklist.md`** (Feature list — 전체 준비 항목)
**`travel/progress.md`** (Progress file — 현재 완료 현황)
**`travel/handoff-notes.md`** (Handoff — 단계간 인수인계 메모)
**`travel/clean-state.md`** (Clean state — 출발 전 최종 정리)
**`travel/schedule.md`** (D-30~D-Day 전체 일정)

## 파일 기반 산출물

```
travel/
├── artifacts/
│   ├── 01-logistics.md    ← 항공권 + 숙소 체크포인트
│   ├── 02-finance.md      ← 보험 + 환전 가이드
│   ├── 03-packing.md      ← 짐 체크리스트
│   └── 04-home.md         ← Clean state + 일정
├── checklist.md           ← Feature list: 전체 준비 항목
├── progress.md            ← Progress file: 완료 현황
├── handoff-notes.md       ← Handoff: 단계간 인수인계
├── clean-state.md         ← Clean state: 출발 전 최종 정리
└── schedule.md            ← D-30~D-Day 점검 일정
```

## progress.md 형식

```md
# 여행 준비 현황

**목적지:** [목적지]
**출발일:** [YYYY-MM-DD] | **귀국일:** [YYYY-MM-DD]
**마지막 업데이트:** [YYYY-MM-DD]

## 준비 현황

| 항목 | 상태 | 참조 파일 |
|---|---|---|
| 항공권 | ⬜ 미완료 | artifacts/01-logistics.md |
| 숙소 | ⬜ 미완료 | artifacts/01-logistics.md |
| 여행자 보험 | ⬜ 미완료 | artifacts/02-finance.md |
| 환전 | ⬜ 미완료 | artifacts/02-finance.md |
| 짐 준비 | ⬜ 미완료 | artifacts/03-packing.md |
| 집 정리 | ⬜ 미완료 | artifacts/04-home.md |
| 점검 일정 확인 | ✅ 완료 | travel/schedule.md |

> 각 항목을 완료하면 ⬜를 ✅로 바꾸세요.
```

## 실패 처리

- 1단계 결과가 비어 있으면 logistics-agent를 한 번 더 실행합니다.
- 출발까지 7일 미만이면 D-30, D-14 일정을 생략하고 남은 항목을 앞당깁니다.
- 모든 파일 생성 후 → 저장 경로와 다음 행동 3가지를 사용자에게 보고합니다.

## 완료 보고 형식

```
✅ 여행 준비 파일이 완성되었습니다.

📁 저장 위치: travel/

진행 현황: travel/progress.md
전체 체크리스트: travel/checklist.md
출발 전 최종 정리: travel/clean-state.md
점검 일정: travel/schedule.md

지금 바로 할 일:
1. travel/progress.md를 열고 항공권·숙소 예약 시작
2. travel/schedule.md에서 오늘 날짜 확인
3. 각 항목 완료 시 progress.md의 ⬜를 ✅로 업데이트
```
