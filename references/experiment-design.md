# Experiment Design

## 目录
- 1. 先绑定假设
- 2. 先选可达证据层级
- 3. 实验计划必备字段
- 4. MVP vs Full 实验矩阵
- 5. baseline 与比较规则
- 6. 各赛道强实验包
- 7. 消融、鲁棒性与失败边界
- 8. 资源与风险现实主义
- 9. 最低输出要求

只要提出候选新颖性假设，就同步设计实验。不要把实验计划留到“以后再说”。

涉及统计有效性、重复运行、数据划分纪律、baseline 调参公平性、可复现性披露时，配套读 `references/validation-and-reproducibility.md`。

## 1. 先绑定假设

每个实验都要明确服务于哪条假设：
- 假设是什么
- 为什么预期有效
- 哪个机制或约束让它可能成立
- 什么结果会支持它
- 什么结果会推翻它

推荐写法：
- `H1：在 X 约束下，引入 Y 机制后，指标 Z 相对 baseline A/B 提升，同时代价不超过 T。`

不要写空泛假设，例如“本方法整体性能更好”。要写清：
- 对谁更好
- 在什么工况下更好
- 代价上限是什么

---

## 2. 先选可达证据层级

EE / 电子信息研究里，实验层级通常有四种：
- analytical / theoretical
- simulation
- benchmark / software implementation
- hardware / HIL / prototype

优先选择当前资源能支撑的最高可信层级，但不要假装能做到没有平台的层级。

常见判断：
- 只有模型、没有平台：先做到理论 + 仿真 + 软件 benchmark。
- 有实时仿真平台：可以上 HIL。
- 有板卡 / 样机 / 电机台架 / SDR / FPGA / MCU：再谈 prototype。
- 没有流片、没有 NDA 工艺库、没有现场数据：不要暗示能做 silicon / industrial deployment 级验证。

---

## 3. 实验计划必备字段

每个方案至少写清：
- hypothesis
- target domain and problem setting
- evidence level target（simulation / software / HIL / prototype）
- baseline(s)
- independent variables
- dependent variables / metrics
- controlled factors
- dataset / simulator / hardware platform
- scenarios / operating conditions
- validation unit（run / seed / case / design / measurement）
- repeated runs / seeds / case count（如适用）
- variance / confidence interval reporting plan（如适用）
- train / val / test 或 dev / held-out discipline（数据驱动任务）
- ablation / sensitivity / robustness checks
- complexity / resource cost
- reproducibility disclosure items（toolchain / library / solver / hardware / benchmark version）
- success criteria
- failure criteria
- schedule / prerequisite risks

如果研究问题和资源条件不匹配，这里要直接暴露，不要后面再补一句“视情况而定”。

---

## 4. MVP vs Full 实验矩阵

默认先给两层计划：

### MVP 实验包
用于判断方向值不值得继续投入。

至少回答：
- 主假设是否有可见信号
- 在 1-2 个代表工况下是否优于强 baseline
- 关键 trade-off 是否还能接受
- 是否存在明显复现 / 资源阻塞

### Full 实验包
用于支撑论文主结果或开题后的完整验证。

至少扩展到：
- 多场景 / 多工况矩阵
- 强 baseline 全面对比
- ablation
- robustness / sensitivity
- complexity / resource overhead
- failure boundary
- 如果资源允许，再补 HIL / hardware / prototype

建议用下面的矩阵：

| 层级 | 目标 | 最少内容 | 停止 / 继续条件 |
|---|---|---|---|
| MVP-1 | 验证主假设是否有信号 | 1-2 个代表场景 + 2-3 个 baseline + 主指标 | 若主指标无提升或代价过高，停止或换假设 |
| MVP-2 | 验证可复现性与稳定性 | 加入随机种子 / 参数扰动 / 轻量鲁棒性 | 若结果不稳定，先修设定再扩展 |
| Full-1 | 构成主结果 | 完整工况矩阵 + 强 baseline + 消融 | 若 improvement 只在窄场景成立，降级论点 |
| Full-2 | 构成工程可信度 | complexity / resource / HIL / prototype（若可达） | 若资源不可达，明确证据止于软件或仿真 |

