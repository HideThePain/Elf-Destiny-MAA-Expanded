#!/usr/bin/env python3
import re
import os
from pathlib import Path

root = Path(__file__).resolve().parent.parent

def find_keys_in_decisions():
    keys = set()
    decision_dir = root / 'common' / 'decisions'
    if not decision_dir.exists():
        return keys
    pattern = re.compile(r"\b(?:desc|selection_tooltip|custom_tooltip|title|confirm|tooltip|type)\s*=\s*([A-Za-z0-9_\.\$\-']+)")
    for path in decision_dir.glob('**/*.txt'):
        for line in path.read_text(encoding='utf-8').splitlines():
            m = pattern.search(line)
            if m:
                raw = m.group(1)
                # strip quotes if present
                key = raw.strip('"').strip("'")
                keys.add(key)
    return keys


def find_localization_keys():
    loc_keys = set()
    loc_dir = root / 'localization'
    if not loc_dir.exists():
        return loc_keys
    # simple parse: lines starting with KEY followed by ':'
    for path in loc_dir.glob('**/*.yml'):
        for line in path.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = re.match(r"^([A-Za-z0-9_\.\-]+)\s*:\s*", line)
            if m:
                loc_keys.add(m.group(1))
    return loc_keys


def main():
    dec_keys = find_keys_in_decisions()
    loc_keys = find_localization_keys()

    missing = sorted(k for k in dec_keys if k not in loc_keys)

    print(f"Found {len(dec_keys)} localization keys referenced in decisions")
    print(f"Found {len(loc_keys)} localization keys in localization files")
    if missing:
        print('\nMissing localization keys referenced by decisions:')
        for k in missing:
            print(f" - {k}")
        raise SystemExit(2)
    else:
        print('\nAll decision localization keys are present.')

if __name__ == '__main__':
    main()
