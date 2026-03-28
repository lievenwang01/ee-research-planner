# Direction Routing

先判定“用户要什么产物”，再判定“主要研究落在哪一层”。这份文档用来把模糊对话快速路由到合适赛道，并避免一上来就泛泛谈创新。

## 0. 先识别任务类型

用户意图通常先落在下面六类之一：

| 用户常见说法 | 先交付什么 |
|---|---|
| 开题、开题报告、开题怎么做 | direction brief + 主赛道 + 检索计划 + 1-2 个可做假设 |
| 选题、题目怎么定、方向怎么收敛 | 候选题目包 + 比较维度 + 风险排序 |
| 综述、文献综述、文献调研 | 检索轴 + 纳入排除标准 + prior-art 分组 / 矩阵 |
| 找创新点、还能怎么创新、创新空间在哪 | 最近邻 prior art + 缺口列表 + 2-4 条 novelty hypotheses |
| 做实验方案、实验怎么设计 | 已选假设 + baseline + 平台 + 变量 + 指标 + 风险 |
| 给你 DOI / 摘要 / PDF 帮我看 | 结构化论文卡片 + 放入矩阵 + 判断与当前问题的距离 |

如果用户说法跨多类，按“最接近最终交付”的那一类先走，再补上前置阶段的缺口。

## 1. 再选主赛道

主赛道按“主要贡献承载层”来定，而不是按标题里出现了多少热门词。

### A. Power / Energy Systems

**常见触发词**
- 电力系统、配电网、微电网、综合能源、源网荷储、需求响应
- 潮流、状态估计、优化调度、故障诊断、负荷预测、暂态稳定、韧性

**通常在研究什么**
- 电网 / 能源系统的 planning、operation、forecasting、protection、coordination、resilience

**优先问清 4 件事**
- 对象是 transmission、distribution、microgrid 还是 energy management。
- 任务是预测、优化、控制、诊断还是稳定性分析。
- 数据来源是公开数据、标准算例、仿真，还是现场 / 企业数据。
- 指标更看重经济性、稳定性、可靠性、韧性、碳排还是计算效率。

**默认实验抓手**
- IEEE 标准算例 / 自建仿真系统
- 历史负荷 / 可再生出力 / 故障场景数据
- 与经典优化器、调度器或预测器对比
- 不确定性、故障、极端场景鲁棒性测试

**容易混淆的相邻赛道**
- 如果主要贡献在变换器控制或驱动，转到 power electronics & drives。
- 如果主要贡献在边缘部署、控制固件或设备协同，转到 embedded / IoT / control。

### B. Power Electronics & Drives

**常见触发词**
- 变换器、逆变器、整流器、DC-DC、MMC、SiC、GaN、WBG
- 电机驱动、PWM、调制、观测器、MPC、热设计、EMI、效率优化

**通常在研究什么**
- converter topology、modulation、control strategy、loss / thermal / EMI、drive system dynamics

**优先问清 4 件事**
- 对象是拓扑、控制律、调制策略、器件选型还是热 / EMI。
- 功率等级、开关频率、母线电压、负载工况是什么。
- 指标主次是效率、纹波、THD、动态响应、损耗、热应力还是可靠性。
- 是否有 PLECS / MATLAB / PSIM / HIL / 小功率样机。

**默认实验抓手**
- 仿真 + 小功率样机 / HIL
- 工况扫描与参数敏感性分析
- 与 PI / SVPWM / FCS-MPC / observer 等基线对比
- 效率、谐波、热、动态响应联合评估

**容易混淆的相邻赛道**
- 如果主要贡献在电网调度、能量管理、系统级运行，转到 power / energy systems。
- 如果主要贡献在 MCU / FPGA 实时实现与系统联调，副赛道可挂 embedded / IoT / control。

### C. Communications / Signal Processing

**常见触发词**
- 调制编码、信道估计、检测、均衡、MIMO、OFDM、语义通信
- 雷达、阵列、波束赋形、目标检测、时频分析、压缩感知、滤波、估计
- ECG / EEG / EMG、生理信号、心拍分类、心律失常识别、可穿戴 biosignal、医学时序分类

**通常在研究什么**
- waveform、receiver、channel / interference modeling、estimation / detection、signal representation、joint comm-sensing
- 也包括以信号表示、特征提取、时序建模、鲁棒分类 / 检测为主的 biomedical signal processing 题目；如果主要贡献承载层在算法、表征、泛化或评估协议，先留在这条赛道

