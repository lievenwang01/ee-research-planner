# Literature Strategy

## 目录
- 0. 先定检索任务
- 1. 四层合法检索路径
- 2. 检索式构造法
- 3. 赛道化查询启发
- 4. shortlist 构造与收敛
- 5. 证据等级与使用边界
- 6. 只有 abstract-level 证据时怎么做
- 7. 最低输出要求

把文献检索设计成分层流程，不要把“能不能看到 IEEE 全文”当成唯一入口。

## 0. 先定检索任务

先写清检索任务，不然关键词会越搜越散：
- 研究对象：系统 / 器件 / 信号 / 芯片 / 控制对象是什么。
- 任务类型：预测、优化、控制、估计、诊断、设计自动化、部署。
- 关键约束：实时性、功耗、面积、稳定性、THD、可靠性、数据量、硬件成本。
- 输出目标：开题摸底、综述、baseline 收集、找 gap、为实验找可复现实验设置。

检索开始前至少产出 4 组词：
- 问题词
- 方法词
- 约束 / 指标词
- 证据词（review / benchmark / hardware / case study / dataset）

---

## 1. 四层合法检索路径

### Layer 1: Metadata / Abstract Search

先做广覆盖检索，用来画地图，不直接下细节结论。

可用来源示例：
- Google Scholar
- Crossref
- OpenAlex
- Semantic Scholar
- 出版社落地页
- 常规网页搜索

这一层的目标：
- 找高频关键词、缩写、同义词
- 找近 3-5 年代表性 venue / author / group
- 找经典 baseline 名称
- 找 survey / tutorial / benchmark / challenge paper
- 识别常用系统模型、数据集、公开 benchmark 名

操作顺序：
1. 用宽检索式找 20-40 篇 mapping pool。
2. 从标题 + venue + 年份 + abstract 里抽出 recurring terms。
3. 记录可复现信息：数据集、测试系统、benchmark、代码仓库、硬件平台名。
4. 用这些词做第二轮定向检索。

不要在这一层做的事：
- 不要把 abstract 没写的细节补成事实。
- 不要把“看起来像 SOTA”当成强 baseline 结论。
- 不要从一篇文章的关键词推导整个方向已成熟。

### Layer 2: OA / Full-text Discovery

在确认关键文献后，继续找合法可读全文。

优先顺序：
1. arXiv / TechRxiv / SSRN / 预印本
2. 作者主页 / 实验室页面 / institutional repository
3. open-access journal 页面
4. accepted manuscript / postprint
5. 补充材料、代码仓库、slide、poster、appendix

这一层重点补：
- 方法框架图
- 公式 / 模型假设
- 实验矩阵
- baseline 配置
- 指标定义
- ablation / robustness / hardware setup

如果找不到主文全文，但找到了代码、supplement、作者 slide，也要记录，因为它们常常能补齐实验条件。

### Layer 3: Authorized Full-text Access

只有当前环境已经具备 IEEE、ACM、Elsevier、Springer、CNKI、万方、学校图书馆或实验室订阅授权时，才使用对应数据库全文。

使用原则：
- 只在已登录 / 已授权时访问全文。
- 不把“理论上学校可能有权限”写成“已经拿到了全文”。
- 优先精读最关键的 5-10 篇，不做无限扩张。

全文精读时强制抽取：
- 问题定义与边界
- 方法细节与关键假设
- 系统模型 / 数据来源 / 工况
- baseline 与指标
- 作者承认的限制
- 哪些内容可以直接服务实验复现

### Layer 4: User-provided DOI / Citation / PDF

如果用户主动提供 DOI、BibTeX、截图、题目或 PDF，优先围绕这些材料深读。

处理原则：
- 先确认版本：journal / conference / preprint / thesis。
- DOI 与 PDF 标题不一致时，先解释版本关系，再总结内容。
- 把内容沉淀成卡片与矩阵，不只复述摘要。
- 用户给的 PDF 如果是最接近工作，应优先用来界定 novelty 风险和 baseline 选择。

---

## 2. 检索式构造法

至少准备 5 组检索式：
1. `problem + method`
2. `problem + metric / constraint`
3. `problem + review / survey / benchmark`
4. `problem + hardware / prototype / HIL / real-time`
5. `closest baseline name + limitation / comparison`

词组构造清单：
- 中文词组
- 英文词组
- 缩写 / 全称组
- 同义术语组
- 场景 / 工况组
- 指标 / 约束组

