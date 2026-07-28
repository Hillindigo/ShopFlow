# -*- coding: utf-8 -*-
"""PromptLoader

读取并缓存 ShopFlow 的统一系统提示词文件 app/application/prompts/globex.yml，
全项目提示词只从这里取；文件名保持不变以兼容现有加载路径。
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml

PROMPTS_PATH = Path(__file__).resolve().parent / "globex.yml"


@lru_cache(maxsize=1)
def load_prompts() -> dict:
    with open(PROMPTS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)
