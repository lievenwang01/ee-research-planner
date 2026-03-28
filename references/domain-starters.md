# Domain Starters

用于两类情况：
- 用户方向已经比较具体，但另一个 agent 容易把问题说泛。
- 你已经知道主赛道，却需要快速补齐该子方向的 scoping、检索和实验抓手。

不是为了替代通用流程；而是为了让常见子方向少踩几个坑。

## 1. 配电网韧性 / 极端天气后故障恢复 / 关键负荷保供

### 先把问题切片切对
这类题目最容易混成四条线，先分清：
1. **灾前 hardening / planning**：加固、投资、设备选址。
2. **灾中 / 灾后 restoration operation**：故障隔离、网络重构、修复调度、孤岛运行、负荷恢复。
3. **resilience assessment**：韧性指标设计、恢复曲线、服务损失刻画。
4. **分布式控制 / 调度实现**：多智能体、分层控制、边缘协同。

如果用户说的是“极端天气后故障恢复 + 关键负荷保供”，默认先站在 **post-event restoration / operation**，把其他三条线作为：
- 指标来源（assessment）
- 方法来源（control / optimization / learning）
- 扩展方向（hardening）

### 至少补齐的 6 个边界
- 网络层级：distribution feeder / microgrid / active distribution network
- 时间尺度：单阶段恢复，还是 multi-period sequential restoration
- 资源对象：开关操作、抢修队、DG / ESS / mobile power source、孤岛能力
- 关键负荷定义：医院 / 通信 / 水厂等优先级，还是抽象负荷分层
- 不确定性：故障位置、修复时间、负荷波动、DER 出力、通信可见性
- 证据层级：标准算例仿真、时序仿真、闭环调度仿真、HIL / 数字孪生

### 文献检索时优先盯住的词
**问题词**
- `distribution network resilience`
- `service restoration`
- `post-disaster restoration`
- `critical load restoration`
- `resilient distribution system restoration`
- `distribution network reconfiguration after extreme event`

**机制词**
- `switching reconfiguration`
- `repair crew dispatch`
- `DG dispatch` / `mobile energy storage`
- `microgrid islanding`
- `stochastic optimization` / `robust optimization`
- `multi-agent reinforcement learning`

**指标 / 约束词**
- `unserved energy` / `ENS` / `EENS`
- `restoration time`
- `critical load pickup`
- `fairness`
- `radiality`
- `switching operation limit`
- `partial observability`
- `extreme weather`

**检索提醒**
- 把 `resilience` 与 `reliability` 区分开；前者通常强调恢复轨迹和极端事件，后者更偏长期统计停电指标。
- 把 `restoration` 与 `hardening` 区分开；不要把灾前投资类论文当成最接近 prior art。
- 同时搜 `distribution system restoration`、`service restoration`、`critical load restoration`，因为不同社群用词不同。

### prior-art framing 时优先看的 4 组工作
1. **韧性指标 / 恢复曲线类**：告诉你论文通常怎么定义“恢复得更好”。
2. **网络重构 / 负荷恢复优化类**：是最常见主线。
3. **抢修调度 + 重构 + DER 协同类**：往往更接近“极端天气后保供”的真实问题。
4. **学习式 / 分布式恢复类**：容易看起来新，但要检查是否真的处理了更强约束。

### 这个方向最常见的 novelty traps
- 把 **灾前 hardening** 和 **灾后 restoration** 混成一个口号题，最后问题边界失焦。
- 只报总恢复负荷或 ENS，却不刻画 **关键负荷优先级、恢复时序、服务公平性**。
- 忽略 **径向结构、孤岛可行性、电压 / 潮流约束**，做成了过于理想化的恢复题。
- 用了更复杂的求解器 / 学习器，但没有证明比“强优化基线 + 相同约束”更值得。
- 比较对象的灾损模型、可见性假设、DER 可用性不同，却硬说自己更优。

### 最小可行实验包
- **系统**：IEEE 33 / 69 / 123-bus 之类公开配电网算例（至少 1-2 个）。
- **场景**：极端天气后若干损毁场景；写清线路故障、开关可用性、DG / ESS 状态、关键负荷分层。
- **baselines**：
  - 经典服务恢复 / 重构方法
  - 韧性加权恢复方法或多目标优化方法
  - 若你走学习路线，再补一个可合法复现的学习近作
