#!/usr/bin/env python3

from collections import defaultdict
import csv
import json
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import statistics

class Session:
    def __init__(self):
        self.time_epochs = []
        self.device_id = None
        self.query_length = []
        self.selected_index = -2

    def query_drops(self):
        ans = 0
        for i in range(1, len(self.query_length) - 1):
            if (self.query_length[i - 1] <= self.query_length[i]) != (self.query_length[i] <= self.query_length[i + 1]):
                ans += 1
        return ans // 2 + ans % 2

sessions = [defaultdict(Session) for _ in [0, 1]]

with open("2024InternshipData.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        json_data = json.loads(row["event_data"])

        # Events are given in ascending order of the timestamp
        sessions[json_data["experimentGroup"]][json_data["session_id"]].time_epochs.append(float(row["time_epoch"]))
        # every session id has only one device associated to it
        sessions[json_data["experimentGroup"]][json_data["session_id"]].device_id = row["device_id"]
        # event id's are specified in ascending order (0, 1, ...) for every event
        sessions[json_data["experimentGroup"]][json_data["session_id"]].query_length.append(json_data["searchStateFeatures"]["queryLength"])
        # the event_id is searchRestarted for the first entries, and only the last is sessionFinished

        # 'selectedIndex' is either 'null' (no element selected, i'll represent this as -1) or an one element array with the selected item
        # the second case can only happen if the event_id is 'searchFinished'
        # some entries don't have a searchFinished (i'll represent this as -2)
        if row["event_id"] == "sessionFinished":
            sessions[json_data["experimentGroup"]][json_data["session_id"]].selected_index = (json_data["selectedIndexes"] or [-1])[0]

max_index = max([x.selected_index for group in [0, 1] for x in sessions[group].values()])

def selected_to_color(selected_id):
    if selected_id < 0:
        return (1, 0, 0)
    return cm.get_cmap("viridis")(selected_id ** 0.5 / max_index ** 0.5)

for group in [0, 1]:
    print(f"=== Group {group} ===")

    plt.figure()
    plt.title(f"Selected indexes, group={group}")
    plt.ylim(0, 0.5)
    selected_indexes_data = [x.selected_index for x in sessions[group].values()]
    plt.hist(selected_indexes_data, bins=range(-1, max_index + 1), weights=np.ones(len(selected_indexes_data)) / len(selected_indexes_data))

    print(f"Selected indexes (values >= 0), group={group}: mean={statistics.mean([x for x in selected_indexes_data if x >= 0])}, median={statistics.median([x for x in selected_indexes_data if x >= 0])}")

    plt.figure()
    plt.title(f"Characters typed, group={group}")
    plt.yscale("log")
    plt.ylim(top=1000)
    characters_typed_data = [(x.query_length, x.selected_index, [y - x.time_epochs[0] for y in x.time_epochs]) for x in sessions[group].values()]
    for (chars_typed, selected_index, timestamps) in characters_typed_data:
        plt.plot(timestamps, chars_typed, color=selected_to_color(selected_index))

    time_solution_data = [x.time_epochs[-1] - x.time_epochs[0] for x in sessions[group].values()]
    print(f"Time to solution (value > 0), group={group}: mean={statistics.mean([x for x in time_solution_data if x > 0])}, median={statistics.median([x for x in time_solution_data if x > 0])}")

    query_drops_data = [x.query_drops() for x in sessions[group].values()]
    print(f"Query erases (value >= 0), group={group}: mean={statistics.mean(query_drops_data)}, median={statistics.median(query_drops_data)}")

plt.show()
