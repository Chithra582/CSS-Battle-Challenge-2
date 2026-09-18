#!/usr/bin/env python3
"""css-battle-challenge-agent -- OpenGAP v0.1.0 CLI"""
import argparse, os, json, yaml

ROOT = os.path.dirname(os.path.abspath(__file__))
REQUIRED_FILES = ["agent.yaml","SOUL.md","RULES.md","DUTIES.md","EXPLAINABILITY.md","AGENTS.md"]

def validate():
    print("=== css-battle-challenge-agent Validation ===\n")
    all_pass = True
    for f in REQUIRED_FILES:
        exists = os.path.isfile(os.path.join(ROOT, f))
        status = "PASS" if exists else "FAIL"
        if not exists: all_pass = False
        print(f"  [{status}] {f}")
    tools_dir = os.path.join(ROOT, "tools")
    yamls = [x for x in os.listdir(tools_dir) if x.endswith(".yaml")] if os.path.isdir(tools_dir) else []
    status = "PASS" if yamls else "FAIL"
    if not yamls: all_pass = False
    print(f"  [{status}] tools/ ({len(yamls)} yaml files)")
    skills_dir = os.path.join(ROOT, "skills")
    subdirs = [x for x in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir,x))] if os.path.isdir(skills_dir) else []
    status = "PASS" if subdirs else "FAIL"
    if not subdirs: all_pass = False
    print(f"  [{status}] skills/ ({len(subdirs)} skills)")
    adapters_dir = os.path.join(ROOT, "adapters")
    adapt_files = os.listdir(adapters_dir) if os.path.isdir(adapters_dir) else []
    status = "PASS" if len(adapt_files) >= 4 else "FAIL"
    if len(adapt_files) < 4: all_pass = False
    print(f"  [{status}] adapters/ ({len(adapt_files)} files)")
    print()
    print("Result:", "ALL PASS [OK]" if all_pass else "SOME CHECKS FAILED [FAIL]")

def export_all():
    with open(os.path.join(ROOT,"agent.yaml")) as f:
        spec = yaml.safe_load(f)
    print(json.dumps(spec, indent=2))

def challenge_info():
    print("=== CSS Battle Challenge 2 -- Flip The Coin ===")
    print("Type      : CSS/JS Interactive Animation Challenge")
    print("Tech      : HTML5, CSS3 (3D Transforms), Vanilla JavaScript")
    print("Feature   : 3D coin flip with perspective + rotateY + backface-visibility")
    print("Stats     : Heads count, Tails count, Total flips tracked")
    print("Author    : Chithra R (https://github.com/Chithra582)")

parser = argparse.ArgumentParser(description="css-battle-challenge-agent CLI")
parser.add_argument("--validate", action="store_true")
parser.add_argument("--export", action="store_true")
parser.add_argument("--challenge", action="store_true")
args = parser.parse_args()
if args.validate: validate()
elif args.export: export_all()
elif args.challenge: challenge_info()
else: parser.print_help()
