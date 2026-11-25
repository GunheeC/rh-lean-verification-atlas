# 실명 검토를 기록하는 방법

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

직접 유도하거나 원문과 대조한 추론 하나부터 기록할 수 있다. 점검표에서 그 단계 번호와 판본의 SHA-256 식별자를 복사한다. 이 식별자가 검토한 글을 특정한다. 어떤 계산을 했고 무엇을 발견했는지 적는다. 빈틈, 유보 사항, 따라가지 못한 단계도 단독으로 제출할 수 있다. [점검표 선택](../../../ROADMAP.md) · [가상 예시(Fictitious)](../../../signoffs/examples/FICTITIOUS-EXAMPLE.yaml) · [접수된 이의](../../../questions/disputes.md) · [English](../../../signoffs/README.md)

## 제출

실명 검토 이슈 양식을 사용하거나 아래 명령으로 만든 기록을 풀 리퀘스트로 낸다. 제출하는 모든 항목은 공개된다. 소속과 ORCID는 선택 사항이다. 본인이 읽었다는 확인 문구는 이름을 기재한 독자가 작성한다. 관리자는 제출자의 글을 옮겨 적는다. 관리자인 Gunhee Cho가 직접 읽고 제출하면 관리자 검토로 표시한다. [이슈 양식](../../../.github/ISSUE_TEMPLATE/signoff.yml) · [필드 안내](../../../signoffs/TEMPLATE.md)

| 범위 | 판정 입력 방식 |
|---|---|
| 지정한 단계 | 단계마다 하나의 평결을 쓴다. YAML 예시는 `scope: {steps: [S1, S3]}`이다. |
| `whole-note` | 판본의 모든 활성 단계에 평결을 쓴다. 건너뛴 단계는 `not-attempted`로 표시한다. |
| `statement-vs-lean` | 서술한 명제의 양화 순서, 가정, 결론을 고정 Lean 선언 또는 해당 성분 선언들과 대조해 이 대상에 별도 평결을 쓴다. |

평결은 `checked-correct`, `correct-with-reservation`, `gap-found`나 `error-found`는 이의를 연다. 같은 대상에 대한 이의는 원래 제기자와 다른 독자만 해소할 수 있으며 관리자는 해소자가 될 수 없다. 새 평결은 `checked-correct`여야 한다. 해결 과정과 원래 기록의 파일명을 적는다. 이슈에는 `S2: checked-correct resolves PRIOR_RECORD.yaml`, YAML에는 `resolves: {S2: [PRIOR_RECORD.yaml]}`이라고 쓴다. 원래 평결과 해소 기록을 함께 공개한다. 명제 대조에도 같은 규칙이 적용된다. [공개 이의 목록](../../../questions/disputes.md)

판본이 바뀌면 긍정 평결을 새로 받아야 한다. 이의가 제기된 단계나 명제가 그대로이면 이의는 새 판본에도 남는다. 그 대상 자체를 수정하거나 폐기하면 종전 이의에 교체 사실을 표시한다. 바뀐 대상은 새로 읽고 기록해야 한다.

**L4는 명시된 입력을 전제로 한 Full 단위에만 부여한다.** 체크리스트에 유도 단계가 하나 이상 있어야 한다. 입력이나 문헌을 호출하기만 하는 단계만으로는 충분하지 않다. 현 판본의 모든 활성 단계와 별도의 명제 대조 각각에 `checked-correct`가 필요하다. `correct-with-reservation`과 미시도·판단 불가 평결은 긍정 확인에 포함되지 않는다. 단계마다 다른 사람이 읽어도 된다. 이 표지는 입력 자체, 의존 그래프, V, F 또는 RH의 진위를 판정하지 않는다.

근거 등급은 누적되지 않는다. L4에 앞선 AI 등급이나 별도 해설이 필수인 것은 아니다. 관리자 혼자도 요건을 충족할 수 있다. L4 옆에는 기여 독자 수, 관리자 포함 여부, 신고한 AI 도움 수준(`none`, `some`, `substantial`)이 표시된다. 이름·소속·ORCID는 제출자의 자기 신고이며 저장소는 신원을 인증하지 않는다.

‘독립 독자 2명 이상’은 별도 표지다. 각 대상마다 서로 다른 두 독자가 `checked-correct`를 제출하고 `what_i_did`에 “I checked independently of other readers.”를 써야 한다. 이해충돌란은 `none`이어야 한다. AI 도움 `substantial`은 공개하지만 독립 확인에는 포함되지 않는다. 같은 이름이나 ORCID는 두 명으로 세지 않는다. 단위 전체에 표지를 붙이려면 모든 활성 단계와 명제 대조가 각각 요건을 충족해야 한다.

## 관리자와 풀 리퀘스트

이슈 본문을 텍스트 파일로 복사하거나 필드 안내에 따라 YAML 또는 JSON을 준비한다. `-`를 사용하면 표준 입력으로 붙여 넣을 수 있다. 아래 명령은 날짜, 독자 정보, 본인 확인 문구, 판본과 단계 지문, 범위와 평결을 검증한다. 접수 명령은 고유 번호를 부여해 기록하고 생성 페이지를 갱신한다. 같은 본문을 다시 입력할 때는 원래 기록을 유지한다.

```sh
python scripts/add_signoff.py --dry-run my-check.yaml
python scripts/add_signoff.py my-check.yaml
```

로컬 변경을 검토한 뒤 풀 리퀘스트에 `signoffs/records/YYYY-MM-DD_UNIT_reader-slug_n.yaml`과 재생성한 파일들을 포함한다. 정정은 새 기록으로 제출하며 원 제출은 수정하거나 삭제하지 않는다. 집계가 달라지면 `python scripts/snapshot.py --append --round 'Edition label'`로 판본을 기록한다. 선택 인수 `--date`에는 UTC 날짜를 넣는다. 접수와 게시는 수동이다. [진척 기록](../../../PROGRESS.md)

논증을 수정할 때는 단위 ID마다 노트 경로 목록 `sources`와 해당 `*.steps.yaml` 형식의 `steps`를 준비한다. 단계 번호를 유지하고 새 판본에 해당하는 AI 근거만 남긴다. `python3 scripts/proof_steps.py --install updated_specs.json` 다음 `python3 scripts/refresh_round4.py`를 실행한다. 이전 판본과 폐기된 번호를 보존하고 점검표·등급을 갱신한다. 새 판본에 남은 단계도 다시 읽고 제출해야 한다.
