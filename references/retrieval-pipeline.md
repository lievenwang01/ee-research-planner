# Retrieval Pipeline

## 目录
- 0. 作用范围
- 1. 分层证据流程
- 2. 工具 / skill 路由
- 3. 最低交付
- 4. 合规边界

这份参考讲“怎么把文献计划真正落到合法证据”。检索式设计与 shortlist 收敛细节仍看 `literature-strategy.md`；需要把摘要 / 网页 / PDF 变成结构化证据时读 `evidence-extraction.md`。

## 0. 作用范围

目标不是一次性拿全所有全文，而是按证据层级推进：
1. metadata search
2. shortlist construction
3. OA / full-text discovery
4. authorized database retrieval
5. user-provided DOI / citation / PDF lane

默认先广覆盖，再收敛，再精读。不要把“能不能直接看 IEEE 全文”当成唯一入口。

## 1. 分层证据流程

### Layer 1：Metadata Search

用途：画地图、找 recurring terms、venue、作者群、benchmark 名、warning papers。

优先动作：
- 先按 `literature-strategy.md` 写清 query 组。
- 用 `scripts/search_openalex.py` 拉一批结构化 metadata。
- 再用 `scripts/normalize_paper_records.py` 统一 schema，必要时用 `scripts/build_literature_cards.py` 生成初始卡片。

适合回答：
- 这个方向最近几年主要在哪些 venue 出现？
- 高频关键词 / 同义词 / 缩写是什么？
- 哪些 paper 值得进 shortlist？

不适合回答：
- 具体算法细节
- 精确 baseline 配置
- 公式、损失、控制律、硬件 setup

### Layer 2：Shortlist Construction

从 mapping pool 收敛到 8-15 篇 shortlist，再选 3-6 篇 deep-read set。

操作顺序：
1. 先按 relevance / evidence / comparability / novelty-risk / practicality 打分。
2. 强制保留几类 paper：
   - 最新代表作
   - 经典强 baseline
   - 实验最透明的 paper
   - warning paper
3. 对每篇标：用途标签 + 当前证据等级 + 下一步补证据动作。

这一层先判断“为什么要读这篇”，不要急着写长摘要。

### Layer 3：OA / Full-text Discovery

当 shortlist 已稳定，再为关键 paper 找合法可读正文或补充材料。

优先顺序：
1. DOI 落地页 / publisher landing page
2. arXiv / TechRxiv / institutional repository
3. 作者主页 / lab 页面 / accepted manuscript
4. project page / code / appendix / supplement / poster / slides

本层重点拿到：
- 方法框架图
- 实验设置
- benchmark / dataset / simulator / hardware 细节
- baseline 名与可比性边界
- 作者自己承认的限制

注意：`scripts/search_openalex.py` 只提供 metadata 与 OA 线索，不会替你抓正文。

### Layer 4：Authorized Database Retrieval

只有在用户自己的授权已存在时，才进入 IEEE / ACM / Elsevier / Springer / CNKI / 万方 / 学校图书馆等数据库正文检索。

允许做的事：
- 用已登录浏览器访问用户有权限的页面
- 导出 citation、下载合法可访问 PDF、记录章节证据
- 读取数据库内的 abstract / references / cited-by 线索

不允许做的事：
- 绕过登录
- 绕过付费墙
- 用镜像站、破解站、分享口令或任何 bypass 手段

如果授权不可用，就明确降级到 E0 / E1 / E2 输出，不要假装已精读全文。

### Layer 5：User-provided DOI / Citation / PDF Lane

用户直接给 DOI、BibTeX、题目、截图、PDF 时，优先走这一条。

处理顺序：
1. 先确认版本：conference / journal / preprint / thesis。
2. 记录 DOI 与 PDF 标题是否一致。
3. 把材料落成文献卡片，再进入 evidence extraction。
4. 如果这是最近邻工作，优先拿它做 novelty-risk 与 baseline 判断。

这一条通常是最快进入 deep-read 的入口。

## 2. 工具路由

### `WebSearch`

适合：
- 关键词还不稳定时做语义扩展
- 找 research-paper / PDF / GitHub / author page / company or lab 页面入口
- 找”某问题 + 某约束”下的近邻网页与论文标题列表

强项：召回广，适合从模糊 query 找 paper 邻域和验证关键词覆盖。

不要把它当成：全文精读工具。找到入口后，仍要回到卡片、矩阵和证据抽取。

### `WebFetch`

适合：
- 读取已知 URL 的公开网页、landing page、作者主页、project page、arXiv 页面
- 从 article / lab / repository 页面抽取可读正文

强项：对静态公开页面提取干净，适合补 OA 页面与项目页细节、抓取作者公开的 accepted manuscript。

不要把它当成：受限数据库登录器（IEEE/ACM paywall 页面拿不到全文）。

### 本地 PDF / 用户提供文件

用户提供 PDF 或本地路径时，用 `Read` 工具直接读取。优先走 user-provided lane，不再额外搜索。

读完后直接进入 evidence extraction；不需要先 summarize 再精读，一步到位即可。

### 批量 metadata 获取

用 `scripts/search_openalex.py` 批量拉 metadata，再用后续脚本标准化和建卡片。适合需要处理 20+ 篇候选的场景。

单篇或少量文献直接用 `WebSearch` + `WebFetch` + 手动卡片，不必跑脚本。

### 推荐组合

| 场景 | 推荐工具组合 |
|---|---|
| 关键词扩展 + 找文献入口 | `WebSearch` |
| 读公开网页 / OA 页 / 项目页 | `WebFetch` |
| 用户提供 PDF / 本地文件 | `Read` |
| 批量 metadata → 卡片脚手架 | `scripts/search_openalex.py` → `normalize_paper_records.py` → `build_literature_cards.py` |
| 已授权数据库正文（用户自行登录后提供内容） | 接收用户粘贴的内容，进入证据抽取流程 |

## 3. 最低交付

每轮 retrieval 至少交付：
- 当前 query / lane / 目标产物
- mapping pool → shortlist → deep-read set
- 每篇 paper 的用途标签与证据等级
- 可确认的 OA / authorized / user-provided 获取路径
- 仍缺的全文、supplement、benchmark、baseline 证据
- 下一轮最值钱的补证据动作

## 4. 合规边界

- 允许：公开信息、开放获取、用户已授权访问、用户提供 DOI / citation / PDF。
- 不允许：任何 paywall bypass。
- 如果只能拿到 metadata / abstract，就明确标 E0 / E1，不要把未知细节写成事实。
- 脚本层目前只做 metadata 检索、标准化与卡片脚手架；它们不会自动完成全文抓取或深度语义抽取。