- **指标**：关键负荷保供率、恢复时间、ENS / EENS、开关 / 抢修操作次数、求解时间、可行率。
- **必须补的检查**：
  - 多场景而不是单一故障图
  - 是否满足径向 / 潮流 / 电压等工程约束
  - 对不确定修复时间或 DER 波动是否敏感

### 候选 gap 的常见落点
- **constraint gap**：已有工作默认全局可见、修复时间确定、DER 始终可用，但真实灾后并非如此。
- **evaluation gap**：大量论文只在静态故障集上比成本，没有比较恢复轨迹和关键负荷服务质量。
- **deployment gap**：方法在模型里有效，但求解时间、信息需求、协调复杂度不适合灾后调度。
- **scope gap**：主流工作只做 feeder-level 恢复，缺少与微网孤岛 / 移动电源协同的更真实场景。

---

## 2. 低 SNR 条件下 RIS 辅助 MIMO 信道估计（导频开销受限）

### 先把问题切片切对
RIS 相关题目很容易混成：
1. **纯信道估计**：估 cascaded / effective CSI。
2. **beam training / beam alignment**：目标是快速找波束，不一定显式重建完整 CSI。
3. **joint estimation + reflection / detection**：估计和接收机 / 反射控制联合设计。
4. **RIS 硬件架构差异**：fully passive / semi-passive / active RIS。

如果用户明确说“低 SNR + RIS 辅助 MIMO + 信道估计 + 导频开销要小”，默认先压到：
- **主问题**：在低 SNR、导频预算有限时估计 RIS-assisted MIMO channel / cascaded channel
- **副问题**：估计误差是否足以支撑后续检测 / 波束赋形

### 至少补齐的 7 个边界
- 上下行与双工：uplink / downlink，TDD / FDD
- 用户场景：single-user 还是 multi-user
- 信道类型：narrowband / wideband，Rayleigh / geometric mmWave / correlated channel
- 估计对象：direct channel、RIS-BS、RIS-UE、cascaded channel、effective channel
- 导频预算定义：pilot symbols、RIS reflection patterns、time slots、training frames 到底算哪一个
- RIS 架构：fully passive、semi-passive、active；是否额外有 sensing elements
- 证据层级：纯仿真、软件 benchmark、OTA / SDR 原型

### 文献检索时优先盯住的词
**问题词**
- `RIS aided MIMO channel estimation`
- `RIS-assisted channel estimation`
- `cascaded channel estimation RIS`
- `few-pilot RIS channel estimation`
- `low-SNR RIS channel estimation`

**机制词**
- `compressed sensing`
- `sparse recovery`
- `tensor decomposition`
- `bilinear estimation`
- `AMP` / `VAMP` / `BiG-AMP`
- `deep unfolding`
- `model-driven deep learning`
- `semi-passive RIS`

**指标 / 约束词**
- `pilot overhead`
- `NMSE`
- `BER`
- `spectral efficiency`
- `latency`
- `complexity`
- `memory`
- `quantized phase`
- `channel mismatch`

**检索提醒**
- 低 SNR 与低导频预算都要进 query；只搜 `RIS channel estimation` 很容易掉进常规高 SNR 设定。
- 同时搜 `cascaded channel estimation` 与 `effective channel estimation`，两类论文默认目标不同。
- 对学习式方法，加搜 `generalization`、`distribution shift`、`training overhead`，不然很容易只看到离线仿真最优。

### prior-art framing 时优先看的 4 组工作
1. **经典 / 解析基线**：LS、MMSE 及其长导频设定。
2. **稀疏 / 压缩感知类**：利用角域或结构先验降训练开销。
3. **双线性 / 张量 / 因子分解类**：针对 cascaded structure 建模。
4. **hybrid / unfolded / learning-based 类**：常见于低 SNR，但要严查泛化与训练成本。

