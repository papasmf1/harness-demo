# harness-practice — 하네스 실습 프로젝트

이 프로젝트에는 일곱 가지 하네스가 들어 있습니다.

---

## 1. 독서 노트 정리 하네스

책 한 권을 읽은 뒤 핵심 요약, 인용, 질문, 실천 항목, 다음 읽을 책을 하나의 노트 파일로 정리합니다.

### 실행 방법

```
/book-note-orchestrator 아토믹 해빗을 읽었어. 습관을 작게 쪼개야 한다는 게 핵심이고 정체성 기반 습관이 인상 깊었어.
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/book-analyst.md` | 요약 + 인용 추출 |
| `.claude/agents/question-maker.md` | 깊은 질문 생성 |
| `.claude/agents/action-planner.md` | 실천 항목 작성 |
| `.claude/agents/book-recommender.md` | 다음 책 추천 |

### 작업 매뉴얼 (Skill)

`.claude/skills/book-note-orchestrator/` — 전체 순서 관리
`.claude/skills/summarize-book/` · `extract-quotes/` · `generate-questions/` · `plan-actions/` · `recommend-next/`

### 결과물

- 최종 독서 노트: `books/YYYY-MM-DD_책제목.md`
- 중간 작업: `artifacts/`

---

## 2. 장기 여행 준비 하네스

2주 해외여행 준비를 항공권·숙소·보험·환전·짐·집 비우기·점검 일정으로 나눠 5개 파일로 정리합니다.

### 실행 방법

```
/travel-prep-orchestrator 출발지: 서울, 목적지: 스페인 바르셀로나, 출발일: 2026-06-20, 귀국일: 2026-07-04, 예산: 300만원
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/logistics-agent.md` | 항공권 + 숙소 체크포인트 |
| `.claude/agents/finance-agent.md` | 보험 + 환전 계획 |
| `.claude/agents/packing-agent.md` | 짐 목록 (기내·위탁 구분) |
| `.claude/agents/home-agent.md` | 집 비우기 + 점검 일정 |

### 작업 매뉴얼 (Skill)

`.claude/skills/travel-prep-orchestrator/` — 전체 순서 관리
`.claude/skills/research-flights/` · `check-accommodation/` · `plan-insurance/` · `plan-currency/` · `build-packing-list/` · `prepare-home/` · `set-schedule/`

### 결과물

```
travel/
├── artifacts/          ← 중간 작업 파일
├── checklist.md        ← Feature list: 전체 준비 항목
├── progress.md         ← Progress file: 완료 현황
├── handoff-notes.md    ← Handoff: 단계간 인수인계
├── clean-state.md      ← Clean state: 출발 전 최종 정리
└── schedule.md         ← D-30~D-Day 점검 일정
```

---

## 3. 생일파티 기획 하네스

아이 나이·예산·테마·초대 인원을 받아 아이디어 생성 → Rubric 평가 → Feedback Loop → 장소·음식·명단 → 최종 계획서 3개 파일로 완성합니다.

### 실행 방법

```
/party-plan-orchestrator 아이 나이: 6세, 예산: 30만원, 테마: 공룡, 초대 인원: 15명
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/idea-generator.md` | 파티 아이디어 초안 3가지 생성 |
| `.claude/agents/budget-evaluator.md` | Rubric 5개 기준으로 채점 + Feedback Loop |
| `.claude/agents/venue-food-planner.md` | 장소·음식 구체화 |
| `.claude/agents/guest-list-reviewer.md` | 초대 명단 점검 |
| `.claude/agents/final-editor.md` | 3개 최종 파일 완성 |

### 작업 매뉴얼 (Skill)

`.claude/skills/party-plan-orchestrator/` — 전체 순서 + Feedback Loop 관리
`.claude/skills/generate-party-ideas/` · `evaluate-budget/` · `plan-venue-food/` · `review-guest-list/` · `finalize-party-plan/`

### 결과물

```
party/
├── artifacts/             ← 중간 작업 파일
├── plan.md                ← 메인 파티 계획서
├── checklist.md           ← 준비 체크리스트 (D-14~D-Day)
└── budget.md              ← 예산 요약
```

---

## 4. 가족 예산 관리 하네스