常见词位：
- 问题词：`state estimation`, `fault diagnosis`, `economic dispatch`, `beamforming`, `placement`, `task scheduling`
- 方法词：`graph neural network`, `model predictive control`, `Bayesian optimization`, `federated learning`, `observer`, `digital twin`
- 约束词：`real-time`, `low-power`, `high-noise`, `parameter uncertainty`, `resource-constrained`, `distribution shift`
- 证据词：`survey`, `benchmark`, `hardware experiment`, `case study`, `open-source`, `ablation`

建议把 query 设计成“主问题 + 约束”而不是只写方法名。EE / 电子信息方向里，约束常常比方法更决定论文位置。

---

## 3. 赛道化查询启发

### Power / Energy Systems

常见问题词：
- `optimal power flow`, `economic dispatch`, `unit commitment`
- `state estimation`, `fault location`, `stability assessment`
- `microgrid`, `integrated energy system`, `demand response`, `energy storage`
- `distribution network`, `renewable integration`, `resilience`, `voltage control`

常见约束词：
- `uncertainty`, `N-1 security`, `chance-constrained`, `low-inertia`
- `topology change`, `high PV penetration`, `carbon cost`, `islanding`

检索提醒：
- 同时搜 transmission / distribution / microgrid 三种表述，别把系统层级混成一个问题。
- 关注是否基于 IEEE 14/30/57/118-bus、MATPOWER、pandapower、OpenDSS、公开负荷 / 风光数据。
- 搜 `benchmark`、`case study`、`IEEE bus`、`real load data`，方便后续实验落地。

### Power Electronics & Drives

常见问题词：
- `DC-DC converter`, `inverter`, `multilevel inverter`, `grid-connected converter`
- `PMSM`, `IPMSM`, `induction motor`, `sensorless control`, `FOC`
- `current control`, `speed control`, `observer`, `MPC`, `deadbeat`, `SVPWM`

常见约束词：
- `low-speed`, `parameter mismatch`, `dead-time`, `switching loss`, `THD`, `current ripple`, `thermal`

检索提醒：
- 把器件对象、控制对象、工况词一起搜，比如 `PMSM sensorless low-speed robustness`。
- 额外搜 `HIL`, `dSPACE`, `OPAL-RT`, `DSP`, `C2000`, `prototype`，区分只有仿真和做过样机的工作。
- 关注采样频率、开关频率、负载变化、母线电压、参数摄动是否公开。

### Communications / Signal Processing

常见问题词：
- `channel estimation`, `signal detection`, `beamforming`, `equalization`
- `MIMO`, `massive MIMO`, `RIS`, `mmWave`, `OFDM`, `semantic communication`
- `radar signal processing`, `modulation recognition`, `source separation`

常见约束词：
- `low SNR`, `pilot overhead`, `mobility`, `phase noise`, `interference`, `latency`, `complexity`

检索提醒：
- Query 里显式加入指标词：`BER`, `BLER`, `NMSE`, `spectral efficiency`, `throughput`。
- 区分 synthetic channel simulation、公开数据集、OTA / SDR 实验。
- 对 AI 方法，额外搜 `generalization`, `dataset shift`, `training overhead`, `online adaptation`。

### Circuits / Chips / EDA

常见问题词：
- `placement`, `routing`, `floorplanning`, `logic synthesis`, `timing optimization`
- `power estimation`, `IR drop`, `clock tree`, `physical design`, `DFT`
- `approximate computing`, `accelerator mapping`, `HLS`, `verification`

常见约束词：
- `PPA`, `timing closure`, `congestion`, `memory footprint`, `runtime`, `scalability`

检索提醒：
- 一定同时搜 benchmark 名：`ISPD`, `ICCAD`, `DAC`, `OpenROAD`, `TAU`, `EPFL`, `Titan` 等公开基准。
- Query 里显式加 `open-source flow`, `public benchmark`, `technology library`，避免后面发现方法依赖不可得工艺库。
- 区分 proxy metric 改善与真正 signoff PPA 改善。

### Embedded / IoT / Control

常见问题词：
- `resource-constrained`, `edge inference`, `real-time scheduling`
- `networked control`, `fault-tolerant control`, `event-triggered control`
- `wireless sensor network`, `IoT security`, `battery management`, `embedded vision`

