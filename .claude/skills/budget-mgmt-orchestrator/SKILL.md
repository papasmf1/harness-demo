---
name: budget-mgmt-orchestrator
description: 가족 예산 관리 하네스의 팀장 Skill. 지출 요청을 받아 Guardrail → Approval Loop → Audit Log 순서로 처리하고, 월말 보고서와 Sandbox 시뮬레이션도 조율한다.
triggers:
  - "지출 기록"
  - "지출 승인"
  - "월말 보고서"
  - "시뮬레이션"
  - "budget-mgmt-orchestrator"
---

# 가족 예산 관리 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 모든 지출 요청이 올바른 순서로 검토되고, 빠짐없이 기록되도록 조율합니다.

## 필수 입력 (지출 요청 시)

- 지출 항목 (필수)
- 금액 (필수)
- 카테고리 (없으면 budget-checker가 추론 또는 확인 요청)

## 실행 흐름

### [흐름 A] 지출 요청 처리

```
입력
  │
  ▼
budget-checker (enforce-guardrail → check-budget-limit)
  ├─ BLOCK (금지 항목 또는 한도 초과)
  │    └─ expense-logger (BLOCK 기록) → 완료
  │
  └─ PASS 또는 APPROVE_REQUIRED
       ├─ APPROVE_REQUIRED (50만원 이상)
       │    └─ approval-agent (run-approval-loop)
       │         ├─ APPROVED → expense-logger (APPROVED 기록) → 완료
       │         └─ REJECTED → expense-logger (REJECTED 기록) → 완료
       │
       └─ PASS (50만원 미만, 한도 내)
            └─ expense-logger (PASS 기록) → 완료
```

### [흐름 B] 월말 보고서

- monthly-reviewer (run-monthly-review) → `budget/monthly-report.md`

### [흐름 C] Sandbox 시뮬레이션

- budget-sandbox (run-sandbox) → `budget/sandbox-result.md`
- expense-log.md, monthly-plan.md 변경 없음

## 입력에 따른 흐름 선택

| 입력 내용 | 실행 흐름 |
|---|---|
| "X원 지출 기록" / "Y 샀어" | 흐름 A |
| "월말 보고서" / "이번 달 정리" | 흐름 B |
| "만약에 X 사면" / "시뮬레이션" | 흐름 C |
| "예산 계획 만들어줘" | monthly-plan.md 초안 생성 (단독) |

## 파일 기반 산출물

```
budget/
├── monthly-plan.md      ← 이번 달 카테고리별 예산 한도
├── expense-log.md       ← Audit Log (모든 판정 기록)
├── monthly-report.md    ← 월말 분석 보고서
└── sandbox-result.md    ← 시뮬레이션 결과 (임시)
```

## monthly-plan.md 초기 형식

처음 사용 시 아래 형식으로 생성합니다. 사용자가 금액을 채워 넣습니다:

```md
# 가족 예산 계획

**월:** YYYY년 MM월
**총 예산:** 000만원

## 카테고리별 한도

| 카테고리 | 월 한도 | 비고 |
|---|---|---|
| 식비 | 000,000원 | |
| 교통 | 000,000원 | |
| 의료 | 000,000원 | |
| 교육 | 000,000원 | |
| 저축 | 000,000원 | 자동이체 |
| 카드값 | 000,000원 | 전월 사용분 |
| 기타 | 000,000원 | |

## 금지 항목 (Guardrail)

- 비상금 통장 임의 인출
- 적금·투자 계좌 중도 해지
- 이 파일(monthly-plan.md) 직접 수정

## Permission 규칙

- 50만원 미만: 자동 처리
- 50만원 이상: Approval Loop 발동
```

## 실패 처리

- budget-checker 결과가 비어 있으면 → 한 번 재실행
- expense-logger 저장 실패 → 사용자에게 알리고 수동 기록 요청
- monthly-plan.md 없으면 → 초기 형식 생성 후 사용자에게 금액 입력 요청
