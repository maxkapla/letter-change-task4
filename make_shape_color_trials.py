import csv
import os
import random
import math

random.seed(1)

N_TRIALS = 84
SET_SIZE = 4

PALETTE = [
    [0.122, 0.467, 0.706],
    [1.000, 0.498, 0.055],
    [0.173, 0.627, 0.173],
    [0.839, 0.153, 0.157],
    [0.580, 0.404, 0.741],
    [0.549, 0.337, 0.294],
    [0.890, 0.467, 0.761],
    [0.800, 0.800, 0.800],
    [0.737, 0.741, 0.133],
    [0.090, 0.745, 0.812],
]

SHAPES = [3, 4, 5, 6, 8, 64]

OUT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shape_color_change_trials.csv")

if N_TRIALS % 2 != 0:
    raise ValueError("N_TRIALS must be even.")

def safe_text(x):
    s = str(x)
    return s[1:] if s.startswith("=") else s

def rgb_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def sample_colors():
    while True:
        pick = random.sample(PALETTE, SET_SIZE)
        good = True
        for i in range(SET_SIZE):
            for j in range(i + 1, SET_SIZE):
                if rgb_dist(pick[i], pick[j]) < 0.35:
                    good = False
        if good:
            return pick

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
    change = plan["change"]
    pos = plan["pos"]

    shapes = random.sample(SHAPES, SET_SIZE)
    mem_cols = sample_colors()
    probe_cols = mem_cols.copy()

    if change == 1:
        old = probe_cols[pos]
        used = [tuple(c) for i, c in enumerate(probe_cols) if i != pos]
        options = [c for c in PALETTE if c != old and tuple(c) not in used]
        probe_cols[pos] = random.choice(options)
        correct = "d"
    else:
        correct = "s"

    row = {
        "trial": trial_num,
        "change": change,
        "pos": pos,
        "correct": correct,
    }

    for i in range(SET_SIZE):
        row[f"v{i+1}"] = shapes[i]
        row[f"col{i+1}"] = safe_text(mem_cols[i])
        row[f"tcol{i+1}"] = safe_text(probe_cols[i])

    rows.append(row)

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    fieldnames = (
        ["trial", "change", "pos", "correct"]
        + [f"v{i+1}" for i in range(SET_SIZE)]
        + [f"col{i+1}" for i in range(SET_SIZE)]
        + [f"tcol{i+1}" for i in range(SET_SIZE)]
    )
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {N_TRIALS} trials to {OUT_CSV}")