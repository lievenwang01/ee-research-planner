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

## 2. 工具 / skill 路由

### `exa`

适合：
- 关键词还不稳定时做语义扩展
- 找 research-paper / PDF / GitHub / author page / company or lab 页面
- 找”某问题 + 某约束”下的近邻网页与论文入口

强项：召回好，适合从模糊 query 找 paper 邻域。

不要把它当成：正文精读工具。找到入口后，仍要回到卡片、矩阵和证据抽取。

### `jina-reader`

适合：
- 读取公开网页、landing page、作者主页、project page
- 用 search mode 做网页级检索并直接拿干净正文
- 从 article / lab / repository 页面抽取可读 markdown

强项：网页提取干净，适合补 OA 页面与项目页细节；也适合在不想暴露本机出口 IP 时读取网页。

不要把它当成：受限数据库登录器，或本地 PDF 深度解析器。

### `summarize`

适合：
- 已经拿到 URL 或本地 PDF 后，快速做长文压缩
- 先对 OA PDF、用户提供 PDF、长网页做高密度摘要
- 在精读前先拿一版结构化 overview

强项：对长文和本地文件很省时间，是”已拿到材料后”的压缩工具。

不要把它当成：metadata 搜索器。先找材料，再 summarize。

### `Agent Browser`

适合：
- 需要登录、点击、翻页、下载、展开引用、切换标签页
- 用户已授权访问的 IEEE Xplore / publisher / library 页面
- 页面强依赖 JS，普通抓取拿不到内容

强项：交互式网页自动化；可在已授权会话里完成合法 retrieval。

升级条件：静态公开页优先用 `jina-reader`；只有遇到登录、复杂 JS 或必须点击导出时再升级到 `Agent Browser`。

### 推荐组合

| 场景 | 推荐工具组合 |
|---|---|
| 关键词扩展 + 找文献入口 | `exa` |
| 读公开网页 / OA 页 / 项目页 | `jina-reader` |
| 已拿到 URL / PDF 后快速压缩 | `summarize` |
| 授权数据库 / 交互式下载 | `Agent Browser` |
| 批量 metadata → 卡片脚手架 | `scripts/search_openalex.py` → `normalize_paper_records.py` → `build_literature_cards.py` |

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