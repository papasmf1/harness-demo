---
name: finalize-party-plan
description: 4개 artifacts를 읽어 party/plan.md, party/checklist.md, party/budget.md 3개 파일로 최종 파티 계획서를 완성하는 작업 매뉴얼
triggers:
  - "파티 계획 완성"
  - "최종 계획서 생성"
  - "파티 파일 합산"
output:
  - party/plan.md
  - party/checklist.md
  - party/budget.md
---

# 최종 편집 작업 매뉴얼

## 절차

1. **입력 읽기 (4개 파일 전부)**
   - `party/artifacts/01-ideas.md`
   - `party/artifacts/02-evaluation.md` (WARN 항목 기록)
   - `party/artifacts/03-venue-food.md`
   - `party/artifacts/04-guest-list.md`

2. **`party/plan.md` 작성 — 메인 파티 계획서**
   - 파티 기본 정보 (날짜, 장소, 테마, 예산)
   - 파티 개요 (테마, 분위기, 핵심 콘셉트)
   - 타임라인 (도착~마무리까지 30분 단위)
   - 장소·음식 요약
   - 초대 인원 요약 (이름 대신 총 인원 수만)
   - 준비 D-Day 일정 (D-14~D-Day)
   - WARN 항목이 있으면 하단에 "주의 사항" 섹션 추가

3. **`party/checklist.md` 작성 — 준비 체크리스트**
   - D-14, D-7, D-3, D-1, D-Day 섹션으로 나눔
   - 각 섹션에 구체적 할 일 목록 (체크박스 형식)
   - 담당자 칸 추가 (엄마, 아빠, 기타)

4. **`party/budget.md` 작성 — 예산 요약**
   - 항목별 예상 비용 표
   - 총계 vs 예산 상한 비교
   - 실제 비용 입력 칸 (초기값 비워둠)
   - 잔액 또는 초과액 표시

5. **저장 확인**
   - 3개 파일 모두 저장 완료 확인

## 품질 체크

- [ ] plan.md에 타임라인 포함
- [ ] checklist.md에 D-14~D-Day 전 기간 포함
- [ ] budget.md에 모든 비용 항목 포함
- [ ] WARN 항목이 plan.md에 명시됨
- [ ] 부모가 입력하지 않은 정보는 [미정] 또는 빈칸 처리
