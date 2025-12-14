#!/usr/bin/env python3
from pathlib import Path
import json
import sys

repo_root = Path(sys.argv[1]).resolve()

CONFIG_DIR = repo_root / "configlets" / "configs"

CVP_CONFIGLET = {}

for f in CONFIG_DIR.rglob("*.cfg"):
    CVP_CONFIGLET[f.stem] = f.read_text()

print(json.dumps(CVP_CONFIGLET))