### 这个方向最常见的 novelty traps
- 只说“导频更少”，却没有把 **RIS pattern 数、时隙数、导频符号数** 统一记账。
- 把 **fully passive RIS** 与 **semi-passive / active RIS** 放在一个开销表里直接比较。
- 只在理想稀疏、完美统计先验或高相关结构下有效，却声称普适低 SNR 优势。
- 只报 NMSE，不检查估计是否真的改善后续检测 / 波束赋形 / 频谱效率。
- 用大模型或重训练换来增益，但不交代 offline training cost、在线推理复杂度和存储。
- 把 narrowband 结果外推到 wideband / mobility / multi-user，却没有重新做可比验证。

### 最小可行实验包
- **信道设定**：先固定一套主设定（例如 narrowband RIS-assisted MIMO 或几何稀疏 mmWave），再扩展；别一开始 wideband + mobility + multi-user 全上。
- **SNR 扫描**：显式覆盖低 SNR 区间，例如从明显低信噪比到中低信噪比。
- **pilot budget 扫描**：导频长度 / RIS 配置数 / frame 数都要单独或联合扫描。
- **baselines**：
  - LS / MMSE 等经典基线
  - 一个结构化稀疏或双线性强基线
  - 若你走学习路线，再补一个近期 hybrid / unfolding 近作
- **指标**：NMSE、BER / BLER（下游任务）、pilot overhead、runtime、memory。
- **必须补的检查**：
  - channel mismatch / correlation / quantized phase / imperfect sparsity
  - 不同 RIS 单元数、天线数、用户数下的复杂度扩展
  - 训练分布与测试分布不一致时是否崩塌

### 候选 gap 的常见落点
- **constraint gap**：已有方法在低导频下仍默认较高 SNR、已知统计先验或半主动硬件。
- **comparability gap**：不同论文对 overhead 记账方式不同，难直接横比。
- **deployment gap**：估计准确，但在线复杂度、内存或硬件假设不适合真实 RIS 链路。
- **evaluation gap**：很多工作只做 NMSE，没有证明 downstream receiver / beamforming 受益。

### 收敛建议
如果 prompt 还没限定，优先收敛成一条更可做的题目骨架：
- `低 SNR + 小导频预算 + 某一类 RIS 架构 + 某一类信道模型 + 某一级证据层级`

例如先压成：
- 在 **fully passive RIS-assisted narrowband MIMO** 下，研究 **低 SNR 与小导频预算** 条件下的 **cascaded channel estimation**；比较结构化基线、hybrid 方法与学习式近作，并把 **NMSE + 下游 BER + overhead + complexity** 一起评估。

---

## 3. 功率变换器 / 电机驱动控制（高效率 + 快动态 + 工程约束）

### 先把问题切片切对
这类题目最容易混成四条线，先分清：
1. **拓扑 / 器件线**：DC-DC、逆变器、整流器、PFC、Si / SiC / GaN 选型与参数。
2. **控制 / 调制线**：电流 / 电压 / 转速 / 转矩控制，PWM / SVPWM / MPC / 观测器。
3. **非理想与可靠性线**：死区、延迟、饱和、热、EMI、参数漂移、寿命。
4. **系统场景线**：并网变流器、车载驱动、伺服、电池接口、可再生能源接口。

如果用户只说“power electronics & drives”，默认先站在 **固定应用对象 + 固定拓扑下的控制问题**，把器件 / 拓扑变化当边界条件，而不是一开始把“控制、器件、热、EMI、拓扑”全混成一个大口号题。

### 至少补齐的 8 个边界
- 应用对象：PMSM / IM drive、grid-tied inverter、DC-DC、OBC、PFC 等到底是哪类
- 拓扑与额定：两电平 / 三电平、功率等级、母线电压、电流范围
- 器件与频率：Si / SiC / GaN、开关频率、采样频率、控制更新频率
- 控制层级：内电流环、外速度 / 电压环、转矩控制、并网支撑目标
- 工况范围：启动、突加负载、低速 / 高速、弱磁区、回馈、轻载 / 满载
- 非理想因素：死区、数字延迟、参数失配、磁饱和、热限制、滤波约束
- 实现平台：DSP / MCU / FPGA，定点 / 浮点，传感器数量与分辨率
- 证据层级：纯仿真、HIL、小功率样机、电机台架、长时热 / 可靠性测试

### 文献检索时优先盯住的词
**问题词**
- `power converter control`
- `motor drive control`
- `PMSM drive`
- `grid-tied inverter control`
- `high switching frequency converter`
- `wide speed range motor drive`

