---
name: ee-research-planner
description: Plan 电气类 / 电子信息类 academic research from a vague idea into a usable research packet. Use for 开题、选题、综述框架、文献调研、找创新点、prior-art mapping、research planning、实验方案设计，或当用户给出关键词、摘要、DOI、citation、PDF 后需要结构化梳理已有工作、创新空间与验证路径。 Covers power/energy systems, power electronics & drives, communications/signal processing, circuits/chips/EDA, and embedded/IoT/control without paywall bypass.
---

# EE Research Planner

把模糊研究想法收敛成一套可继续推进的研究包：问题定义、领域路由、文献计划、prior-art 矩阵、候选创新假设、实验方案。

## 快速入口

用户输入进来时，先一眼判断：

| 用户说法 | 第一动作 | 可跳过的步骤 |
|---|---|---|
| 给了 DOI / 摘要 / PDF / citation | 直接进入证据抽取 → 卡片 → 矩阵 | 可跳过问题定义和赛道路由 |
| 只说方向关键词，方向已经清楚 | 确认主赛道 → 直接出检索计划 | 可跳过 workflow 阶段 1-2 |
| 说"找创新点" | 先确认是否已有文献池；没有则先出检索计划 | 不要跳过 prior-art |
| 说"做实验方案" | 先确认假设是否清楚；没有则先出 novelty hypotheses | 不要跳过 baseline 设计 |
| 方向极度模糊或跨多个赛道 | 读 `references/workflow.md` + `references/direction-routing.md` | 不跳 |
| 已有工作、只要继续某一段 | 直接从用户说的阶段接续，补一句上游假设 | 跳过前置阶段 |

> 能一步判断就不要绕圈子；不确定就只问 1 个最关键问题，不要同时问 3 个。

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
   - communications / signal processing / biomedical signals
   - circuits / chips / EDA
   - embedded / IoT / control
   - ECG / EEG / EMG、可穿戴生理信号分析、医学时序分类这类题，默认先落到 communications / signal processing；只有当主要贡献承载层明显在端侧部署、闭环控制或设备系统联动时，再转到 embedded / IoT / control。
3. 如果用户表达很虚、赛道不清或跨领域，先读：
   - `references/workflow.md`
   - `references/direction-routing.md`
4. 需要输出形状或跨赛道示例时，读：
   - `references/examples.md`
5. 遇到已较具体、但很容易被写泛的常见子方向时，读：
   - `references/domain-starters.md`
6. 需要深入展开时按需读：
   - 文献检索式与收敛：`references/literature-strategy.md`
   - 分层证据获取 / 工具路由：`references/retrieval-pipeline.md`
   - 结构化证据抽取：`references/evidence-extraction.md`
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
5. 候选新颖性假设（按 conservative / balanced / bold 三档各给 1 条，让用户按资源和周期选）
6. 实验计划
7. 风险、缺口、下一步检索 / 求证动作

如果用户只要其中一段，也尽量补一句“上一阶段的假设”和“下一阶段该做什么”。

## 模板

按任务类型选模板组合，不要每次全上：

| 用户要的产物 | 必用模板 | 可选模板 |
|---|---|---|
| 开题 / 选题 | `direction-brief-template` + `literature-plan-template` + `novelty-hypotheses-template` | `prior-art-framing-template` |
| 综述 / 文献调研 | `literature-plan-template` + `literature-card-template` + `literature-evidence-pack-template` | `innovation-matrix-template` |
| 找创新点 | `innovation-matrix-template` + `novelty-hypotheses-template` | `prior-art-framing-template` |
| 实验方案 | `experiment-plan-template` | `novelty-hypotheses-template`（确认假设用） |
| 吸收单篇 / 几篇论文 | `literature-card-template` | `literature-evidence-pack-template` |
| 完整研究包 | 全部 8 个，按交付顺序依次填 | — |

所有模板路径：
- `assets/direction-brief-template.md`
- `assets/literature-plan-template.md`
- `assets/literature-card-template.md`
- `assets/literature-evidence-pack-template.md`
- `assets/innovation-matrix-template.md`
- `assets/prior-art-framing-template.md`
- `assets/novelty-hypotheses-template.md`
- `assets/experiment-plan-template.md`

## 辅助脚本

**什么时候跑脚本**：用户要批量拉一批文献 metadata、或者要从几十篇候选中快速建卡片脚手架时。

**什么时候不需要跑**：只分析 1-5 篇、用户已提供 DOI / PDF、或者只要做方向判断时 — 直接用证据抽取流程即可，不用跑脚本。

可用脚本：
- `scripts/search_openalex.py`：按 query 拉 OpenAlex metadata 与 OA 线索
- `scripts/normalize_paper_records.py`：统一 paper schema，重建 abstract 文本
- `scripts/build_literature_cards.py`：把规范化记录转成文献卡片草稿

这些脚本是 metadata-first helper，不会自动完成全文抓取或深度证据抽取。

## 完成标准

按任务类型判断，不要等到全部 7 段都完成才收束：

| 任务类型 | 完成判据 |
|---|---|
| 开题 / 选题 | direction brief 有具体约束 + 主赛道明确 + 至少 2 条可操作假设 + 检索计划可执行 |
| 综述 / 文献调研 | 检索轴完整 + shortlist 有 8-15 篇 + 每篇有用途标签和证据等级 + 主流方向已分组 |
| 找创新点 | prior-art matrix 显出缺口 + 3 档假设各有最近邻对应 + 每条有风险标签 |
| 实验方案 | 假设已绑定 + baseline / 指标 / 平台明确 + MVP 包可立刻开始 + 资源风险已列出 |
| 吸收单篇 / 几篇 | 每篇有 9 字段卡片 + 证据等级标注 + 对当前问题的 novelty risk 判断 |

全流程完成标准（研究包）：
- 问题边界清楚，不再停留在泛方向口号。
- 主赛道与验证层级明确。
- 检索路径和 prior-art 对比框架明确。
- 候选创新点能对应最近邻工作，且通过反证检查（见 `references/innovation-analysis.md` §6）。
- 至少有一个可执行实验方案雏形。

## 推进卡住时的兜底规则

如果用户连续澄清后方向仍然不清晰，不要继续追问。强制执行：
1. 选一个最保守的问题解读，写出 direction brief 草稿。
2. 注明"以下基于我对你问题的暂定理解，请确认或修正"。
3. 给出 3 个"如果你其实是想做 X / Y / Z，我们需要往哪个方向调整"的选项。

不要让对话停在反复问问题上；给出最小产物比持续追问更有价值。