지출 요청을 받아 Guardrail(자동 차단) → Approval Loop(큰 지출 승인) → Audit Log(전체 기록)로 처리하고, 월말 보고서와 Sandbox 시뮬레이션을 제공합니다.

### 실행 방법

```
/budget-mgmt-orchestrator 식비 35,000원 지출 기록해줘.
/budget-mgmt-orchestrator 냉장고 교체 비용 85만원 지출 승인 요청.
/budget-mgmt-orchestrator 5월 월말 보고서 만들어줘.
/budget-mgmt-orchestrator 에어컨 수리 45만원 사면 예산 어떻게 되는지 시뮬레이션해줘.
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/budget-checker.md` | Guardrail — 금지 항목 차단 + 한도 확인 |
| `.claude/agents/approval-agent.md` | Approval Loop — 50만원 이상 지출 승인 처리 |
| `.claude/agents/expense-logger.md` | Audit Log — 모든 판정 기록 |
| `.claude/agents/monthly-reviewer.md` | 월말 점검 — 집계 + 보고서 + 다음 달 제안 |
| `.claude/agents/budget-sandbox.md` | Sandbox — 실제 영향 없이 시뮬레이션 |

### 작업 매뉴얼 (Skill)

`.claude/skills/budget-mgmt-orchestrator/` — 전체 흐름 조율
`.claude/skills/check-budget-limit/` · `enforce-guardrail/` · `run-approval-loop/` · `log-expense/` · `run-monthly-review/` · `run-sandbox/`

### 결과물

```
budget/
├── monthly-plan.md      ← 이번 달 카테고리별 예산 한도
├── expense-log.md       ← Audit Log (모든 판정 기록)
├── monthly-report.md    ← 월말 분석 보고서
└── sandbox-result.md    ← 시뮬레이션 결과 (임시)
```

---

## 5. 주말 행사 준비 하네스

가족 또는 동네 주말 행사를 기본 규칙·준비물·역할 분담·일정·안전 점검·회고 순서로 나눠 종합 계획서와 안전 체크리스트로 완성합니다. 행사 후에는 별도로 회고록을 추가할 수 있습니다.

### 실행 방법

```
/event-prep-orchestrator 행사: 동네 바베큐 파티, 날짜: 5월 31일 토요일 오후 4시, 장소: 아파트 옥상, 예상 인원: 20명

# 행사 후 회고
/event-prep-orchestrator 회고: 음식이 부족했고 게임 준비가 늦었어. 날씨는 좋았고 아이들 반응은 좋았어.
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/rule-writer.md` | 기본 규칙 정리 |
| `.claude/agents/supply-planner.md` | 카테고리별 준비물 목록 |
| `.claude/agents/role-assigner.md` | 역할 분담표 작성 |
| `.claude/agents/schedule-builder.md` | 당일 타임라인 |
| `.claude/agents/safety-inspector.md` | 안전 점검 체크리스트 |
| `.claude/agents/event-retrospector.md` | 행사 후 회고록 |

### 작업 매뉴얼 (Skill)

`.claude/skills/event-prep-orchestrator/` — 전체 순서 + Fan-out 관리
`.claude/skills/write-event-rules/` · `plan-event-supplies/` · `assign-event-roles/` · `build-event-schedule/` · `inspect-safety/` · `write-retrospect/`

### 결과물

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

---

## 6. 새 취미 시작 계획 하네스

취미 이름·예산·기간을 받아 목표 설정 → 학습 방식 → 장비 구매(예산 Guardrail) → 연습 루틴 → 종합 계획서로 완성합니다. 매달 진도 점검도 별도로 실행할 수 있습니다.

### 실행 방법

```
/hobby-plan-orchestrator 취미: 기타, 기간: 6개월, 예산: 30만원, 목표: 좋아하는 팝송 1곡 연주

# 매달 진도 점검
/hobby-plan-orchestrator 점검: 1달째. 코드 C·G·Am 익혔는데 F가 안 잡혀. 연습은 주 3회 함.
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/goal-setter.md` | SMART 목표 문서 작성 |
| `.claude/agents/method-picker.md` | 독학·학원·온라인 방식 비교 + 추천 |
| `.claude/agents/gear-advisor.md` | 장비 목록 + 총 예상 비용 |
| `.claude/agents/hobby-budget-guard.md` | 예산 Guardrail (PASS/BLOCK 판정) |
| `.claude/agents/routine-builder.md` | 주간 루틴 + 월간 마일스톤 |
| `.claude/agents/progress-checker.md` | 월간 진도 점검 보고서 |

