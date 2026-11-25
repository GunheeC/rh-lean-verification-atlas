AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R18_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R18_review.md`
- SHA-256: `0e60c972a3860dd5590fc4574819c0b8cfeb03072fd94667a2804033f52e1862`
- Report scope: R18에서 반영한 R17 독립 검토

## Archived report · [English summary](../../reviews/R18_review.md)

The report below preserves its original verdict, scope and unresolved points. Source line numbers in other records count from its original title.

# R18에서 반영한 R17 독립 검토

원본 커밋은 `40e56bab026552e089d7afcfeff08d2defb9c005`다. 검토 문서의 판정, 제출 당시의 수치, 지금 작업본에서 확인한 내용을 구분해 기록했다. [독립 검토](../../reviews/R17_review.md) · 원문 위치와 판정별 근거 (`R18_review_overlay.json`)

## Z4.2.04 및 등록부

| 항목 | 원본 대조 결과 |
|---|---|
| E1 | `ThetaVec.thetaVector`의 구현은 `PeriodLatticeSesquilinearFormIsHerm.lean:437–498`이며 Pair 콘에 속한다. 별칭 `Ker.Cd.kThetaVector`는 `IsAdmissibleFlagPairOfUnitriangularLeftAutomorph.lean:28–30`에 있고 Pair 밖에 있다. |
| E2 | `WeilVac.thMM_spec`은 `ExistsWeilOThZeroTriv.lean:33–36`에서 네 사본 항등식의 계수를 공급한다. `Base.thMM_spec`와 `Ker.kThetaVector`는 정칙성 경로에 있다. |
| E3 | 이미 센 콘을 차례대로 제거하면 `vector_bound_link` 우회분은 270/247줄, `ThetaLine.theta_line` 우회분은 2,046/2,015줄이다. 표준 격자의 정수성은 `Base.latAll`이 공급한다. |
| E4 | P장 r15 469–478행은 선택한 `sgStar`를 수정 시그마와 일치시키고 r16 298–305행은 원점에서의 Lean 규약과 네 기호의 대응을 적는다. |
| E5 | P장 r16 364–367행의 승수 식은 각 자기쌍대 격자에 대한 정수성 다음에 온다. |
| E6 | 그래프와 소스가 가리키는 범위는 `FourthRootStd.stdOK` 700–701, `FL.lam_mem` 528–540, `StdData` 52–64, `quadMultiplierRules` 234–242다. P장 r15의 Milne ANT·FT 주소와 판본 표기, MF v1.31의 날짜를 정리했다. r16은 같은 ANT v3.01을 인용한다. |
| E7 | 작업 원장에는 이미 15건 모두 confirmed였으며 독립 검토자가 받은 묶음에서 이 파일이 빠졌다. 15건 각각의 이름·파일·시작·끝 줄을 원문 및 그래프와 대조했다. R16 원판정은 CONFIRMED 13, CONFIRMED WITH GAPS 2였다. E1–E7 반영 뒤의 승인과 원판정을 함께 담은 현재 등록부를 검토 묶음에 넣었다. |

Z4.2.04는 독립 AI 검토를 거친 무조건 complete다. 상위 입력은 14/20이다. 네 구현자의 Pair 잔차 합집합은 8,373/7,887줄, 선택 래퍼를 포함하면 8,379/7,893줄, 다섯 진입점을 모두 끊어야 도달할 수 없는 부분은 3,654/3,477줄이다. 앞 수는 코어 전체, 뒤 수는 정리다. 15개 선언과 근거 (`R16_pending.json`) · 상태 원장 (`status.json`)

## 세 블록의 등급과 인용 정밀도

| R17 블록 | 선언 수 | 코어 줄 | A → S의 근거 |
|---|---:|---:|---|
| `z15-twexp-c2b58f` | 1 | 129 | 비영 꼬인 대각합으로 고정 가중공간을 고른 뒤 그 위에서 가환 연산자들의 공통 고유벡터를 취한다. |
| `z15-cosetsum-d24f4c` | 2 | 189 | 유한 개의 서로소 이중잉여류를 나눈 뒤 동일한 안정자 부피를 합한다. 보조 선언은 대표들을 선택한다. |
| `z4213-099` | 5 | 84 | 분모의 소인수 중 N과 서로소인 부분을 분리하고 국소 지시원과 공통분모를 사용한다. |

세 블록을 이루는 원본 선언 8개를 모두 대조했다. 이동량은 402줄이다. R17의 A 71블록 중 장·절만 인용한 28블록(Mumford 20, Weil 5, Etingof 3)에 `장 수준` 표시를 남겼다. 이 중 `z4213-099`가 S로 이동해 기존 A에서 정리 단위 근거를 보강할 행은 27개다. 기존 A 71블록 가운데 68개가 A에 남는다. 원본 인용과 개정 등급은 블록별로 조회할 수 있다. 28개 행과 세 재등급의 원문 위치 (`R18_review_overlay.json`)

Milne ANT 5.11, Voight 14.6.9, Deitmar–Echterhoff 1.5.2는 지정 판본의 본문을 확인했다. Lam VI.2.12는 원서 색인과 Clark–Jagy의 정확한 인용을 대조했다. 같은 결론이 2진 국소체를 포함한다는 점을 Casselman 명제 9.2의 원문 증명으로 확인했다. Lam 원서 정리 본문은 직접 확인하지 못했다. Cox의 격자 존재·유일성 증명 위치 및 Mumford·Weil의 판본별 쪽 범위도 기록했다. 문헌과 각 Lean 선언의 가정 대조 (`R18_citations.md`)

## 문헌 경계에서 생긴 6줄

같은 20개 입력의 그래프에서 첫 문헌 선언에서 멈추면 코어는 194,661개 선언, 1,604,500줄이다. 도달한 문헌 경계는 759개 선언, 3,855줄이다. 이 경계 밖으로도 계속 가면 문헌 19개와 코어 4개의 꼭짓점이 추가된다. 추가 코어는 아래와 같다. 문헌까지 통과한 탐색에서 R16 검토 B의 수치 1,604,506을 정확히 재현했다. R16 검토 B의 개별 실행 코드는 확보되지 않았다.

| 지나간 문헌 선언 | 그 아래 추가되는 코어 | Lean 원문 | 가중치 |
|---|---|---|---:|
| `Published.FontaineBcris.oneSubPhiOnto_of_filZero` | `MemLoc.Core.OneSubPhiOnto` | `AcrisTorsionFreeComplete.lean:225` | 1 |
| `Published.FontaineBcris.fundOnto` | `MemLoc.Core.FundOnto` | `AcrisTorsionFreeComplete.lean:223` | 1 |
| `Published.cheb_holds` | `TwSys.Cheb` | `GaloisSideTwistedSelmerAuxiliaryPrimes.lean:11–14` | 4 |
| `Published.cheb_holds → TwSys.Cheb` | `TwSys.Cheb._proof_1` | 생성 선언, 원문 범위 없음 | 0 |

R18의 분모는 첫 문헌에서 멈춘 1,604,500줄이다. R17 두 시범 입력의 U에서 양의 가중치를 가진 비명제 정의는 9,496개, 40,072줄이다. 원문 범위가 없는 생성 정의 2,393개를 더해도 줄 수는 같다. 규칙 1을 20개 입력에 적용하는 단계에서 이 분량을 D로 보냈다. 규칙별 검증 (`R18_gates.json`)

## 원래 등급 및 현재 판정 조회

R17_triage.json (`R17_triage.json`) 하나에 R17 소유자표 108,757행과 블록 장부 48,646행을 각각 원래 gzip 바이트와 그 SHA-256으로 넣었다. 모든 수동 분류 블록에 구성 선언의 전체 이름을 추가했다. 원래 소유 범위(시범 합집합과 시범 밖의 공유 코어)에 속하는 U 블록은 40,612개, 선언은 100,359개, 코어는 785,051줄이다. 이 중 시범 합집합의 U가 735,290줄이다. 독립된 빈 디렉터리에 JSON과 조회 스크립트만 복사해 40,612개 U 블록의 구성 선언 수와 가중치를 다시 합산했다.

```sh
python3 scripts/r17_lookup.py --declaration GlobalTheory.TieBase.base_data
python3 scripts/r17_lookup.py --block z4213-099@c067
python3 scripts/r17_lookup.py --class U > ${REVIEW_TMP}/r17_u_blocks.jsonl
python3 scripts/index_r17_review.py --output ${REVIEW_TMP}/r17_index_regenerated.json
```

전체 조회로 꺼내는 `classification`은 제출 당시 등급이며 후속 판정은 `round18_review`에 있다. R17 제출 당시 JSON을 압축 해제한 SHA-256은 `901b69db89875017ff2cf002fa868fd95b4e9215ca594797e5cf5f377d62c00b`이다. 동결된 제출본·두 장부·R18 검토 결과에서 색인 JSON을 다시 생성해 바이트가 일치함을 확인했다. 묶음 (`R18_review_packet.zip`)에는 제출 당시 도구·그래프·명제 추출물, 당시 결과, Z4.2.13 비교표, 현재 등록부와 조회 스크립트, SHA-256 목록이 있다.