---

## 5. baseline 与比较规则

baseline 不能只选弱对手。至少包括：
- 一个经典强基线
- 一个最接近的近期方法
- 如果用了复杂模型，再补一个简单低成本 baseline 说明 trade-off

比较时必须统一：
- 数据 / 工况
- 指标定义
- train / val / test 或开发 / 最终报告 case 的边界
- 训练预算 / 迭代预算 / 调参预算（如果有）
- 计算资源或控制周期
- 是否允许先验信息
- 失败计入规则（不收敛、超时、不可行、失稳是否算失败）

如果 baseline 缺实现，允许：
- 采用作者公开代码
- 采用社区公认复现
- 退一步只比较可合法复现的强 baseline，并写明未纳入原因

不要做的事：
- 让 baseline 工作在更差工况
- 对自己方法做更充分调参，对 baseline 不做
- 拿不同数据集或不同控制周期的结果硬比

---

## 6. 各赛道强实验包

### Power / Energy Systems

强实验包应至少包含：
- **系统模型 / 数据来源**：IEEE bus system、MATPOWER / pandapower / OpenDSS、公开负荷 / 风光 / 电价数据；说明 AC/DC、单时段 / 多时段、网络约束是否纳入。
- **工况矩阵**：负荷高低谷、可再生出力波动、拓扑变化、故障 / 失联、储能状态变化、不确定性水平。
- **baselines**：经典优化 / 调度 / 估计方法 + 最近代表作。
- **指标**：成本、损耗、违约率、弃风弃光、频压偏差、鲁棒性、求解时间、可行率、稳定性。
- **额外检查**：约束是否被真正满足；是否只在单个 test case 有效；是否对预测误差敏感。

MVP：
- 1-2 个标准系统
- 2-3 类代表工况
- 成本 / 可行率 / 求解时间三类核心指标

Full：
- 多系统规模
- 不确定性与安全约束扫描
- 与最新方法 + 经典方法全对比
- 若有条件，再加 HIL / 数字孪生 / 调度闭环仿真

### Power Electronics & Drives

强实验包应至少包含：
- **对象与模型**：变换器 / 电机参数，开关频率、采样频率、母线电压、负载范围、死区、器件非理想因素。
- **工况矩阵**：稳态 + 暂态；负载阶跃、速度变化、低速区、高速区、参数失配、网侧扰动。
- **baselines**：PI / FOC / deadbeat / MPC / observer-based 等经典强 baseline，加最接近近作。
- **指标**：效率、THD、电流纹波、转矩纹波、超调、调节时间、稳态误差、开关损耗、温升 / 热负荷、计算延迟。
- **实现约束**：控制周期是否可实时执行；算法复杂度能否放进 DSP / MCU / FPGA。

MVP：
- 单一对象模型 + 代表工况扫描
- 稳态与暂态各至少一组结果
- 主指标 + 计算开销

Full：
- 参数摄动 / 噪声 / 采样误差 / 死区鲁棒性
- 多工作点扫描
- 若资源允许，加 PLECS / Simulink 实时仿真、HIL、DSP / dSPACE / C2000 或样机实验

### Communications / Signal Processing

强实验包应至少包含：
- **信道 / 数据模型**：AWGN、Rayleigh、Rician、mmWave、MIMO、OFDM、RIS、公开数据集或可复现实验生成器。
- **工况矩阵**：SNR sweep、用户数 / 天线数、导频长度、干扰强度、移动性、失配场景。
- **baselines**：LS / MMSE / OMP / Viterbi / 传统 detector，以及近期强方法。
- **指标**：BER / BLER、NMSE、detection probability、throughput、spectral efficiency、latency、complexity、memory。
- **泛化检查**：训练分布与测试分布不一致时表现如何；是否依赖大量离线训练。

MVP：
- 1 套主信道模型
- 1 个核心任务
- SNR sweep + 2-3 个 baseline

