# Validation and Reproducibility

## 目录
- 1. 先判断是否需要统计检验
- 2. 最少要交代的验证字段
- 3. 重复运行、随机种子与方差报告
- 4. 数据划分与 benchmark 纪律
- 5. baseline、调参与消融公平性
- 6. 各赛道的验证重点
- 7. 可复现性披露清单
- 8. 何时统计检验有意义，何时不必假装有意义
- 9. 最小报告块

实验计划不要只写“指标 + baseline”。还要写清结果是否稳定、比较是否公平、别人能否按同样条件复现。

## 1. 先判断是否需要统计检验

先识别你的**重复单位**是什么：
- 随机初始化 / 随机种子驱动的独立训练或优化运行
- 不同测试 case / 场景 / 拓扑 / 被试样本
- 不同时间窗 / 不同数据 split
- 不同硬件样机 / 板卡 / 芯片设计实例

如果结果来自明显随机过程、有限样本比较或跨 case 分布，就需要报告方差，并在合适时考虑统计检验。

如果结果本质上是单次确定性工程演示，例如：
- 单个硬件样机展示
- 单个 signoff flow 的一次 QoR 结果
- 单条闭环波形的单次截图

就不要硬套 t-test。此时更重要的是：
- 扩充场景覆盖
- 做参数 / 工况扰动
- 报告失败率或波动范围
- 明确证据层级仍有限

## 2. 最少要交代的验证字段

实验计划里至少补齐：
- **repetition unit**：按 run、split、case、device 还是 design 统计
- **n**：重复次数 / 场景数 / benchmark 数量
- **seed policy**：固定哪些随机种子，哪些保持独立
- **variance reporting**：mean±std、median[IQR]、min-max、95% CI 用哪种
- **data split / scenario split**：train / val / test 或 dev / held-out 纪律
- **tuning budget**：自己方法与 baseline 的调参预算是否一致
- **runtime environment**：硬件、仿真器、EDA flow、库版本、求解器版本
- **failure handling**：不收敛、违约、失稳、超时、编译失败如何记入结果

## 3. 重复运行、随机种子与方差报告

### 什么时候要多次运行

以下情况默认不要只报单次最优值：
- 深度学习 / 强化学习 / 随机搜索 / 随机初始化优化
- 含随机信道、随机噪声、随机负载或 Monte Carlo 仿真
- 启发式 EDA / placement / routing / scheduling
- 含随机丢包、扰动、网络时延注入的控制 / IoT 实验

### 默认做法

- 对随机训练 / 随机优化：做多次独立运行，改变随机种子。
- 对 Monte Carlo 类仿真：明确试验次数与抽样分布。
- 对跨 case benchmark：报告跨 case 的分布，而不是只挑最好的几个 case。
- 对硬件测量：报告重复测量次数、仪器精度或波动范围。

### 报告方式

优先选一种清晰、统一的方式：
- 近似对称分布：`mean ± std` 或 `95% CI`
- 明显偏态 / heavy-tail：`median [IQR]`
- case 数不大但必须展示离散性：同时给散点 / 范围

不要只写：
- 最好一次结果
- 只给平均值不给离散性
- “多次运行结果类似”但不写 n 和统计口径

## 4. 数据划分与 benchmark 纪律

### 数据驱动任务

对 communications / signal processing、EDA 学习式方法、embedded/IoT 学习部署任务尤其重要：
- 明确 train / val / test 的边界，不要在 test 集上调参。
- 小样本时可用 cross-validation，但最终仍要保留独立 test 或明确说明没有真正 held-out test。
- 时序 / 电力 / 控制数据优先按时间、场站、设备或拓扑做分割，避免随机打散造成泄漏。
- 合成数据训练、真实数据测试时，要明确 domain gap。
- benchmark 若有官方 split，优先遵守；若自定义 split，要可复现。

### 非数据集型 benchmark

对 power systems、power electronics、EDA、control 等更多是 case / 工况 / 设计集验证的任务：
- 区分开发用 case 与最终报告 case。
- 不要根据 test case 结果反复改模型却不披露。
- 多系统 / 多工况结论要说明覆盖范围，而不是把一个标准例子当成普适结论。

## 5. baseline、调参与消融公平性

### baseline 公平性

至少确保以下项目对齐：
- 同一数据 / 同一工况 / 同一 benchmark 集
- 同一约束条件：控制周期、面积预算、功耗预算、算力预算、信道知识、预测信息
- 相近的调参与搜索投入
- 同样的 early stopping / 收敛标准 / timeout 规则
- 同样的失败计入方式

### 调参与预算披露

如果自己的方法用了更大搜索预算、更多预训练数据、更强硬件或更长运行时间，必须写明。

建议至少披露：
- 搜索方法：grid / random / Bayesian / manual
- 搜索空间大小或关键超参数范围
- 每个方法的最大训练轮数 / 最大求解时间 / 最大迭代次数
- 是否使用作者公开权重 / 公开代码默认参数

### 消融纪律

