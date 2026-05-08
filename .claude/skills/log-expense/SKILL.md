---
name: log-expense
description: 지출 판정 결과(PASS/BLOCK/APPROVED/REJECTED)를 날짜·금액·이유와 함께 budget/expense-log.md에 추가하는 Audit Log 작업 매뉴얼
triggers:
  - "지출 기록"
  - "Audit Log 추가"
---

# Audit Log 기록 작업 매뉴얼

## 절차

1. **파일 존재 확인**
   - `budget/expense-log.md` 없으면 → 헤더 포함 새 파일 생성
   - 있으면 → 마지막 행 아래에 추가

2. **새 파일 헤더 형식**
   ```md
   # 지출 Audit Log

   **월:** YYYY년 MM월
   **마지막 업데이트:** YYYY-MM-DD

   | 날짜 | 항목 | 금액 | 결과 | 사유 |
   |---|---|---|---|---|
   ```

3. **행 추가 형식**
   ```
   | YYYY-MM-DD | [항목명] | [금액]원 | PASS/BLOCK/APPROVED/REJECTED | [사유] |
   ```

4. **결과 코드 기준**
   - `PASS` — budget-checker 자동 통과
   - `BLOCK` — Guardrail 또는 한도 초과 차단
   - `APPROVED` — approval-agent 승인
   - `REJECTED` — approval-agent 거부 또는 사용자 취소

5. **"마지막 업데이트" 날짜 갱신**

## 품질 체크

- [ ] 기존 행 수정·삭제 없음 (추가만 가능)
- [ ] 결과 코드가 4가지 중 하나
- [ ] 사유 칸이 비어 있지 않음 (PASS면 "한도 내 자동 통과"로 기재)
- [ ] 날짜 형식 YYYY-MM-DD 유지