Full：
- 多信道 / 多失配场景
- complexity 与 latency 对比
- 若资源允许，加 OTA / SDR / 原型链路验证

### Circuits / Chips / EDA

强实验包应至少包含：
- **benchmark**：公开设计集 / EDA benchmark；写明节点、工艺库、约束、是否开源 flow。
- **流程位置**：综合、布局、布线、时序优化、映射、验证、HLS 中的哪一步。
- **baselines**：工业 / 学术经典方法 + 最接近近期方法。
- **指标**：PPA（功耗 / 性能 / 面积）、WNS / TNS、拥塞、线长、DRC、runtime、memory、收敛稳定性。
- **可验证边界**：proxy metric 还是 signoff metric；是否依赖不可公开工艺库；能否在 OpenROAD 等公开 flow 下复现。

MVP：
- 公开 benchmark + 可跑通的开源 flow
- 质量指标 + runtime
- 至少证明不是只在单个小设计上有效

Full：
- 多规模 benchmark
- 代理指标与最终指标关联分析
- 消融 + 可扩展性
- 若没有流片或商业库，明确证据止于 benchmark / open-source flow，不暗示 silicon tape-out 结果

### Embedded / IoT / Control

强实验包应至少包含：
- **系统对象**：被控对象 / 网络结构 / MCU / FPGA / SoC / 传感器平台。
- **工况矩阵**：扰动、噪声、延迟、丢包、故障、功耗模式、长时间运行。
- **baselines**：经典控制 / 调度 / 部署方法 + 近期近作。
- **指标**：跟踪误差、稳定时间、超调、能耗、CPU 利用率、RAM / Flash、延迟、jitter、掉线恢复、长期稳定性。
- **安全边界**：控制饱和、失稳风险、资源耗尽风险、部署失败模式。

MVP：
- 仿真或软件在环 + 代表板级资源约束
- 控制性能 + 资源占用联合评估

Full：
- HIL / 实板实验
- 扰动 / 网络异常 / 长稳测试
- 若只能仿真，明确“尚未实板闭环验证”

---

## 7. 消融、鲁棒性与失败边界

至少回答：
- 哪个模块 / 机制贡献最大
- 去掉核心机制后会怎样
- 参数轻微变化后是否还有效
- 在哪些条件下失效
- 收益是否值得代价
- 如果结果含随机性，收益是否稳定而不是只赢一次

常见鲁棒性项：
- 参数失配
- 噪声
- 数据分布偏移
- 控制周期变化
- 负载 / 拓扑变化
- 硬件量化 / 延迟 / 内存受限

失败判据示例：
- 关键指标无统计意义提升
- 只在极窄场景有效
- 复杂度、时延、功耗、面积代价不可接受
- 对超参数或模型失配过敏，难以复现
- 违反工程约束：不满足实时性、稳定性、资源预算或安全边界

---

## 8. 资源与风险现实主义

实验计划必须显式写资源门槛：
- 是否有公开数据 / benchmark
- 是否需要商业软件 / 授权库 / 私有数据
- 是否需要 HIL、样机、板卡、电机台架、示波器、功率分析仪、SDR、FPGA、流片资源
- 是否需要长时间现场部署或企业数据

没有的资源不要默认拥有。推荐直接写成三类：
- `现有即可做`
- `借助学校 / 实验室条件可做`
- `当前不可得，仅能做软件 / 仿真替代`

如果证据层级只能到仿真，结论也要收缩：
- 可以说“在仿真 / benchmark 中显示潜力”
- 不要说“具备工程可用性”或“适合工业部署”

---

## 9. 最低输出要求

实验计划阶段至少交付：
- 1 条主假设的完整实验计划
- 备选假设的简版验证路径
- MVP vs Full 实验矩阵
- baseline 与指标表
- validation / reproducibility 短块（validation unit、n、方差或 CI、split discipline、baseline fairness、复现披露）
- 资源门槛与风险缺口
- 明确当前证据会止于 simulation / software / HIL / prototype 的哪一层

如果用户是开题阶段，先给最小可验证实验包；如果用户是论文冲刺阶段，再扩成完整实验矩阵。