消融不是“拿掉一个模块看降多少”就完了。至少回答：
- 核心收益来自哪个机制
- 去掉后是否仍满足约束
- 性能下降是否伴随复杂度下降
- 若多个模块耦合，是否做组合消融而不只做单模块消融

## 6. 各赛道的验证重点

### Communications / Signal Processing
- SNR sweep、信道失配、导频长度、用户数 / 天线数变化不要缺。
- 若是学习式接收机 / 估计器，强调 train / val / test 分离与跨信道泛化。
- BER / BLER / NMSE 之外，同时交代 latency、memory、online complexity。
- OTA / SDR 不可达时，不要把纯仿真结论说成链路级部署结论。

### Power / Energy Systems
- 重点是跨系统、跨负荷 / 出力场景、跨不确定性水平的可行率与稳定性分布。
- 若使用历史时序或预测模型，避免时间泄漏；训练与评估窗口要分离。
- 约束违背、潮流不可行、N-1 / 安全约束失效要计入失败，而不是丢样本。
- 单个 IEEE case 的好结果不代表可推广到多网络、多时段调度。

### Power Electronics & Drives
- 重点是稳态 + 暂态、参数失配、采样 / 开关频率限制、死区、噪声、延迟。
- 不只报 THD / 纹波平均值；还要看极端工况、恢复时间和是否满足实时实现。
- 硬件或 HIL 中应披露控制器型号、采样率、执行延迟、传感器与测量带宽。
- 单次示波图不等于稳定复现；至少说明重复测试与工况覆盖。

### Circuits / Chips / EDA
- 重点是 benchmark 数量、设计规模覆盖、runtime / memory、QoR 分布。
- 学习式或启发式 flow 要区分单 design 调优与跨 design 泛化。
- 明确 proxy metric 还是 signoff metric；不同节点 / 库 / 约束下不要硬比。
- 若依赖商业工具或私有工艺库，写清不可公开部分，并尽量补公开 flow 证据。

### Embedded / IoT / Control
- 重点是扰动、延迟、丢包、量化误差、长时间运行稳定性。
- 学习控制 / 在线优化要说明 warm-up、重训练频率、部署资源占用。
- 报控制性能时同时报 CPU、RAM、功耗、deadline miss、jitter。
- 单次实板 demo 不足以支撑鲁棒性；要补多轮实验或多工况运行。

## 7. 可复现性披露清单

至少能让别人知道“用什么条件复现”。按证据层级写：

### 通用
- 代码 / 伪代码 / 流程描述是否可得
- 配置文件、关键超参数、随机种子
- 软件版本：Python / MATLAB / Simulink / PLECS / PyTorch / TensorFlow / solver / OpenROAD 等
- 硬件：CPU / GPU / MCU / DSP / FPGA / SDR / board 型号
- 数据、benchmark、测试 case 来源与版本

### Simulation / Software
- 仿真器、求解器、步长、容差、采样时间
- 初始条件、边界条件、噪声模型、扰动注入方式
- 预处理、归一化、数据筛选规则

### HIL / Hardware / Prototype
- 控制板 / 功率级 / 传感器 / 仪器型号
- 时钟、采样频率、控制频率、通信链路设置
- 校准方法、安全限值、保护逻辑
- 环境条件：温度、电源条件、负载条件

### Circuits / EDA
- benchmark 列表、工艺节点、库版本、约束脚本
- flow 步骤、工具版本、随机种子、timeout / 并发设置
- 使用商业库时哪些部分可分享，哪些只能文字披露

### Embedded Deployment
- 编译器、RTOS / firmware 版本、编译选项
- 中断 / 任务调度设置、通信协议、缓存 / 内存限制
- 板级外设和传感器配置

## 8. 何时统计检验有意义，何时不必假装有意义

适合做统计检验的场景：
- 多个独立随机种子运行
- 多个独立 benchmark case / design / data split
- 多次独立测量且样本定义清楚

此时可考虑：
- 配对比较优先于非配对比较（同一 case 上比较多个方法）
- 同时报 effect size 和 CI，不要只报 p-value
- 样本很小或分布奇怪时，谨慎解释“显著性”

不太适合硬做显著性检验的场景：
- 只有一个 hardware prototype
- 只有一个超大 benchmark 实例
- 样本并不独立，却被当独立重复计数
- 反复调参后只保留最终一次结果

这类情况更好的做法是：
- 增加工况 / 设计 / 时间窗覆盖
- 报告范围、失败案例和边界条件
- 诚实写“当前证据不足以支撑统计显著性结论”

## 9. 最小报告块

在实验计划或结果摘要里，至少加一个短块：

- `validation unit`：seed / case / design / measurement
- `n`：
- `variance / CI reporting`：
- `data or scenario split discipline`：
- `baseline tuning fairness`：
- `reproducibility disclosure`：toolchain / hardware / library / dataset / benchmark version
- `failure accounting`：超时 / 失稳 / 不可行 / 不收敛如何记入

如果这些字段写不出来，说明实验计划还不够扎实。