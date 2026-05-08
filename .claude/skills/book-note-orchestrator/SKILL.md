---
name: book-note-orchestrator
description: 책 제목과 독서 메모를 받아 요약, 인용, 질문, 실천 항목, 다음 책 추천을 순서대로 완성하고 하나의 독서 노트 파일로 저장합니다. 독서 노트를 처음부터 끝까지 정리할 때 사용합니다.
---

# 독서 노트 오케스트레이터

## 목적

이 Skill은 팀장 역할입니다. 4명의 팀원(book-analyst, question-maker, action-planner, book-recommender)이 순서대로 일하도록 조율하고, 각 결과를 하나의 독서 노트로 엮습니다.

## 입력

- 책 제목 (필수)
- 저자 (있으면 포함)
- 사용자가 읽으면서 남긴 메모 또는 인상 깊었던 내용 설명

## 입력 확인

시작 전에 반드시 확인합니다:
- 책 제목이 없으면 → 책 이름을 먼저 물어봅니다.
- 내용 설명이 한 줄 미만이면 → "어떤 내용이 인상 깊었나요? 기억나는 것 3가지만 말해주세요." 질문합니다.
- 충분하면 바로 1단계로 넘어갑니다.

## 실행 흐름

### 1단계: 분석 (book-analyst)

book-analyst subagent를 사용해서 아래 두 작업을 수행합니다:
- `summarize-book` Skill에 따라 핵심 요약 작성
- `extract-quotes` Skill에 따라 인용 추출
- 결과를 `artifacts/01-summary.md`에 저장

### 2단계: 질문 (question-maker)

question-maker subagent를 사용해서:
- `artifacts/01-summary.md`를 읽고
- `generate-questions` Skill에 따라 질문 3-5개 작성
- 결과를 `artifacts/02-questions.md`에 저장

### 3단계: 실천 (action-planner)

action-planner subagent를 사용해서:
- `artifacts/01-summary.md`와 `artifacts/02-questions.md`를 읽고
- `plan-actions` Skill에 따라 실천 항목 3개 이하 작성
- 결과를 `artifacts/03-actions.md`에 저장

### 4단계: 추천 (book-recommender)

book-recommender subagent를 사용해서:
- `artifacts/01-summary.md`를 읽고
- `recommend-next` Skill에 따라 다음 읽을 책 2-3권 추천
- 결과를 `artifacts/04-recommendations.md`에 저장

### 5단계: 최종 노트 합산

위 4개 파일을 읽어서 아래 형식으로 `books/YYYY-MM-DD_책제목.md`에 저장합니다.

## 최종 노트 형식

```md
# 독서 노트: [책 제목]

**저자:** [저자명]
**읽은 날짜:** [YYYY-MM-DD]

---

## 핵심 요약

**한 줄 요약:** [한 문장 요약]

[요약 본문]

---

## 인상적인 인용

[인용 목록]

---

## 내가 가진 질문

[질문 목록]

---

## 실천 항목

[실천 항목 체크리스트]

---

## 다음에 읽을 책

[추천 책 목록]
```

## 파일 기반 산출물

- `artifacts/01-summary.md` — 요약 + 인용
- `artifacts/02-questions.md` — 질문 목록
- `artifacts/03-actions.md` — 실천 항목
- `artifacts/04-recommendations.md` — 다음 책 추천
- `books/YYYY-MM-DD_책제목.md` — 최종 독서 노트

## 실패 처리

- 1단계 결과가 비어 있으면 → 입력 내용을 다시 확인하고 book-analyst를 한 번 더 실행합니다.
- 실천 항목이 모호하면 → action-planner를 다시 호출하고 구체화를 요청합니다.
- 5단계 파일 저장 후 → 파일 경로와 핵심 내용 3줄을 사용자에게 보고합니다.

## 완료 보고 형식

```
✅ 독서 노트가 완성되었습니다.

📄 저장 위치: books/YYYY-MM-DD_책제목.md

핵심 요약: [한 줄 요약]
실천 항목: [첫 번째 실천 항목]
다음 책: [첫 번째 추천 책]
```
