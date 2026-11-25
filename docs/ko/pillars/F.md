# F · 한 선택에서 동시에 성립하는 정부호 쪽 증인

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**F의 전체 서면 유도는 미완성이며 검토 대기 중이다.** 조건부 정리는 정부호 쪽에서 노름 상계와 모든 행 조건을 같은 자료로 충족하는 증인의 존재를 가정한다. 최상위 Lean 경로는 편극 갈루아 행과 국소 사상의 존재 증명에서 출발해 T02의 두 레코드, 세타 비교, 공변부피 상계와 국소 존재 증명을 공급한다. `RecTExists`는 각 자리에서 사상이 존재한다는 명제다. [영어 전체 지도](../../../pillars/F.md) · [조건부 정리](../../../units/V4-COND.md) · `everyCharacter_of_row` (`MainConclusion.lean:7–11`) · `every_character_of_literature_of_vWin` (`EveryCharacterOfLiteratureOfVWin.lean:810–813`)

## 정확히 무엇을 가정하는가?

$N(\mathcal C)=\mathrm{Closed}(\mathcal C,(F_m,H)\mapsto\mathrm{LinkN}(F_m))$, $D_*=\mathrm{DefiniteSideCondition}$으로 두면 정확한 종속 타입에서의 명제는 다음과 같다.
$$
 F\quad\Longleftrightarrow\quad\exists w:\mathrm{HypsAlt}(N,D_*),\quad\top .
$$

```lean
Nonempty (_root_.GlobalTheory.Fc.HypsAlt
  (fun 𝒞 => Closed 𝒞 fun Fm _ => LinkN Fm)
  _root_.GlobalTheory.Fc.DefiniteSideCondition)
```

족의 클래스 $\mathcal A$, 묶음의 선택 $\sigma$, 함수 $c_T:\mathbb R^2\to\mathbb R$와 나머지 조건의 증거가 모두 $w$에 들어 있다. 노름 조건은 $N(D_3(3,\mathcal A))$이며 정부호 행 조건은 $D_*,\mathcal A,\sigma$를 함께 사용한다. 점이나 행마다 별개의 선택을 하면 이 양화 순서를 잃는다. [TopPlug.lean:12–15](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean#L12-L15) · [HypsAlt, Hyps.lean:22–90](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Hyps.lean#L22-L90)

노름 조건을 풀면 어떤 $\varepsilon_1>0$이 있고, 각 $0<\varepsilon\le\varepsilon_1$에 대해 충분히 큼을 재는 자료 $K$가 있다. 모든 $F_m:\mathrm{FamP}(\varepsilon)$와 실수 $H$에 대해 $D_3(3,\mathcal A)(F_m)$, $F_m.\mathrm{Large}(K,H)$를 가정한다. 그러면 어떤 $C,x_0\in\mathbb R$가 있어 모든 $x\ge x_0$, $\mathrm{ShaFinOdd}(F_m.D(x,i))$인 모든 $i\in F_m.\mathrm{Ix}(x)$, 허용되는 모든 리프트 $j$에 대해 $\mathrm{LinkN\_at}(F_m.L(x,i),j,C)$가 성립한다. 마지막 수치 부등식에는 합의 수렴 조건이 한 번 더 들어간다. [Closed, ParamsHeightRankConstant.lean:157–161](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ParamsHeightRankConstant.lean#L157-L161) · [S0.NL, GeometricWeakTiesOfStrong.lean:36](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/GeometricWeakTiesOfStrong.lean#L36-L36) · [LinkN, GlobalTheoremInputs.lean:40–47](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L40-L47)

T02의 검사 벡터 단계는 `P.greenCuspidal`도 쓴다. 이 필드의 타입은 조건부 정리의 Green 명제와 정의상 같다. [T02](../../../units/T02.md) · `nonempty_hyps_definite_side_of_closed_bound` (`SiegelEisensteinSecondTermHypotheses.lean:49–50`) · `GreenCuspidal` (`GreenCuspidalIff.lean:8`)
