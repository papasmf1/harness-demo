---
name: run-sandbox
description: 실제 예산에 영향 없이 가상 지출 시나리오를 시뮬레이션하고 결과를 budget/sandbox-result.md에 저장하는 작업 매뉴얼
triggers:
  - "시뮬레이션"
  - "만약에"
  - "가상 지출"
  - "Sandbox"
---

# Sandbox 시뮬레이션 작업 매뉴얼

## 절차

1. **입력 읽기**
   - `budget/monthly-plan.md` (카테고리별 한도)
   - `budget/expense-log.md` (현재까지 누적 지출)

2. **현재 잔액 계산**
   - 각 카테고리: 한도 - (PASS + APPROVED 누적)
   - 전체 예산 잔액

3. **가상 지출 적용**
   - 가상 금액을 해당 카테고리에 더한 후 잔액 재계산
   - 음수가 되면 "초과" 표시

4. **Guardrail 시뮬레이션**
   - 금지 항목이면 → "이 지출은 실제 요청 시 즉시 차단됩니다" 표시
   - 50만원 이상이면 → "Approval Loop가 발동됩니다" 표시

5. **결과 저장** — `budget/sandbox-result.md` (덮어쓰기)
   - 파일 상단에 ⚠️ 시뮬레이션 면책 문구 필수

## 절대 금지

- `budget/expense-log.md`에 어떤 행도 추가하지 않는다.
- `budget/monthly-plan.md`를 변경하지 않는다.
- 시뮬레이션 결과를 오케스트레이터에게 "실제 PASS"로 반환하지 않는다.

## 품질 체크

- [ ] ⚠️ 시뮬레이션 면책 문구 상단에 포함
- [ ] expense-log.md 변경 없음
- [ ] monthly-plan.md 변경 없음
- [ ] 카테고리별 현재 잔액과 시뮬레이션 후 잔액 모두 표시
- [ ] 권고 결론 포함 (집행 권장 여부)
