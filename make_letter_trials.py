import csv
import os
import random

random.seed(1)

N_TRIALS = 84
OUT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "letter_change_trials.csv")

LETTERS = list("BCDFGHJKLM")

if N_TRIALS % 2 != 0:
    raise ValueError("N_TRIALS must be even.")

def rand_four_letter_string_unique():
    return "".join(random.sample(LETTERS, 4))

def safe_text(x):
    s = str(x)
    return s[1:] if s.startswith("=") else s

change_list = [1] * (N_TRIALS // 2) + [0] * (N_TRIALS // 2)

positions = [0] * 11 + [1] * 11 + [2] * 10 + [3] * 10
random.shuffle(positions)

trial_plan = []
pos_index = 0

for change in change_list:
    if change == 1:
        pos = positions[pos_index]
        pos_index += 1
    else:
        pos = -1
    trial_plan.append({"change": change, "pos": pos})

random.shuffle(trial_plan)

rows = []

for trial_num, plan in enumerate(trial_plan, start=1):
    mem_str = rand_four_letter_string_unique()
    probe_letters = list(mem_str)

    change = plan["change"]
    pos = plan["pos"]

    if change == 1:
        used_letters = set(mem_str)
        options = [l for l in LETTERS if l not in used_letters]
        probe_letters[pos] = random.choice(options)
        correct = "d"
    else:
        correct = "s"

    probe_str = "".join(probe_letters)

    rows.append({
        "trial": trial_num,
        "mem_text": safe_text(mem_str),
        "probe_text": safe_text(probe_str),
        "d1": mem_str[0],
        "d2": mem_str[1],
        "d3": mem_str[2],
        "d4": mem_str[3],
        "p1": probe_str[0],
        "p2": probe_str[1],
        "p3": probe_str[2],
        "p4": probe_str[3],
        "correct": correct,
        "change": change,
        "pos": pos
    })

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "trial",
            "mem_text", "probe_text",
            "d1", "d2", "d3", "d4",
            "p1", "p2", "p3", "p4",
            "correct", "change", "pos"
        ]
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {N_TRIALS} trials to {OUT_CSV}")