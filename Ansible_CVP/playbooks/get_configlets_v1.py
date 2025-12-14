#!/usr/bin/env python3
from pathlib import Path
import json

CVP_CONFIGLET = {}

for f in Path("../configlets/configs").rglob("*.cfg"):
    CVP_CONFIGLET[f.stem] = f.read_text()

print(json.dumps(CVP_CONFIGLET))