### 작업 매뉴얼 (Skill)

`.claude/skills/hobby-plan-orchestrator/` — 전체 순서 + Guardrail Loop 관리
`.claude/skills/set-hobby-goal/` · `pick-learning-method/` · `research-gear/` · `check-hobby-budget/` · `build-practice-routine/` · `check-hobby-progress/`

### 결과물

```
hobby/
├── artifacts/
│   ├── 01-goal.md       ← SMART 목표 문서
│   ├── 02-method.md     ← 학습 방식 비교 + 추천
│   ├── 03-gear.md       ← 장비 목록 + 예산 판정
│   └── 04-routine.md    ← 주간 루틴 + 마일스톤
├── plan.md              ← 종합 취미 시작 계획서
└── progress.md          ← 월간 진도 점검 보고서 (누적)
```

---

## 7. 아침 루틴 개선 하네스

아침 60분을 전날 준비·알람·옷 가방·식사·출발 시간 역산으로 나눠 종합 계획서로 완성합니다. 실패할 때마다 기록하면 Feedback Loop로 루틴이 점점 개선됩니다.

### 실행 방법

```
# 처음 설정
/morning-routine-orchestrator 설정: 출근, 기상 6:30, 출근 9:00, 지하철 30분

# 실패했을 때 기록 (루틴 개선 Feedback Loop)
/morning-routine-orchestrator 기록: 오늘 아침 옷 못 찾아서 10분 지각했어
```

### 팀원 (Agent)

| 파일 | 역할 |
|---|---|
| `.claude/agents/morning-planner.md` | Environment Audit 체크리스트 + progress.md 반영 |
| `.claude/agents/alarm-advisor.md` | 최적 기상 시간 + 알람 전략 |
| `.claude/agents/outfit-checker.md` | 전날 준비할 옷·가방 체크리스트 |
| `.claude/agents/breakfast-preparer.md` | 15분 이내 식사 계획 + 사전 준비 |
| `.claude/agents/departure-timer.md` | 출발 시간 역산 + 분 단위 타임라인 |
| `.claude/agents/failure-analyst.md` | 실패 원인 분류 → progress.md 누적 |

### 작업 매뉴얼 (Skill)

`.claude/skills/morning-routine-orchestrator/` — 전체 순서 + Feedback Loop 관리
`.claude/skills/plan-evening-prep/` · `set-alarm-plan/` · `check-outfit-bag/` · `plan-breakfast/` · `plan-departure/` · `log-morning-failure/`

### 결과물

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

---

## 전체 폴더 구조

```
harness-practice/
├── CLAUDE.md                          ← 이 파일 (프로젝트 안내판)
├── books/                             ← 독서 노트 저장
├── artifacts/                         ← 독서 하네스 중간 파일
├── travel/                            ← 여행 하네스 파일
│   └── artifacts/                     ← 여행 하네스 중간 파일
├── party/                             ← 파티 하네스 파일
│   └── artifacts/                     ← 파티 하네스 중간 파일
├── budget/                            ← 예산 하네스 파일
├── event/                             ← 행사 하네스 파일
│   └── artifacts/                     ← 행사 하네스 중간 파일
├── hobby/                             ← 취미 하네스 파일
│   └── artifacts/                     ← 취미 하네스 중간 파일
├── morning/                           ← 아침 루틴 하네스 파일
│   └── artifacts/                     ← 아침 루틴 하네스 중간 파일
└── .claude/
    ├── agents/                        ← 팀원 카드 31개
    ├── settings.json                  ← Hook + Permission
    └── skills/                        ← 작업 매뉴얼 40개
```

## 테스트 프롬프트

**독서 노트 — 정상:**
```
/book-note-orchestrator 아토믹 해빗을 읽었어. 습관을 작게 쪼개야 한다는 게 핵심이고 정체성 기반 습관이 인상 깊었어.
```

