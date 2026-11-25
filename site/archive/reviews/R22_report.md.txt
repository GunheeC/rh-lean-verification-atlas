AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R22_report

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R22_report.md`
- SHA-256: `a7339fb4da23c10a011673bc9cb67ad574c319d59be8c201b242118774962090`
- Report scope: 22라운드 · 본 논문 v2

## Archived report · [English summary](../../reviews/R22_report.md)

The report below preserves its original verdict, scope and unresolved points. Source line numbers in other records count from its original title.

# 22라운드 · 본 논문 v2

원고 main.pdf (`main.pdf`)는 영어 316쪽이다. 원래 Lean only였던 32개 머리를 지배 줄 수가 큰 순서로 열었다. 각 머리에서 첫 분할 5–12개, 합계 237개 위치(서로 다른 선언 232개)를 확인했다. 추가 재분할과 공통 공급자를 포함한 이번 원장은 623개다. 기존 번호 40개를 재사용하고 583개를 추가해 전체 명제 수는 **192 → 775**가 되었다. 새 손증명은 0건이다.

## 처분과 남은 분량

줄 수의 단위는 원문 선언마다 매긴 포함 구간 길이이다. 같은 선언은 원래 32개 영역 중 한 곳에서만 센다. 명제의 처분과 그 명제가 호출하는 대규모 공통 자료의 증명 상태를 구별했다.

| 처분 | 전체 명제 | 잎 | 잎의 중복 제거 줄 | 작은 내부 잔여 줄 |
|---|---:|---:|---:|---:|
| Cited | 1 | 1 | 0 | 0 |
| Related reference | 81 | 78 | 399,439 | 57,830 |
| Project-specific | 361 | 334 | 1,824,594 | 602,136 |
| Routine assembly | 180 | 112 | 812,825 | 581,773 |
| **합계** | **623** | **525** | **3,036,858** | **1,241,739** |

별도 미분해 잔여 2,193,528줄을 더하면 원래의 **6,472,125줄**과 정확히 일치한다. 525개 잎의 최대 배정량은 D160의 **47,940줄**이다. 내부 머리의 로컬 증명이 단순 조립이어도 공통 선행 자료의 내용에는 같은 처분을 일괄 부여하지 않았다. D311은 Lan의 명제 3.3.1.5와 가정·결론을 대조한 인용 잎이다. 문헌 경계에서 그래프가 멈추므로 배정된 코어 줄 수는 0이다. Project-specific 334개 전부의 크기순 목록은 PDF §10.1, 검색어·대조 문헌·근거는 부록 G와 명제 원장 (`R22_decomposition.json`)에 있다.

## 5만 줄 경계

중복 제거 배정량이 5만 줄을 초과하는 말단 명제는 0개다. 다음 네 곳에서는 한 정리의 배타적 지배 영역으로 쪼갤 수 없는 공통 자료가 5만 줄 이상 남았다. 하한은 현재 컷 안에서 임의 정점 12개를 더 골라도 남을 최소 분량이다. 네 곳의 선언 전부에 대한 이름공간 소속은 주제별 원장 (`R22_shared_subjects.json`)에 있다. 각 묶음과 주요 주제는 PDF 부록 G.37에 실었다.

| 원래 영역 · 내부 머리 | 잔여 줄 | 직접 공급자 둘 이상에서 도달 | 컷 12개 추가 후 하한 | 읽기 묶음 | 최대 묶음 |
|---|---:|---:|---:|---:|---:|
| T02 | 1,498,006 | 1,497,270 | 1,386,072 | 35 | 50,000 |
| T01 | 381,435 | 380,596 | 338,275 | 13 | 49,751 |
| W01 · D071 | 203,531 | 202,951 | 180,913 | 6 | 49,995 |
| T03 | 110,556 | 108,833 | 93,243 | 3 | 49,926 |

네 영역의 양의 가중치 선언 **177,214개**를 이름공간 항목 **14,866개**에 연결한 뒤 **57개** 읽기 묶음에 중복 없이 배정했다. 최대 묶음은 50,000줄이다. 이 묶음에는 독립 정리나 인용 판정을 붙이지 않았다. 외부 기존 Related 경계의 공제 전 지배량으로는 W07 145,398, T11 97,419, B03 93,354, T09 64,874줄이며 이들에 대한 이번 32개 영역의 배정은 각각 0줄이다.

## Project-specific 잎 상위 20개

| 순위 | 번호 | Lean 선언 | 중복 제거 줄 |
|---:|---|---|---:|
| 1 | D160 | `GlobalTheory.T.exists_quasiProjective_harrisTaylor_family` | 47,940 |
| 2 | D395 | `GlobalTheory.goodPrime_packages` | 46,421 |
| 3 | D073 | `UpperTheory.V.Z.Sym.W.specOutS` | 45,473 |
| 4 | D397 | `GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt` | 45,114 |
| 5 | D398 | `GlobalTheory.RunPrimeData.exists_primeData_heights` | 44,822 |
| 6 | D467 | `GlobalTheory.Fam.colSide_alt` | 43,853 |
| 7 | D314 | `GlobalTheory.T.model_on_hodge_from_family` | 43,746 |
| 8 | D378 | `GlobalTheory.Fc.six_rows_at_member_alt` | 43,648 |
| 9 | D379 | `GlobalTheory.CountConstants.count_constants_of_siegelWeil` | 40,441 |
| 10 | D412 | `GlobalTheory.Mem.SRe.UpS.has4_of_has3_of_sExt_none` | 37,472 |
| 11 | D468 | `GlobalTheory.Fam.lawsLinks_of_geo_rows_cols_alt` | 36,634 |
| 12 | D382 | `GlobalTheory.Svd.modelsAt_of_part` | 36,499 |
| 13 | D497 | `GlobalTheory.T.square_leading_term_bound` | 34,272 |
| 14 | D383 | `Formalism.L2.SG.Pf.Coef.cutAt_of_deep` | 32,753 |
| 15 | D161 | `UpperTheory.Gal.Int.Geo.jumpStep_holds` | 32,467 |
| 16 | D414 | `GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt` | 31,788 |
| 17 | D424 | `GlobalTheory.NLinkE.main_alt_alt` | 30,640 |
| 18 | D162 | `UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_geo` | 30,291 |
| 19 | D163 | `UpperTheory.Gal.FixZ.FixK_holds` | 29,747 |
| 20 | D433 | `SelfIntersectionVolumeEstimates.height_lower_bound_general_alt` | 29,605 |

## 원문 대조와 검토 반영

- 원본 Lean 커밋 `40e56bab026552e089d7afcfeff08d2defb9c005`의 명제 623건, Prop 정의 및 보조 정의 2,333건, 증명 경로의 출발 선언 890건을 구간 해시와 대조했다. 제시한 경로 615개에서 연속 호출 2,748회(서로 다른 직접 호출 1,318개)가 컴파일된 증명 값에 실제로 나타난다. `.olean` 해시 기록 1,513건과 공개 매니페스트가 일치한다. 원문 및 증명 경로 (`R22_source_evidence.json`) · 검색 가능한 원문 부록 (`decomposition_sources.html`)
- 원래 52개 경계와 새 선언을 합한 641개 정점에서 삭제에 의한 지배량과 도달량을 재계산했다. N003 카탈로그 475개 전부를 대조했다. 동일 선언 72개는 같은 번호를 사용했고, 398개에는 가장 가까운 선택 지배자를 기록했다. 나머지 5개에는 선택 지배자가 없다. 그래프 원장 (`R22_graph_weights.json`)
- [R21 독립 검토](../../reviews/R21_review.md) §1–2. P128에서는 식 (8)이 주는 안정자 분해를 명시했다. N003·N478을 Blueprint 카탈로그의 T01·T13 대응으로 정의했다. 두 그래프의 차이 200줄은 추가 선언 29개이며, 공개 선언 5개가 각각 한 줄, 나머지가 195줄이다. Mechanism의 격자, 국소 오차와 Selmer 예산, 제곱근 지수, 창 구간과 주합·극점의 관계 및 관성 소수 지수 조건을 Lean 원문에 맞춰 6–7쪽에 반영했다.
- §3. 비교 항목 8개에서 Kollár의 SNC 조건, Washington의 원문 번호와 닫힌 증명 항, Scholze와 Demailly의 인용, Labesse의 차수 가정을 확인했다. W02·W04의 전 유한소 비분기 조건에서는 허수 이차체가 허용되지 않는다. 기존 Cited 3건과 이번 D311은 서로 다른 층의 집계다. 문헌 대조 (`R22_reference_review.json`)
- §4. 큰 12가지의 제안 선언 113개 모두에 원문 위치를 붙였다. 26개는 이미 원고에 있고 87개는 추가 읽기 위치다. 맥락을 설명하는 래퍼 7개와 중첩 예 2개도 대조했다. 표에 나온 115개 가중치를 재현했으며 P020의 21,873은 공제 전, 8,160은 공제 후이다. W01의 `mem_UC`는 8,001줄 중 7,998줄이 명제형, 3줄이 좌표별 고정점 동치를 적용하는 증명이다. 제안 대조표 (`R22_review_crosswalk.json`)
- §4.3. Cited 3개, Related 17개, 둘을 합친 20개 동시 삭제량은 전체 그래프에서 각각 6,445, 1,240,130, 1,246,697줄이다. T17–T24 공동 삭제량은 108,935줄이다. 검토서의 28개 인용 후보 중 명시적으로 식별되는 17개에 대해 169,763줄을 재현했다. 나머지 11개 이름이 특정되지 않아 28개에 대한 357,209줄과 20+28개에 대한 1,476,687줄은 미확인으로 남겼다. 검토서의 약 90만 줄 인용 가능 추정치도 처분 집계에서 제외했다. 공동 삭제 원장 (`R22_review_graph.json`)
- §5–6. P096·P134는 독립 검토의 `correct` 판정과 소수 보완 각 3건을 반영했다. 검토자가 별도 교차검토에 회부했으므로 두 후보는 계속 대기 상태이다. 용어집은 30개에서 38개로 확장하고 Lean 구간 44개를 확인했다. 후보 검토 기록 (`R22_candidate_review.json`)

## 배치 소요와 빌드

2026-11-24 UTC 19:49:59–20:22:21. 전체 경과 **32분 22초**. 아래 시간은 같은 시계에서 확인한 분 단위이며 겹치는 하위 작업은 합산하지 않았다.

| 배치 | UTC | 결과 |
|---|---|---|
| 원장·원본 준비와 첫 컷 | 19:49–19:56 | 32개 원래 영역과 우선순위, 첫 중복 제거 계산 |
| 수학 주제별 분할 및 추가 컷 | 19:51–20:03 | 세타, 기하, Selmer, 연결 정리의 원문 확인과 초과 영역 재귀 분할 |
| 문장·원문·수치 통합 | 20:03–20:09 | 최종 623개 항목, 증명 값 대조와 검토 전 빌드 |
| 독립 검토 반영 | 20:10–20:19 | 검토서 대조, 공동 삭제 재계산, 읽기 묶음, 기존 후보 수정 |
| 최종 빌드·대조·기록 | 20:19–20:22 | 316쪽 및 PDF 첨부 원문 확인 |

XeLaTeX/latexmk 빌드 성공. PDF SHA-256은 `df2186cdaf37b74b0c324accf67090add22c7a5ade0df01da854b9481986de89`이다. 모든 316쪽을 다시 열어 텍스트를 추출했다. PDF 내부 목적지 3,016개, 외부 URL 주석 240개, 로컬 링크 13개를 식별했고 미해결 목적지는 0개였다. 미정의 참조·중복 레이블·누락 글리프·넘침 경고는 0건이다. 부록 G에 첨부한 HTML은 원본과 바이트 단위로 일치한다. 1·6·7·96·138·141·310·313쪽을 렌더링했고, 역사적 140개 부모의 상태 및 원본 해시 검사도 통과했다.