**优先问清 4 件事**
- 场景是无线通信、雷达、感知，还是联合通信感知。
- 核心变量是信道、接收机、波形、估计器、检测器还是 inference model。
- 信道 / 噪声 / 干扰 / mobility 假设是什么。
- 指标是 BER、SER、throughput、latency、spectral efficiency、NMSE、Pd/Pfa 还是复杂度。

**默认实验抓手**
- 合成信道、公开数据集或标准 benchmark
- SNR / 干扰 / mobility / 稀疏度扫描
- 与经典检测器、估计器或近期学习基线对比
- 性能 + 复杂度 + 泛化边界联合评估

**容易混淆的相邻赛道**
- 如果主要贡献在芯片架构、硬件加速器、EDA 支撑，转到 circuits / chips / EDA。
- 如果主要贡献在边缘部署、系统联控或实时嵌入实现，副赛道可挂 embedded / IoT / control。

### D. Circuits / Chips / EDA

**常见触发词**
- 模拟 / 数字 / 混合信号电路、ADC、PLL、SRAM、NoC、加速器
- EDA、PPA、验证、布局布线、时序收敛、低功耗、DFT、容错

**通常在研究什么**
- circuit topology、chip architecture、EDA algorithm、design methodology、verification / optimization flow

**优先问清 4 件事**
- 工作主要落在 circuit、architecture、EDA algorithm 还是 methodology。
- 目标优先级是面积、功耗、延迟、精度、吞吐、可验证性还是设计效率。
- 证据层级是行为级仿真、RTL、门级 / 后仿、benchmark，还是 silicon result。
- 是否受工艺库、EDA 工具、公开 benchmark、开源 RTL 可得性限制。

**默认实验抓手**
- open-source RTL / benchmark 电路 / placement-routing benchmark
- PPA、runtime、收敛质量对比
- 工艺角、噪声、失配、时序边界分析
- 若无流片条件，优先写清“可做到哪一级证据”

**容易混淆的相邻赛道**
- 如果主要贡献是通信算法本身，不要误路由到芯片。
- 如果主要贡献是固件、设备协同或控制闭环，不要误路由到芯片。

### E. Embedded / IoT / Control

**常见触发词**
- MCU、RTOS、边缘计算、IoT、传感器网络、机器人、工业控制、数字孪生
- 状态估计、故障诊断、调度、边缘 AI、在线学习、闭环控制

**通常在研究什么**
- firmware、networked system、embedded inference、closed-loop control、resource-aware deployment

**优先问清 4 件事**
- 对象是 device、firmware、networked system 还是 closed-loop control。
- 是否有实时、功耗、通信、安全或可靠性约束。
- 平台是 STM32 / ESP32 / FPGA SoC / Linux edge / ROS system 还是纯仿真。
- 指标是时延、丢包、控制性能、功耗、稳定性、鲁棒性还是部署成本。

**默认实验抓手**
- software-in-the-loop / hardware-in-the-loop / 实物平台
- 任务负载、网络扰动、时延抖动、异常工况扫描
- 控制性能与资源消耗联合评估
- 长时间稳定性与部署可行性测试

**容易混淆的相邻赛道**
- 如果主要贡献在电网运行优化，转到 power / energy systems。
- 如果主要贡献在器件、拓扑或调制，转到 power electronics & drives。
- 如果主要贡献在电路 / EDA，不要路由到 embedded。

## 2. 跨赛道处理规则

跨赛道很常见，但不要五条线并行开挖。按下面规则落主副赛道：

1. **先找主要贡献承载层**：用户最想写进题目和摘要的创新，落在哪一层就定为主赛道。
2. **副赛道只服务主赛道**：副赛道通常用于补实验平台、约束条件或方法来源，不单独扩成另一条研究主线。
3. **先收窄再扩展**：题目里出现 “AI + 控制 + 通信 + 芯片” 时，先压缩成一个最小问题，再决定哪一层最值得深挖。

## 3. 路由失败时的最小兜底问法

如果仍然分不清，就只追问这 3 个问题：
- 你最想优化 / 解释 / 设计的对象是什么？
- 你希望最后交付的是开题、综述、创新点，还是实验方案？
- 你现在手里最真实可用的资源是什么：数据、仿真、硬件、工具、论文？

拿到这三点后，先给“暂定主赛道 + 理由 + 下一步检索方向”，不要空等完美信息。