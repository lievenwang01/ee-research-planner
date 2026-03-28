# Examples

这份参考只展示“输出该长什么样”，不是完整答案。用于从模糊对话快速落到合适产物形状。

## Example 1 — Power / Energy Systems：开题 / 选题输出形状

**用户意图**
- “我想做配电网韧性相关开题，但题目还很虚。”

**推荐输出骨架**
1. **问题压缩**
   - 暂定对象：含分布式电源的配电网故障恢复
   - 暂定任务：在极端天气后提升服务恢复速度与负荷保供能力
   - 关键约束：不完全信息、可再生波动、开关操作次数受限
2. **direction brief**
   - 主赛道：power / energy systems
   - 副赛道：embedded / control（若涉及分布式协调控制）
   - 预期贡献：韧性指标重构 / 恢复优化策略 / 极端场景评估
3. **literature plan**
   - 检索轴：resilience / service restoration / distribution network / uncertainty
   - 纳入标准：近 5 年 + 经典恢复模型 + 极端场景论文
4. **prior-art 缺口**
   - 现有工作多在静态故障集上验证，极端连锁场景不足
   - 多数只看恢复成本，不同时刻画保供公平性与恢复时序
5. **候选假设**
   - 引入“恢复速度 + 关键负荷优先级 + 操作复杂度”的联合目标可更稳定地区分策略优劣
6. **实验计划**
   - IEEE 33 / 69 节点系统
   - 基线：传统恢复优化、单目标韧性调度
   - 指标：ENS、恢复时间、关键负荷保供率、求解时间

## Example 2 — Communications / Signal Processing：prior-art mapping 输出形状

**用户意图**
- “帮我做一个低 SNR 场景下通信感知一体化接收机的文献调研，重点找创新空间。”

**推荐输出骨架**
1. **任务定义**
   - 主赛道：communications / signal processing
   - 目标产物：prior-art matrix + innovation hypotheses
2. **分组方式**
   - 按 receiver 范式分组：model-based / hybrid / learning-based
   - 按场景分组：static / mobility / interference-rich / low-SNR
3. **prior-art matrix 示例列**

| 代表文献 | 任务边界 | 接收机机制 | 假设条件 | 指标 | 主要不足 |
|---|---|---|---|---|---|
| A | joint detection + sensing | model-based iterative | known CSI | BER / NMSE | 低 SNR 下退化明显 |
| B | ISAC receiver | unfolded network | synthetic channel only | BER / Pd | 泛化边界不清 |
| C | hybrid receiver | sparse prior + DNN | narrowband | BER / complexity | 干扰场景不足 |

4. **创新假设形状**
   - Hypothesis 1：把低 SNR 鲁棒先验显式嵌入 hybrid receiver，可降低纯学习模型对信道分布漂移的敏感性。
   - 最近邻：hybrid / unfolded receiver 类工作。
   - 最小验证：SNR 扫描 + 分布外信道 + 干扰场景。

## Example 3 — Circuits / Chips / EDA：实验方案输出形状

**用户意图**
- “我想做一个面向低功耗数字电路的 EDA 选题，最后要落到实验方案。”

**推荐输出骨架**
1. **direction brief**
   - 主赛道：circuits / chips / EDA
   - 任务：在 timing 约束下优化低功耗综合 / 映射流程
   - 证据层级：open-source benchmark + tool-flow evaluation
2. **最近邻 prior art**
   - 传统启发式映射
   - 学习辅助 PPA 优化
   - 只优化功耗、忽略 runtime 或 timing closure 的方案
3. **实验计划形状**
   - Benchmarks：ISCAS / EPFL / open-source RTL sets
   - Baselines：经典 heuristic flow、近期 ML-guided flow
   - 主指标：power、delay、area、runtime
   - 控制变量：工艺库、约束脚本、综合参数
   - 消融：是否使用结构特征、是否使用多目标排序
   - 成功判据：在不破坏 timing closure 的前提下取得稳定 PPA 改善

## 什么时候用这些形状

- 用户说“开题 / 选题”时，优先参考 Example 1 的骨架。
- 用户说“文献调研 / prior-art mapping / 找创新点”时，优先参考 Example 2。
- 用户说“做实验方案 / 怎么验证 / benchmark 怎么选”时，优先参考 Example 3。