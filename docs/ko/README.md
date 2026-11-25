# RH Lean 검증 아틀라스

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Levent Alpöge의 Lean 개발은 제타 함수의 리만 가설과 제타 함수 또는 디리클레 L함수의 영점에 관한 네 가지 추가 진술을 선언한다. 제3자의 감사 기록은 Lean 커널의 승인을 보고하며, 이 프로젝트는 그 실행을 재현하지 않았다. 서면 유도는 V, F, Green의 유한체 지표 명제, 국소 함의 31개, 보충 입력 S1–S6을 가정한다. S6에는 Mathlib의 고전적 결과가 들어 있다. Lean 원문은 V와 F를 항으로 공급한다. 둘이 각각 지배하는 서로 겹치지 않는 영역은 측정한 코어 줄 수의 47.73%다. 아틀라스는 두 영역의 읽기 지도를 제공하며, 손으로 따라갈 전체 유도는 아직 없다. [MainConclusion.lean:10–11](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L10-L11) · [RowSrc.lean:6–6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean#L6-L6) · [EveryCharacterOfLiteratureOfVWin.lean:810–813](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L810-L813)

이 자료는 AI가 작성하고 AI가 교차검토했다. 사람의 확인은 없으며 리만 가설이 증명됐다는 주장을 하지 않는다. [어디까지 서술됐고, 무엇이 남았고, 내가 무엇을 확인할 수 있나](coverage.md) · [외부 검사](../../sources/kernel-audit.md) · [검증 현황](STATUS.md) · [English](../../README.md)

## 두 문서

Gunhee Cho의 논문 *Toward a human verification of Alpöge's Lean proof of the Riemann hypothesis, I: the conditional chain from Selmer windows to zero-free regions*은 Lean 명제 775개를 정리하고 셀머 창에서 영점 없는 영역까지의 조건부 연역을 개괄한다. 일부 단계는 가정에서 결론까지 자세히 풀어 썼다. 블루프린트는 원래의 입력 20개를 각각의 정의와 보조정리에서부터 설명한다. 아틀라스는 독자가 손으로 한 단계씩 검산할 수 있도록 판본마다 두 문서의 논증을 Lean 선언 및 검토 기록과 연결한다. Gunhee Cho의 지도로 AI가 초고를 쓰고 Lean 원문과 교차 대조했다. 저자를 포함해 아직 이 논증을 확인한 사람은 없다. [논문 v8](../../editions/v0.1.0/paper_v8.pdf) · [The Alpöge formalization of RH and GRH: an informal blueprint (블루프린트 v13c)](../../editions/v0.1.0/blueprint_v13c.pdf) · [판본과 지문](../../data/editions.json)

Levent Alpöge의 Lean 개발에서 관심 있는 명제를 하나 고를 수 있다. 한 명제나 밀접한 명제들을 모은 읽기 항목을 ‘단위’라고 한다. 각 단위에서 가정과 Lean 선언을 확인한다. 서면 논증이 있는 경우 해당 판본도 연결된다. 검토 기록은 어느 글의 어느 주장까지 살폈는지 명시한다. 외부 커널 검사는 컴파일한 Lean 개발에 관한 기록이다. [진척](../../PROGRESS.md) · [읽기 대기열](../../ROADMAP.md) · [기여자](../../AUTHORS.md)

> **서술과 검토 현황** · [검증 범위](STATUS.md) · [진척 추이](../../PROGRESS.md)  
> 전체 217개 단위 중 명시한 가정 아래 전체 논증이 있는 단위는 55개, 개요는 127개, 명제만 있는 단위는 35개다.  
> AI의 서면 논증 검토를 근거로 L2 등급을 받은 단위는 24개다. 현 판본의 739단계 중 6단계에 그 추론을 특정한 AI 검토 기록이 있다.  
> 실명 독자가 확인한 단계는 0개다. 모든 단계와 명제 대조의 실명 확인이 갖춰진 단위는 0개다. [읽기 대기열](../../ROADMAP.md)

## 목적에 따라 시작하기

| 찾는 내용 | 첫 페이지 |
|---|---|
| 처음 오셨나요? | [논증의 전체 흐름을 먼저 읽기](proof-at-a-glance.md) |
| Lean이 진술하는 내용과 확인 범위 | [검증 현황](STATUS.md) · [수학적 개요](OVERVIEW.md) · [자주 묻는 질문](FAQ.md) |
| 두 핵심 입력의 가정과 점검 순서 | [V · 셀머 창](pillars/V.md) · [F · 정부호 측 증인](pillars/F.md) · [쪽수별 읽기 순서](../reading-orders.md) |
| 내 분야의 명제와 열린 질문 | [해석적 수론](analytic.md) · [Arakelov 기하·수의 기하](arakelov.md) · [세타 대응·유니타리 군의 보형 표현](theta.md) · [갈루아 표현·보형성 올림·Iwasawa 이론과 오일러 계](galois.md) · [국소 p진 이론](local.md) · [대수적 K이론·산술군 코호몰로지](ktheory.md) · [형식화·재현](formal.md) |
| 선수지식에 맞는 대학원 수준 읽기 | [분야별 6–8쪽 발췌](../../notes/README.md) · [한쪽 소수합 창부터 읽기](../../notes/analytic/README.md) |
| 가지고 있는 Lean 선언 찾기 | [선언 조회](../../lookup/declarations.md) · [용어집](../../lookup/glossary.md) |
| 공개된 다른 프로젝트와 비교하기 | [공개 자료 안내](../../LANDSCAPE.md) · [자료 간 대응표](../../crosswalk/README.md) |
| 문제를 남기거나 검토 결과를 기록하기 | [기여 안내](../../CONTRIBUTING.md) · [실명 검토 양식](signoffs/README.md) |

[증명 지도](../../MAP.md)에서 목표와 입력을 세 배율로 볼 수 있다. [분야별 현황](../../dashboard/README.md)에서는 서술 상태와 등급별로 단위를 찾을 수 있다.

내려받은 사본에서는 `site/index.html`을 열면 된다. 선언 검색과 도표는 로컬 파일에서 작동한다.

## 일곱 분야

| 분야 | 처음 확인할 질문 | 시작 단위 |
|---|---|---|
| [해석적 수론](analytic.md) | 어떤 창 부등식이 극을 배제하는가? | [P022](../../units/P022.md) |
| [Arakelov 기하·수의 기하](arakelov.md) | 공변부피에 판별식이 어디서 들어가는가? | [P049](../../units/P049.md) |
| [세타 대응·유니타리 군의 보형 표현](theta.md) | Fock 모형에서 어느 격자들이 서로 쌍대인가? | [Z4.4](../../units/Z4.4.md) |
| [갈루아 표현·보형성 올림·Iwasawa 이론과 오일러 계](galois.md) | 두 Selmer 길이 상계를 어떻게 합치는가? | [P020](../../units/P020.md) |
| [국소 p진 이론](local.md) | 비분해 소수의 표 한 행에 어떤 부등식이 쓰이는가? | [P045](../../units/P045.md) |
| [대수적 K이론·산술군 코호몰로지](ktheory.md) | 유한 개수 상계에서 지수 손실이 어디서 생기는가? | [P036](../../units/P036.md) |
| [형식화·재현](formal.md) | 공개 선언의 동일성을 어떻게 확인하는가? | [P001](../../units/P001.md) |

## 근거 등급

| 최고 기록 등급 | 확인할 근거 | 단위 수 |
|---|---|---:|
| L0 | 선언의 판본과 위치 고정. 이 단위 자체의 검토 없음 | 138 |
| L1 | 명제 및 가정과 Lean 원문의 대조 | 55 |
| L2 | 명시한 가정 아래 작성된 논증의 AI 교차검토 | 24 |
| L3 | 독립 자료 둘 이상의 일치 기록 | 0 |
| L4 | Full 단위에서 입력 호출 외의 실제 추론이 있고 모든 단계와 별도 명제 대조가 실명 확인됨 | 0 |

Full은 명시된 가정에서 논증을 끝까지 썼다는 뜻이다. Outlined는 중간 추론을 보충해야 하는 개요이며, Statement only는 명제와 출처만 있는 경우다. 검토 등급은 해당 단위를 뒷받침하는 근거를 나타낸다. AI 검토, 독립 자료 대조, 실명 검토는 따로 센다. 등급은 누적 요건이 아니다. L4는 해당 판본의 국소 논증과 명시된 가정만 대상으로 하며 V·F 또는 리만 가설 전체를 확인하지 않는다. 각 L4에는 독자 수, 유지관리자 참여 여부와 신고한 AI 도움 수준을 함께 표시한다. 상당한 AI 도움을 받은 검토는 독립적인 사람의 검토로 세지 않는다. 이의는 유지관리자가 아닌 두 번째 독자의 검토 또는 해당 대상을 대체한 본문 개정으로 해소할 수 있다. 이름은 본인 기재이며 신원을 검증하지 않는다. [검토 근거](../../reviews/README.md) · [실명 확인 규칙](signoffs/README.md)

## 아틀라스 관리자

Gunhee Cho가 아틀라스를 관리합니다. 소속은 Texas State University 수학과(`wvx17@txstate.edu`)와 TranscendQ(`geonhee@transcendq.com`)입니다.
견해와 오류에 대한 책임은 저자에게 있습니다. [저자와 배경 문헌](../../AUTHORS.md)

저자는 [EnjoyingMath](https://www.youtube.com/@enjoyingmath9346) 채널 커뮤니티에서 이어지는 토론을 바탕으로, 수학 전공 학생과 수학자들과 함께 Alpöge의 Lean 증명을 한 단계씩 손으로 확인하고자 합니다. 얼마나 오래 걸리더라도 이 작업을 이어 가는 것이 목표입니다. 검증이 어디까지 진행됐는지는 아틀라스의 각 판본과 진행 현황 페이지, 채널을 통해 영어와 한국어로 공개할 계획입니다. 현재 아틀라스에 기록된 사람의 확인은 0건입니다. [진행 현황](../../PROGRESS.md)

## 인용

Gunhee Cho (maintainer), *RH Lean Verification Atlas*, v0.1.0, 2026년 11월 25일. AI-drafted; maintained by Gunhee Cho. 정확한 아틀라스 커밋, 단위 ID, Lean 선언 이름을 함께 적는다. 특정 해설을 사용했다면 판과 쪽수도 기록한다. 릴리스 공개 후 Zenodo가 DOI를 발급하면 여기에 표시한다. [인용 메타데이터](../../CITATION.cff) · [판본 지문](../../data/editions.json) · [릴리스 안내](../../RELEASE_NOTES_v0.1.0.md)

## 검토 기여

한 단위와 판본을 고르고 실제로 읽은 논증의 범위, 판정과 유보 사항을 기록한다. 부분 검토, 반례, 해결하지 못한 질문도 남길 수 있다. [기여 안내](../../CONTRIBUTING.md) · [열린 질문](../../questions/README.md)

## 라이선스

AI 생성 텍스트에 저작권이 성립하는 범위에 한해 저작권 © 2026 Gunhee Cho. 아틀라스의 자체 글과 데이터에는 CC BY 4.0이, 자체 스크립트와 워크플로 코드에는 MIT 라이선스가 적용된다. Lean 원문에서 유래한 내용과 제3자 자료는 자체 라이선스 부여 범위에서 제외한다. 고정 저장소의 라이선스 조사 결과는 출처 장부에 적었다. [Lean 라이선스 조사](../../sources/README.md) · [적용 범위](../../LICENSE) · [MIT 라이선스](../../LICENSE-MIT) · [외부 자료 고지](../../NOTICE.md)
