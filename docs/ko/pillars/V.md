# V · 한 구간 전체에 적용되는 셀머 길이 상계

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**V의 전체 서면 유도는 미완성이며 검토 대기 중이다.** V는 허용된 모든 수체와 유한 소수 집합에 같은 구간을 적용하는 셀머 길이 상계다. 조건부 정리에서는 V를 가정한다. P013은 편극 갈루아 행을 가정하여 V를 공급한다. 최상위 Lean 선언은 그 행을 `galoisLocalGlobalStrong_recParameter`로 공급한다. P013의 886,201줄은 행 공급자의 지배 영역을 제외한 그래프 계수다. [P013](../../../units/P013.md) · [B01](../../../units/B01.md) · [P010](../../../units/P010.md) · `everyCharacter` (`MainConclusion.lean:7–11`) · `galoisLocalGlobalStrong_recParameter` (`RowSrc.lean:6`)

## 정확한 명제와 Lean 진입점

양의 법을 갖는 원시 복소 디리클레 지표 $\psi$, 실수 $0<\varepsilon<1/52$, 모든 $x\ge1$에서 $x^{2+8\varepsilon}\le 2^{e(x)}\le2x^{2+8\varepsilon}$를 만족하는 임의의 함수 $e:\mathbb R\to\mathbb N$을 고정합니다. 그러면 어떤 실수 $J\ge1$과 $X_0\in\mathbb R$가 존재하여, 모든 실수 $X\ge X_0$와 $X^{1/J}$에서의 모든 허용 소수쌍 $(q,d)$에 대해 $X^{1/J}\le Y$, $Y^2\le X$를 만족하는 $Y$가 존재합니다. **모든** $x\in[Y,Y^2]$에서 $t=\lfloor x^{401}\rfloor_+$로 둡니다. $e(x),q,d$가 정하는 원분체 조건을 만족하는 모든 수체 $E$, 모든 대수적 폐포 $\Omega/E$, 허용되는 모든 국소 자료계 $D=(D_\ell)_\ell$에 대해, 모든 소수 $\ell$과 $1\le k<t$에서 길이 $h_\ell(k)$는 유한합니다. 또한 모든 유한 소수 집합 $S$에 대해
$$
\sum_{\ell\in S}\log(\ell)\sum_{1\le k<t}h_\ell(k)\le\sqrt{\exp(x^\varepsilon)}.
$$
여기서 $h_\ell(k)$는 소수 $\ell$과 꼬임 $k$에서 국소화 사상 핵의 $\mathbb Z_\ell$-길이입니다. 영어 지도의 다음 절에서 소수쌍 조건, 원분체 조건과 이 사상을 풉니다. `PChar` (`PrimePairSizeCondition.lean:7–11`) `PageN` (`ExistsPageN.lean:39–39`) `VVle` (`ExistsPageN.lean:12–17`) `VAt` (`ExistsPageN.lean:41–42`) `VWinAt` (`ExistsPageN.lean:44–47`) `VWin` (`ExistsPageN.lean:49–49`)

```lean
def VWin : Prop := ∀ ψ : PChar, VWinAt ψ 401

theorem UpperTheory.One.vwin_of_row
    (h : UpperTheory.GalStar.Row0b fun h rc => UpperTheory.Zero.LLC.IsRecT h rc) :
    UpperTheory.Top.VWin
```

[고정 판본의 정의](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean#L49-L49) · [가정과 결론을 잇는 Lean 선언](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean#L4-L5) · [영어 지도 전체](../../../pillars/V.md)
