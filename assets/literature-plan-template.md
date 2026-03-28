# 文献检索计划模板

## 1. 当前检索任务
- 目标产物：开题摸底 / 综述 / prior-art mapping / baseline 收集 / 实验落地
- 当前问题切片：
- 主赛道 / 副赛道：
- 关键约束：
- 当前证据目标：先画地图 / 找最近邻 / 找可复现实验设置 / 找 warning papers

## 2. 检索边界
- 时间范围：
- 文献类型：期刊 / 顶会 / survey / benchmark / 标准 / thesis / code / supplement
- 证据来源优先级：metadata / OA / authorized / user-provided
- 语言范围：中文 / 英文
- 明确排除项：

## 3. 四组检索轴
| 轴 | 核心词 | 同义词 / 缩写 | 必须联用的约束词 | 暂不纳入的近邻词 |
|---|---|---|---|---|
| 问题轴 |  |  |  |  |
| 方法轴 |  |  |  |  |
| 指标轴 |  |  |  |  |
| 约束轴 |  |  |  |  |

## 4. 检索式草案
- Query 1（problem + method）：
- Query 2（problem + metric / constraint）：
- Query 3（problem + review / survey / benchmark）：
- Query 4（problem + hardware / prototype / HIL / real-time）：
- Query 5（closest baseline + limitation / comparison）：

## 5. 纳入 / 排除标准
### 纳入标准
- 
- 
- 

### 排除标准
- 只谈泛方向、和当前问题切片距离过远
- 实验平台或约束条件无法判断，且暂时不能补证据
- 与当前方向近似但实际上是另一赛道主问题
- 

## 6. 收敛策略
### Mapping Pool（20-40 篇）
- 目标：认地图、找 recurring terms、benchmark、baseline 名
- 保留规则：

### Shortlist（8-15 篇）
- 目标：做 prior-art matrix
- 优先保留：近 3 年代表作 / 经典基线 / 和我最接近的约束 / 实验透明度高的工作 / warning paper

### Deep-read Set（3-6 篇）
- 目标：精读、选 baseline、定实验
- 必须覆盖：最近邻工作 / 经典强基线 / 最新代表作 / 实验最透明工作 / warning paper

## 7. 证据等级与用途标签计划
| 候选文献 | 预估用途标签（map / anchor / baseline / method-fragment / warning） | 当前证据等级（E0-E4） | 下一步补证据动作 |
|---|---|---|---|
| Paper / topic A |  |  |  |
| Paper / topic B |  |  |  |
| Paper / topic C |  |  |  |

## 8. 需要优先确认的 benchmark / dataset / simulator / hardware 线索
- benchmark / case：
- dataset / channel / load / design set：
- simulator / toolchain：
- hardware / HIL / prototype 线索：

## 9. 当前已知风险
- novelty-risk：
- evidence-risk：
- comparability-risk：
- resource-risk：

## 10. 本轮检索结束时至少要拿到
- 关键词分层表
- shortlist 与用途标签
- 最近邻 prior art 候选
- benchmark / baseline / platform 线索
- 下一轮需要补全文或补证据的清单