**机制词**
- `field-oriented control` / `FOC`
- `direct torque control` / `DTC`
- `finite control set MPC`
- `continuous control set MPC`
- `dead-time compensation`
- `disturbance observer`
- `sensorless control`
- `digital delay compensation`
- `SiC` / `GaN` / `wide bandgap`

**指标 / 约束词**
- `efficiency`
- `THD`
- `torque ripple`
- `current ripple`
- `dynamic response`
- `switching loss`
- `thermal stress`
- `computational burden`
- `parameter uncertainty`

**检索提醒**
- 把 `topology`、`control`、`device` 三类词混着搜，但输出时别把它们混成一个“全都做”的题。
- 对驱动题，同时搜 `PMSM`、`IPMSM`、`induction motor`、`servo drive`，因为不同社群默认对象不同。
- 对学习式 / 智能控制题，补搜 `real-time implementation`、`DSP`、`HIL`、`experimental validation`，过滤掉只在理想仿真里成立的工作。

### prior-art framing 时优先看的 4 组工作
1. **经典控制 + 调制基线**：PI / PR、FOC、DTC、SVPWM 等。
2. **模型增强控制类**：MPC、observer-based、adaptive / robust control。
3. **非理想感知类**：死区补偿、延迟补偿、参数失配、热 / EMI / 可靠性约束。
4. **实现 / 协同设计类**：WBG 器件、高频运行、数字实现、HIL / 样机验证。

### 这个方向最常见的 novelty traps
- 把 **新控制器** 建在过于理想的平均模型上，却不测死区、延迟、参数漂移、饱和。
- 只在单一速度点 / 负载点报结果，却声称 **宽工况** 优势。
- 比较对象的开关频率、采样频率、调参 effort 或硬件平台不同，结果不公平。
- 只报稳态误差或纹波，不报 **效率 / THD / 热应力 / 计算负担**。
- 把驱动题做成“换一个优化器”，但没有证明它能在真实控制周期内跑起来。
- 用 SiC / GaN 当卖点，却完全忽略寄生参数、EMI、dv/dt 副作用和热管理。

### 最小可行实验包
- **对象**：固定 1 个明确对象（例如两电平逆变器-PMSM 驱动，或某类 DC-DC / 并网逆变器），不要拓扑和应用一起飘。
- **工况**：至少覆盖稳态 + 给定 / 负载突变 + 参数失配；若是驱动题，再补低速 / 高速或弱磁区。
- **baselines**：
  - 一个行业常用强基线（PI/FOC、PR、电流环 + SVPWM 等）
  - 一个最近邻高级方法（MPC / observer-based / robust / sensorless 近作）
- **指标**：动态响应、稳态误差、纹波 / torque ripple、THD / efficiency、开关损耗或热代理指标、runtime / memory / feasible control period。
- **必须补的检查**：
  - 参数漂移、死区、采样 / 计算延迟
  - 多工况而不是单点
  - 至少 HIL 或小功率实验台；若做不到，明确只是 simulation evidence

### 候选 gap 的常见落点
- **constraint gap**：已有方法默认连续控制、无限算力或理想测量，不适合实际 DSP / MCU。
- **evaluation gap**：只看误差，不看效率、热、EMI、长期稳定性。
- **deployment gap**：仿真有效，但控制周期、调参难度、传感需求不适合真实驱动 / 变换器。
- **integration gap**：控制和器件 / 拓扑 / 热设计割裂，没有体现 high-frequency / WBG 场景的真实 trade-off。

### 收敛建议
如果 prompt 还很泛，优先收敛成：
- `固定应用对象 + 固定拓扑 + 固定控制层级 + 明确非理想因素 + 明确证据层级`

例如先压成：
- 在 **SiC 两电平逆变器驱动 PMSM** 的场景下，研究 **宽速域 + 参数失配 + 数字延迟** 下的电流 / 转矩控制；比较经典 FOC 基线与最近邻高级控制方法，并把 **动态性能 + efficiency/THD + runtime + 实验可实现性** 一起评估。

---

## 4. 资源受限嵌入式 / IoT / 控制闭环系统（实时性 + 能耗 + 可靠性）