**여행 준비 — 정상:**
```
/travel-prep-orchestrator 출발지: 서울, 목적지: 바르셀로나, 출발일: 2026-06-20, 귀국일: 2026-07-04
```

**여행 준비 — 애매함 (추가 질문이 돌아옵니다):**
```
/travel-prep-orchestrator 여름에 유럽 가려고 하는데 준비해줘.
```

**생일파티 — 정상:**
```
/party-plan-orchestrator 아이 나이: 6세, 예산: 30만원, 테마: 공룡, 초대 인원: 15명
```

**생일파티 — Feedback Loop 발동 (예산 초과 시 재시도됩니다):**
```
/party-plan-orchestrator 아이 나이: 5세, 예산: 10만원, 테마: 디즈니 공주, 초대 인원: 30명
```

**생일파티 — 애매함 (추가 질문이 돌아옵니다):**
```
/party-plan-orchestrator 아이 생일파티 계획해줘.
```

**가족 예산 — 정상 (한도 내 지출):**
```
/budget-mgmt-orchestrator 식비 35,000원 지출 기록해줘.
```

**가족 예산 — Approval Loop 발동 (큰 지출):**
```
/budget-mgmt-orchestrator 냉장고 교체 비용 85만원 지출 승인 요청.
```

**가족 예산 — Guardrail 발동 (금지 항목):**
```
/budget-mgmt-orchestrator 비상금 통장에서 여행 경비 50만원 인출할게.
```

**가족 예산 — Sandbox 시뮬레이션:**
```
/budget-mgmt-orchestrator 이번 달에 에어컨 수리 45만원 추가되면 예산이 어떻게 되나 시뮬레이션해줘.
```

**가족 예산 — 월말 보고서:**
```
/budget-mgmt-orchestrator 5월 월말 보고서 만들어줘.
```

**주말 행사 — 정상:**
```
/event-prep-orchestrator 행사: 동네 바베큐 파티, 날짜: 5월 31일 토요일 오후 4시, 장소: 아파트 옥상, 예상 인원: 20명
```

**주말 행사 — 애매함 (추가 질문이 돌아옵니다):**
```
/event-prep-orchestrator 주말에 동네 행사 하려는데 준비해줘.
```

**주말 행사 — 어려운 사례 (조건 충돌):**
```
/event-prep-orchestrator 행사: 학부모 운동회, 인원: 100명, 예산: 0원, 장소: 미정
```

**주말 행사 — 행사 후 회고:**
```
/event-prep-orchestrator 회고: 음식이 부족했고 게임 준비가 늦었어. 날씨는 좋았고 아이들 반응은 정말 좋았어.
```

**취미 시작 — 정상:**
```
/hobby-plan-orchestrator 취미: 기타, 기간: 6개월, 예산: 30만원, 목표: 좋아하는 팝송 1곡 연주
```

**취미 시작 — Guardrail 발동 (예산 초과):**
```
/hobby-plan-orchestrator 취미: 기타, 예산: 10만원, 목표: 무대에서 공연하기
```

**취미 시작 — 애매함 (추가 질문이 돌아옵니다):**
```
/hobby-plan-orchestrator 기타 배우고 싶어
```

**취미 시작 — 월간 진도 점검:**
```
/hobby-plan-orchestrator 점검: 1달째. 코드 C·G·Am 익혔는데 F가 안 잡혀. 연습은 주 3회 함.
```

**아침 루틴 — 설정 (정상):**
```
/morning-routine-orchestrator 설정: 출근, 기상 6:30, 출근 9:00, 지하철 30분
```

**아침 루틴 — 기록 (Feedback Loop 발동):**
```
/morning-routine-orchestrator 기록: 오늘 아침 옷 못 찾아서 10분 지각했어
```

**아침 루틴 — 설정 재실행 (progress.md 반영 확인):**
```
/morning-routine-orchestrator 설정: 출근, 기상 6:30, 출근 9:00, 지하철 30분
```

**아침 루틴 — 애매함 (추가 질문이 돌아옵니다):**
```
/morning-routine-orchestrator 설정: 등교
```
