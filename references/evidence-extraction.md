# Evidence Extraction

## 目录
- 0. 核心原则
- 1. 三种证据层级怎么抽
- 2. 哪些结论分别需要多强证据
- 3. 实用抽取 schema
- 4. 抽取动作顺序
- 5. 最低交付

目标不是“总结一篇论文”，而是把 abstract、网页、PDF 里的证据压成可横向比较的结构化字段，并明确哪些字段仍未确认。

## 0. 核心原则

- 先摘证据，再写判断；不要先下结论再回填材料。
- 区分作者声称、你能确认的事实、你自己的推断。
- 把证据强度写出来：abstract-only、partial full-text、full-text。
- 能引用原句或原表时，优先保留短证据摘录，避免二次误读。

## 1. 三种证据层级怎么抽

### A. Abstract-only（E1）

通常能确认：
- 研究问题 / 任务类型
- 粗粒度方法家族
- 论文声称的创新方向
- 粗粒度实验对象或场景
- novelty risk 线索

通常不能确认：
- 精确模型结构、控制律、损失函数
- baseline 具体配置
- dataset 切分、训练预算、硬件参数
- 指标定义与统计显著性

适合用途：画地图、选 shortlist、做 warning 标记、提取下一轮 query。

### B. Partial full-text（E2）

包括：正文部分可读、supplement、appendix、code README、slides、poster、项目页、部分章节截图。

通常能确认：
- 方法主干与主要模块
- 部分 benchmark / dataset / hardware 线索
- 某些 baseline、指标、实验场景
- 作者自己承认的部分限制

仍要保留谨慎：
- 如果关键实验表格、实现细节、评价协议缺失，就不要写成“已完全可比”。
- 如果只有项目页或 slides，不要自动等价为全文精读。

适合用途：初步实验设计、baseline 候选筛选、找最需要补的正文位置。

### C. Full-text（E3 / E4）

合法可读全文时，才进入强证据抽取。

应尽量确认：
- 问题边界与关键假设
- 方法机制与创新单元
- 数据 / benchmark / simulator / hardware /工况
- baseline、公平性、调参预算、统计方式
- 限制、失效边界、部署代价

如果还拿到可复用 setup（代码、公开 benchmark、明确 protocol），可升到 E4。

## 2. 哪些结论分别需要多强证据

| 任务 | 可接受的最低证据 | 说明 |
|---|---|---|
| prior-art framing | E1 起步，关键最近邻最好到 E2/E3 | E1 可以判断主线与 novelty risk；真正的最近邻站位最好补到正文或至少 partial full-text |
| novelty claims | E3 for closest papers | 没看过最接近工作的正文，不要把“可能没做过”写成“确定没人做过” |
| experiment design | E2 起步，最终 baseline/protocol 以 E3/E4 为准 | supplement / code / appendix 能帮助起草；正式实验对比应尽量基于全文或官方 protocol |
| baseline selection | E3 或 benchmark 官方文档 | 只看 abstract 不足以决定 baseline 细节；E1 只能作为候选线索 |

实务上可这样降级：
- `E1`：用于 map / warning / query expansion
- `E2`：用于 draft experiment plan，但要列缺失项
- `E3-E4`：用于正式 prior-art 对比、baseline 选择、创新风险判断

## 3. 实用抽取 schema

每篇关键文献至少抽下面字段；未知就写未知，不要补写。

| 字段 | 要记录什么 | 常见证据位置 |
|---|---|---|
| problem | 具体对象、任务、场景、为什么重要 | title / abstract / intro |
| method | 方法主干、模块、控制或优化框架 | abstract / method / figure |
| innovation | 相对最近邻到底新增什么 | abstract / intro / contributions / ablation |
| assumptions | 系统模型、先验、数据前提、理想化条件 | system model / problem formulation / setup |
| dataset / benchmark | 数据集、测试系统、公开基准、simulator、hardware | experiment section / appendix / repo |
| metrics | 主指标、辅指标、资源代价指标 | experiment tables / benchmark protocol |
| setup | 工况、切分、训练预算、采样率、平台、器件、工艺、HIL / prototype 条件 | experiment / appendix / repo / supplement |
| limitations | 作者承认的限制、未覆盖场景、可迁移边界 | discussion / conclusion / failure cases |
| risks | 你对 comparability、novelty、resource、evidence 的风险判断 | 你基于全文或 partial full-text 的综合判断 |

推荐输出形状：
- `事实`：直接来自 paper 的字段
- `证据摘录`：1-3 条最关键原句 / 表格结论 / 页面片段
- `判断`：这篇 paper 对当前研究方向的意义、风险、可复用性

## 4. 抽取动作顺序

1. **先记元信息**：标题、年份、venue、版本、获取路径、证据等级。
2. **再记事实字段**：problem / method / assumptions / setup / metrics。
3. **单独记 innovation**：只写 paper 真正新增的那一小块，不要把整篇重述成创新。
4. **最后记 limitations / risks**：区分作者承认的限制和你自己的比较判断。
5. **跨 paper 汇总**：把关键字段放进矩阵或 `assets/literature-evidence-pack-template.md`，不要让信息停留在单篇卡片里。

如果是从 abstract 开始：
- 先填 `problem`、粗粒度 `method`、`innovation claim`、`unknowns`。
- 一旦拿到 partial / full-text，再回填 assumptions、setup、metrics、limitations。

## 5. 最低交付

做完 evidence extraction 后，至少应有：
- 每篇 paper 的证据等级与获取路径
- 上面 9 个 schema 字段的已知 / 未知列表
- prior-art framing 可直接复用的事实与证据摘录
- novelty claim 仍缺哪些 closest-paper 证据
- experiment design 可直接拿走的 benchmark / metric / setup 线索
- baseline selection 里哪些还是候选、哪些已到 E3/E4 可落地