### 先把问题切片切对
这类题目最容易混成四条线，先分清：
1. **端侧平台线**：MCU / SoC / RTOS、任务调度、内存 / 功耗预算。
2. **通信网络线**：BLE / LoRa / Wi-Fi / TSN / CAN / mesh，时延、丢包、同步。
3. **估计 / 控制线**：状态估计、事件触发控制、容错控制、边缘决策。
4. **部署运维线**：OTA、掉线恢复、安全、日志、现场可维护性。

如果用户只说“embedded / IoT / control”，默认先站在 **资源受限闭环系统**：先把被控对象、控制周期、端侧资源和网络约束说清，再决定是不是需要 TinyML、边云协同或复杂协议栈。很多“智能 IoT”题其实只是监测，不是控制。

### 至少补齐的 8 个边界
- 被控对象：环境监测、移动机器人、无人机、电机、楼宇、工业过程，到底闭环控什么
- 硬件平台：MCU / SoC 型号、RAM / Flash、主频、是否有 RTOS / 硬件加速
- 时间预算：采样周期、控制周期、deadline、可接受 jitter / worst-case latency
- 网络约束：协议、拓扑、链路质量、丢包、时钟同步、是否多跳
- 能源约束：电池 / 能量采集、占空比、休眠策略、平均功耗预算
- 架构位置：纯端侧、边缘节点、网关协同、云仅监控还是参与闭环
- 失效模型：链路中断、节点掉电、传感器漂移、攻击 / 干扰、OTA 失败
- 证据层级：离线仿真、网络仿真、HIL、真实节点实验、现场试点

### 文献检索时优先盯住的词
**问题词**
- `embedded control system`
- `networked control systems`
- `low-power IoT control`
- `edge control`
- `cyber-physical system`

**机制词**
- `event-triggered control`
- `self-triggered control`
- `real-time scheduling`
- `co-design`
- `wireless control`
- `state estimation`
- `TinyML`
- `edge inference`
- `fault tolerant control`

**指标 / 约束词**
- `latency`
- `jitter`
- `packet loss`
- `deadline miss`
- `battery life`
- `energy consumption`
- `stability margin`
- `WCET`
- `memory footprint`

**检索提醒**
- 把 **IoT sensing** 和 **closed-loop control** 区分开；很多 IoT 论文只有采集 / 上云 / 可视化。
- 把 **edge AI** 和 **hard real-time control** 区分开；前者常看平均精度，后者必须看 deadline 和最坏时延。
- 先按物理对象和闭环约束搜，再补协议词；只按 `LoRa` / `BLE` 搜，容易掉进纯通信论文。

### prior-art framing 时优先看的 4 组工作
1. **周期采样的经典嵌入式控制**：固定周期、RTOS / bare-metal、常规控制器。
2. **网络感知 / 事件触发类**：event-triggered、self-triggered、调度-控制协同。
3. **低功耗 IoT / edge intelligence 类**：节能、压缩通信、轻量推理、TinyML。
4. **部署与鲁棒性类**：丢包、同步误差、容错、安全、OTA、现场实验。

### 这个方向最常见的 novelty traps
- 把 **监测 + 上云 + dashboard** 说成控制系统，但没有真实闭环指标。
- 只报平均时延 / 平均能耗，不报 **worst-case latency、jitter、deadline miss、稳定性**。
- 比较对象用不同硬件、不同占空比、不同链路质量，结果不公平。
- 加了 TinyML / 边缘推理，却没有证明闭环性能、能耗或通信成本真的更优。
- 默认链路可靠、时钟完美同步、节点永不掉线，导致方法只在理想网络里成立。
- 只有离线仿真，没有真实节点、HIL 或现场链路证据。

### 最小可行实验包
- **对象**：固定 1 个明确闭环对象（例如无线小车 / 电机 / HVAC / 工业过程），不要把“任意 IoT 场景”写成对象。
- **平台**：固定 1 套端侧硬件 + 1 类网络协议，写清 RAM / Flash / 主频 / 电源条件。
- **baselines**：
  - 一个固定周期的经典控制 / 调度基线
  - 一个最近邻网络感知或事件触发近作
  - 若你走 TinyML / edge inference，再补一个不带学习模块的强基线
