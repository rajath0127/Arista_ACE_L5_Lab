from pathlib import Path

def load_configlets(base_dir, pattern="*.cfg"):
    result = {}
    for f in Path(base_dir).rglob(pattern):
        result[f.stem] = f.read_text()
    return result

class FilterModule(object):
    def filters(self):
        return {
            "get_configlets_v3": load_configlets
        }