常见约束词：
- `latency`, `jitter`, `packet loss`, `RAM`, `flash`, `energy budget`, `safety`

检索提醒：
- 明确区分算法仿真、板级验证、闭环实物测试。
- 搜 `MCU`, `FPGA`, `FreeRTOS`, `HIL`, `testbed`, `long-term deployment`，因为实现平台直接决定论文可信度。
- 对控制问题，额外搜 `stability proof`, `Lyapunov`, `disturbance rejection`, `delay compensation`。

---

## 4. shortlist 构造与收敛

不要一上来抓几十篇精读。按三层池子收敛：

### A. Mapping Pool（20-40 篇）
用途：认地图。
来源：标题 + abstract + venue + 年份。
保留标准：
- 明显相关
- 能代表不同方法流派 / 系统设定
- 能暴露常见 benchmark / baseline

### B. Shortlist（8-15 篇）
用途：做 prior-art matrix。
优先保留：
- 近 3 年代表作
- 经典源头 / 公认强 baseline
- 和你的约束最接近的论文
- 有较强实验细节或可复现材料的论文
- 明显构成 novelty 风险的“warning paper”

可以按 5 个维度快速打分：
- `R` relevance：问题和约束是否贴近
- `E` evidence：拿到的信息有多深
- `C` comparability：实验设定能否迁移到你的计划
- `N` novelty-risk：是否直接堵死你的创新空间
- `P` practicality：数据 / 仿真 / 硬件资源是否可达

### C. Deep-read Set（3-6 篇）
用途：精读与实验设计。
优先级通常是：
1. 最接近你的问题设定
2. 最强经典 baseline
3. 一篇最新代表作
4. 一篇有最好实验透明度的工作
5. 一篇可能构成 warning 的近似工作

---

## 5. 证据等级与使用边界

建议显式标证据等级：
- `E0 metadata`：只有标题 / venue / 年份 / 作者
- `E1 abstract`：可读摘要，但无正文
- `E2 partial full-text`：有部分正文、supplement、代码、slide、appendix 中至少一类
- `E3 full text`：可合法读取正文全文
- `E4 full text + reusable setup`：正文可读，且实验设置 / 数据 / 代码 / benchmark 足够支持复用或复现规划

证据等级如何用：
- `E0-E1`：用于画地图、做 warning、找关键词，不用于下方法细节或 baseline 实现细节结论。
- `E2`：可以提炼部分方法框架和实验条件，但要标明哪些细节仍缺失。
- `E3-E4`：才适合拿来做强对比、baseline 复现、实验矩阵设计。

用途标签继续保留：
- `map`
- `anchor`
- `baseline`
- `method-fragment`
- `warning`

最好把“用途标签”和“证据等级”同时写。`baseline + E1` 表示“它可能是 baseline 来源，但还不能直接写实现细节”。

---

## 6. 只有 abstract-level 证据时怎么做

如果只有 abstract / metadata，不要停工，但要降级输出。

允许做的事：
- 判断它是否与当前方向相关
- 记录问题定义、任务设定、粗粒度方法流派
- 标出它可能构成的 novelty 风险
- 抽取下一轮检索词、作者、venue、benchmark 名称

不要做的事：
- 不要补写模型结构、损失函数、控制律、芯片流程细节
- 不要引用不存在的实验设置
- 不要把 abstract 里的“优于 baseline”写成具体百分比改进，除非摘要真的写了

推荐处理动作：
1. 把该文标成 `E1 abstract`。
2. 用一句话写“已知 / 未知”。
3. 发起二次检索：作者主页、代码仓、tech report、library access、用户是否能提供 PDF。
4. 如果拿不到全文，把它保留在 shortlist 的 `map` 或 `warning` 位，不直接进入 deep-read 核心集。

建议表述模板：
- `基于 abstract，可确认该文处理的是 X 问题并使用了 Y 类方法；正文未获得，因此 Z 细节与实验可比性暂不能确认。`

---

## 7. 最低输出要求

检索阶段至少交付：
- 关键词组与检索式
- 计划使用的数据源 / 数据库层级
- mapping pool → shortlist → deep-read 的收敛结果
- 每篇关键文献的用途标签与证据等级
- 目前能确认的 benchmark / dataset / simulator / hardware 线索
- 仅基于 abstract 判断的结论列表
- 下一轮需要补全文或补证据的清单

没有全文时，也可以做第一轮方向判断，但必须把证据等级写清楚。