- **指标**：控制误差 / 收敛时间 / 超调、deadline miss、latency / jitter、packet delivery、能耗 / battery life、CPU / memory。
- **必须补的检查**：
  - 丢包、时延抖动、节点掉线、传感漂移
  - 多负载 / 多链路质量，而不是单一理想环境
  - 至少真实节点实验或 HIL；若只有仿真，要明确证据边界

### 候选 gap 的常见落点
- **constraint gap**：已有工作默认算力、带宽或供电充足，不适合资源受限节点。
- **evaluation gap**：只看平均精度或平均延迟，没有 worst-case、稳定性和长期能耗。
- **cross-layer gap**：控制、调度、通信、功耗被分开做，缺少真正的协同设计。
- **deployment gap**：论文方法在实验室网络可用，但对掉线、OTA、时钟漂移、维护成本不敏感。

### 收敛建议
如果 prompt 还很泛，优先收敛成：
- `固定被控对象 + 固定端侧平台 + 固定网络条件 + 明确实时 / 能耗预算 + 明确证据层级`

例如先压成：
- 在 **低功耗 MCU + 无线链路** 的闭环场景下，研究 **丢包与抖动存在时** 的事件触发控制 / 调度协同；比较固定周期基线与最近邻近作，并把 **控制性能 + worst-case timing + 能耗 + 真实节点可实现性** 一起评估。

这样更容易形成可写的 direction brief、prior-art framing 和实验计划。

---

## 5. 数字芯片 / 开源 EDA 实现流（RTL→GDS，PPA / timing / congestion 优化）

### 先把问题切片切对
这类题目最容易混成四条线，先分清：
1. **逻辑综合线**：RTL 优化、technology mapping、逻辑重写、面积 / 延迟 / 功耗权衡。
2. **物理实现线**：floorplan、placement、CTS、routing、拥塞 / 时序 / 布线可行性。
3. **预测 / 代理模型线**：时序、拥塞、功耗、DRC 风险的早期估计与 design-space pruning。
4. **flow tuning / 协同优化线**：跨阶段参数调优、脚本搜索、multi-objective flow orchestration。

如果用户只说“芯片 / EDA / 提升 PPA”，默认先站在 **固定一个 flow stage + 固定一个主目标**，例如“placement 后时序 / 拥塞优化”或“综合阶段面积-延迟权衡”；不要一开始把架构、RTL、综合、布局布线、signoff 全混成一个大题。

### 至少补齐的 8 个边界
- 设计对象：算术模块、控制逻辑、RISC-V core、宏块级 block，还是接近 SoC 的集成设计
- flow stage：synthesis、placement、CTS、routing、post-route optimization，到底卡在哪一段
- 主目标：WNS / TNS、面积、功耗、拥塞、DRC、runtime，哪一个是主指标，哪几个只是约束
- 工艺与库：Nangate45、ASAP7、Sky130 或其他公开 PDK / liberty；别把不同 node 混比
- benchmark 来源：OpenROAD-flow-scripts、OpenLane 设计集、ISPD / ICCAD / DAC 公开 benchmark，到底用哪套
- 约束设定：clock period、utilization、die/core size、IO / macro 固定方式、功耗目标是否一致
- 工具链开放性：Yosys / ABC / OpenROAD / OpenSTA / TritonRoute 是否全可复现，还是依赖私有 signoff / 商业 oracle
- 证据层级：脚本级可复现、公开 benchmark 批量实验、ablation、多 seed 稳定性，还是只有单设计 demo

### 文献检索时优先盯住的词
**问题词**
- `open-source EDA`
- `RTL to GDS optimization`
- `OpenROAD flow optimization`
- `physical design optimization openroad`
- `logic synthesis optimization yosys abc`
- `timing congestion co-optimization`

**机制词**
- `technology mapping`
- `logic rewriting`
- `placement optimization`
- `buffer insertion`
- `gate sizing`
- `congestion estimation`
- `timing prediction`
- `design space exploration`
- `reinforcement learning for EDA`
- `graph neural network EDA`

**指标 / 约束词**
- `WNS` / `TNS`
- `total negative slack`
- `wirelength`
- `power`
- `area`
- `routability`
- `DRC violations`
- `overflow`
- `runtime`
- `success rate`

