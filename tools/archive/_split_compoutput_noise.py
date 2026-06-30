"""Throwaway: split computation_output structural NOISE between verdict files and other output logs."""
import json

audit = json.load(open("tools/_anchor_validation_results.json"))
idx = json.load(open("tools/knowledge-index.json", encoding="utf-8"))
eq_index = {e["id"]: e for e in idx["equations"]}

verdict_file = {"NOISE": [], "VALID": []}
other_txt = {"NOISE": [], "VALID": []}
json_out = {"NOISE": [], "VALID": []}

for aid, av in audit["equations"].items():
    e = eq_index[aid]
    if e["type"] != "structural":
        continue
    sf = e["source_file"].lower().replace("\\", "/")
    if not sf.startswith("computations/"):
        continue
    if not (sf.endswith(".txt") or sf.endswith(".json")):
        continue
    if "_gate_verdicts.txt" in sf:
        bucket = verdict_file
    elif sf.endswith(".json"):
        bucket = json_out
    else:
        bucket = other_txt
    v = av["verdict"]
    if v in bucket:
        bucket[v].append((aid, e["raw"][:90], sf))

for label, b in [("verdict_file (*_gate_verdicts.txt)", verdict_file),
                 ("other_txt (other *.txt logs)", other_txt),
                 ("json_out (*.json)", json_out)]:
    n, v = len(b["NOISE"]), len(b["VALID"])
    total = n + v
    rate = 100.0 * n / total if total else 0
    print(f"{label}: NOISE={n}, VALID={v}, total={total}, NOISE%={rate:.1f}")

print()
print("=== verdict_file NOISE samples ===")
for aid, raw, sf in verdict_file["NOISE"][:5]:
    print(f"  [{aid}] {sf}: {raw!r}")
print()
print("=== other_txt NOISE samples ===")
for aid, raw, sf in other_txt["NOISE"][:5]:
    print(f"  [{aid}] {sf}: {raw!r}")
print()
print("=== json_out NOISE samples ===")
for aid, raw, sf in json_out["NOISE"][:5]:
    print(f"  [{aid}] {sf}: {raw!r}")
