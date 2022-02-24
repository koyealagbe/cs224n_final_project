"""
data_splitter.py
Splits movie data into training, dev, and test sets
"""

import random

random.seed(224)

data_file = "dataset.txt"
bos_token = "<BOS>"
eos_token = "<EOS>"
dataset_files = {"train": "train-set.txt", "dev": "dev-set.txt", "test": "test-set.txt"}
dataset_proportions = {"train": 0.8, "dev": 0.1, "test": 0.1}
dataset_sizes = {"train": 0, "dev": 0, "test": 0}
dataset = open(data_file, "r")
screenplays = []

# Populate list of screenplays
for line in dataset:
  if bos_token in line:
    screenplays.append(line)
    #print("Adding screenplay number", len(screenplays))
  else:
    screenplays[-1] += line
dataset.close()

num_screenplays = len(screenplays)

dataset_sizes["train"] = (int) (dataset_proportions["train"] * num_screenplays)
dataset_sizes["dev"] = (int) (dataset_proportions["dev"] * num_screenplays)
dataset_sizes["test"] = num_screenplays - (dataset_sizes["train"] + dataset_sizes["dev"])

random.shuffle(screenplays)
idx = 0
for key, filename in dataset_files.items():
  file = open(filename, "w+")
  for i in range(idx, idx + dataset_sizes[key]):
    file.write(screenplays[i])
  idx += dataset_sizes[key]
  file.close()