**检索提醒**
- 把 `synthesis`、`placement`、`routing` 分开搜，再补 `cross-stage`；只搜 `EDA optimization` 太泛。
- 同时搜工具名和 benchmark 名，例如 `OpenROAD`、`Yosys`、`ABC`、`OpenLane`、`ISPD`，更容易找到可复现实验。
- 对学习式方法，补搜 `generalization across designs`、`cross-PDK`、`multi-design benchmark`、`reproducible flow`，不然很容易只看到单设计调参故事。

### prior-art framing 时优先看的 4 组工作
1. **经典算法 / 工具内优化类**：综合重写、时序修复、布局布线启发式，是最该先站稳的基线。
2. **代理预测 / 早期估计类**：用 surrogate 预测时序 / 拥塞 / 功耗，减少昂贵完整 flow 次数。
3. **学习式 flow tuning 类**：RL、Bayesian optimization、GNN ranking，但要严查可迁移性与训练成本。
4. **benchmark / reproducibility / open-flow 类**：定义公开任务、统一约束、可复现实验协议，这类工作往往决定比较是否成立。

### 这个方向最常见的 novelty traps
- 把 **综合问题**、**物理问题** 和 **跨阶段协同问题** 混成一个口号，最后 baseline 和指标都对不齐。
- 比较对象用了不同 PDK、不同 liberty、不同 clock / utilization / floorplan 约束，却直接横比 PPA。
- 只拿 **默认 OpenROAD / Yosys 配置** 当 baseline，没有补一个认真调过参的强公开基线。
- 只报 WNS 或面积，却不检查 **routing completion、DRC、overflow、runtime、multi-seed 稳定性**。
- 用 ML / RL 获得增益，但训练 / 搜索成本远高于省下的 flow 成本，且对新设计一换就失效。
- 用后段 signoff 指标当卖点，却依赖不可公开的商业工具 / 私有库，导致别人无法验证。
- 只在 1-2 个设计上有效，却声称对“芯片设计”普适。

### 最小可行实验包
- **设计集**：至少 1 套公开 benchmark，例如 OpenROAD-flow-scripts / OpenLane 常用设计集，覆盖多个规模而不是单一 demo。
- **工艺 / 工具链**：固定公开技术栈，例如 Yosys + ABC + OpenROAD + OpenSTA（必要时加 TritonRoute / OpenRCX），写清版本与脚本入口。
- **baselines**：
  - 官方 / 默认公开 flow
  - 一个强公开基线（例如手工调参或最近邻开源方法）
  - 若你走学习路线，再补一个非学习的强搜索 / 调参基线
- **指标**：WNS / TNS、area、power（若工具链可稳定导出）、wirelength / congestion overflow、DRC / routed completion、runtime、成功率。
- **必须补的检查**：
  - 多设计 + 多 seed，而不是单设计单次运行
  - 固定同一 PDK / liberty / 约束，保证 apples-to-apples
  - 若做预测模型，检查对 held-out designs / 不同规模设计是否失效
  - 若做跨阶段方法，检查前一阶段优化是否把问题转嫁到后一阶段

### 候选 gap 的常见落点
- **comparability gap**：已有工作 benchmark、PDK、约束设定不统一，导致结果难横比。
- **evidence gap**：很多论文只给 proxy metric 或单阶段改善，没有证明最终 routed / timed 结果真的更好。
- **generalization gap**：方法在少量训练设计上有效，但换设计类型、规模或 PDK 就崩。
- **stage-interface gap**：单阶段最优不等于全 flow 最优，前后段目标经常互相打架。
- **deployment gap**：方法理论上提升 PPA，但 runtime、工程接入成本或工具依赖不适合真实开源 flow。

### 收敛建议
如果 prompt 还很泛，优先收敛成：
- `固定设计层级 + 固定 flow stage + 固定公开 PDK / benchmark + 固定主指标 + 明确证据层级`

例如先压成：
- 在 **OpenROAD + Nangate45 公共设计集** 上，研究 **placement 阶段的时序-拥塞协同优化**；比较经典公开基线、强调参基线与最近邻学习式方法，并把 **WNS/TNS + overflow + routed completion + runtime + 多设计泛化** 一起评估。