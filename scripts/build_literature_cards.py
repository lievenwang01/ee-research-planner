#!/usr/bin/env python3
"""Build markdown literature cards from normalized paper records.

This script creates metadata-first card scaffolds. It does not replace manual evidence extraction.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build markdown literature cards from normalized records.")
    parser.add_argument("--input", required=True, help="Normalized JSON input path.")
    parser.add_argument("--output", help="Markdown output path. Defaults to stdout.")
    parser.add_argument(
        "--title",
        default="文献卡片（metadata bootstrap）",
        help="Document title for the generated markdown.",
    )
    return parser.parse_args()


def load_records(path: Path) -> List[Dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        return [item for item in payload["records"] if isinstance(item, dict)]
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    raise SystemExit("Unsupported input shape. Expected normalized payload with records[].")


def fmt(value: Any, default: str = "待补") -> str:
    if value is None:
        return default
    if isinstance(value, str):
        value = value.strip()
        return value if value else default
    if isinstance(value, list):
        items = [str(item).strip() for item in value if str(item).strip()]
        return "；".join(items) if items else default
    return str(value)


def inferred_scope(record: Dict[str, Any]) -> str:
    if record.get("abstract_available"):
        return "可确认到摘要层；方法细节、baseline、公平性与 setup 仍需正文核实"
    return "仅 metadata；只能判断相关性、年份、venue 与潜在 novelty risk"


def abstract_excerpt(record: Dict[str, Any], max_chars: int = 900) -> str:
    text = (record.get("abstract_text") or "").strip()
    if not text:
        return "未获得摘要文本。"
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def build_card(record: Dict[str, Any], index: int) -> str:
    doi = record.get("doi")
    doi_url = f"https://doi.org/{doi}" if doi else None
    oa = record.get("open_access") or {}
    oa_links = [link for link in [oa.get("oa_url"), oa.get("pdf_url"), oa.get("landing_page_url")] if link]
    oa_line = " | ".join(dict.fromkeys(oa_links)) if oa_links else "待补"

    lines = [
        f"## {index}. {fmt(record.get('title'))}",
        "",
        "### 1. 基本信息",
        f"- 标题：{fmt(record.get('title'))}",
        f"- 作者：{fmt(record.get('authors'))}",
        f"- 年份：{fmt(record.get('year'))}",
        f"- venue：{fmt(record.get('venue'))}",
        f"- DOI / URL：{fmt(doi_url)}",
        "- 赛道：待补",
        f"- 当前证据等级：{fmt(record.get('evidence_level'))}",
        f"- 用途标签：{fmt(record.get('usage_tag_suggestion'), default='map')}",
        "",
        "### 2. 检索与版本信息",
        f"- 检索命中的关键词 / query：{fmt(record.get('search_query'))}",
        "- 获取路径：metadata（如有 OA 链接仅记录线索，未自动抓正文）",
        f"- 版本：{fmt(record.get('version_hint'))}",
        "- 是否还有未确认版本差异：待核对 conference / journal / preprint 关系",
        "",
        "### 3. 研究问题",
        "- 论文解决什么问题：待根据 abstract / intro 提炼",
        "- 问题边界：待补",
        "- 关键假设：待补",
        "- 关键约束：待补",
        "",
        "### 4. 方法主干",
        "- 核心机制：待根据 abstract / method 提炼",
        "- 创新单元：待补",
        "- 与经典方法相比新增了什么：待补",
        f"- 如果只有 abstract，可确认到哪一层：{inferred_scope(record)}",
        "- 仍然未知的关键细节：模型结构、baseline 配置、训练 / 控制设置、统计方式",
        "",
        "### 5. 实验设置",
        "- 数据 / 仿真 / benchmark / 硬件平台：待补",
        "- 场景 / 工况：待补",
        "- setup / 训练或控制配置：待补",
        "- baseline：待补",
        "- 评价指标：待补",
        "- 可复用到我当前方向的实验要素：待补",
        "",
        "### 6. 结果与作者声称的创新",
        "- 主要结果：待根据 abstract / results 提炼",
        "- 作者声称的创新点：待根据 abstract / intro 提炼",
        "- 证据是否足以支持这些声称：当前仅完成 metadata bootstrap，需继续补证据",
        "",
        "### 7. 真实价值判断",
        "- 我认为真正有效的新意：待补",
        "- 可能被高估的部分：待补",
        "- 对我当前方向最有用的启发：待补",
        "- novelty risk：待补",
        "",
        "### 8. 局限与缺口",
        "- 局限：待补",
        "- 未覆盖场景：待补",
        "- 可迁移性边界：待补",
        "- 风险（novelty / comparability / resource / evidence）：待补",
        "- 若只拿到 abstract，下一步该补什么证据：方法章节、实验表格、baseline、公平性与 setup",
        "",
        "### 9. Shortlist 判断",
        "- relevance：待补",
        "- evidence：待补",
        "- comparability：待补",
        "- practicality：待补",
        "- 是否进入 deep-read set：待补",
        "",
        "### 10. 关联线索",
        f"- 关联关键词：{fmt([concept.get('display_name') for concept in record.get('concepts') or []], default='待补')}",
        "- 关联 benchmark / dataset / simulator / hardware：待补",
        "- 可能继续追的作者 / 课题组 / 近邻论文：待补",
        "",
        "### 11. Metadata lane 可直接复用证据",
        f"- 引文量：{fmt(record.get('cited_count'))}",
        f"- OA 线索：{oa_line}",
        f"- 规范化备注：{fmt(record.get('normalization_note'))}",
        "- 摘要摘录：",
        "",
        "> " + abstract_excerpt(record).replace("\n", "\n> "),
        "",
    ]
    return "\n".join(lines).rstrip()


def build_document(records: List[Dict[str, Any]], title: str) -> str:
    header = "\n".join(
        [
            f"# {title}",
            "",
            "> 说明：这是一份 metadata-first 文献卡片脚手架。它适合做 mapping / shortlist 起步，不等于已经完成全文证据抽取。后续请按 `references/evidence-extraction.md` 回填关键字段。",
            "",
        ]
    ).rstrip()
    cards = [build_card(record, index=index) for index, record in enumerate(records, start=1)]
    if not cards:
        return header + "\n"
    return header + "\n\n---\n\n" + "\n\n---\n\n".join(cards) + "\n"


def main() -> int:
    args = parse_args()
    records = load_records(Path(args.input))
    document = build_document(records, title=args.title)
    if args.output:
        Path(args.output).write_text(document, encoding="utf-8")
    else:
        sys.stdout.write(document)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())