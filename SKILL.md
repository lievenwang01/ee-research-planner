---
name: ee-research-planner
description: Plan 电气类 / 电子信息类 academic research from a vague idea into a usable research packet. Use for 开题、选题、综述框架、文献调研、找创新点、prior-art mapping、research planning、实验方案设计，或当用户给出关键词、摘要、DOI、citation、PDF 后需要结构化梳理已有工作、创新空间与验证路径。 Covers power/energy systems, power electronics & drives, communications/signal processing, circuits/chips/EDA, and embedded/IoT/control without paywall bypass.
---

# EE Research Planner

把模糊研究想法收敛成一套可继续推进的研究包：问题定义、领域路由、文献计划、prior-art 矩阵、候选创新假设、实验方案。

## 默认立场

- 先定问题与赛道，再谈综述、创新和实验。
- 把“已有证据”与“待验证假设”分开写。
- 不做 paywall bypass；只用公开信息、已授权访问或用户提供材料。
- 不把“创新点”写成口号；必须对应最近邻 prior art 与可验证实验。

## 使用顺序

1. 先判断用户要的产物：开题 / 选题 / 综述 / 文献调研 / 找创新点 / 实验方案。
2. 再路由主赛道：
   - power / energy systems
   - power electronics & drives
   - communications / signal processing
   - circuits / chips / EDA
   - embedded / IoT / control
3. 如果用户表达很虚、赛道不清或跨领域，先读：
   - `references/workflow.md`
   - `references/direction-routing.md`
4. 需要输出形状或跨赛道示例时，读：
   - `references/examples.md`
5. 遇到已较具体、但很容易被写泛的常见子方向时，读：
   - `references/domain-starters.md`
6. 需要深入展开时按需读：
   - 文献检索：`references/literature-strategy.md`
   - prior-art framing（最近邻与缺口叙述）：`references/prior-art-framing.md`
   - 创新分析：`references/innovation-analysis.md`
   - 实验设计：`references/experiment-design.md`
   - 统计有效性 / 可复现性：`references/validation-and-reproducibility.md`
7. 只要开始写实验方案，就默认把“验证单位、方差 / CI、baseline 公平性、复现披露”一起补齐；不要只停在 benchmark 和指标。

## 默认交付顺序

优先按这个顺序组织输出：
1. direction brief
2. 主 / 副赛道路由与关键约束
3. 文献检索计划
4. prior-art 摘要或矩阵
5. 候选新颖性假设
6. 实验计划
7. 风险、缺口、下一步检索 / 求证动作

如果用户只要其中一段，也尽量补一句“上一阶段的假设”和“下一阶段该做什么”。

## 模板

需要稳定产物时，优先复用：
- `assets/direction-brief-template.md`
- `assets/literature-plan-template.md`
- `assets/literature-card-template.md`
- `assets/innovation-matrix-template.md`
- `assets/prior-art-framing-template.md`
- `assets/novelty-hypotheses-template.md`
- `assets/experiment-plan-template.md`

## 完成标准

当输出已经满足以下几点时可结束：
- 问题边界清楚，不再停留在泛方向口号。
- 主赛道与验证层级明确。
- 检索路径和 prior-art 对比框架明确。
- 候选创新点能对应最近邻工作与验证方法。
- 至少有一个可执行实验方案雏形。