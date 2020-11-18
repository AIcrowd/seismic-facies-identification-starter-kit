#!/usr/bin/env python

import os
import numpy as np


TRAIN_DATASET_PATH = os.getenv("TRAIN_DATASET_PATH", "data/data_train.npz") 
TRAIN_LABELS_PATH = os.getenv("TRAIN_LABELS_PATH", "data/labels_train.npz") 
TEST_DATASET_PATH = os.getenv("TEST_DATASET_PATH", "data/data_test_2.npz")

OUTPUT_FILE_PATH = os.getenv("OUTPUT_FILE_PATH", "prediction.npz")

"""
For random prediction generation, we will simply
load the test_dataset and generate a random numpy array of the same shape
and fill it with integer values in the range [1, 6]
"""

# Load train dataset
train_dataset = np.load(TRAIN_DATASET_PATH, allow_pickle=True, mmap_mode='r')
train_dataset = train_dataset["data"]

# Load train labels
train_labels = np.load(TRAIN_LABELS_PATH, allow_pickle=True, mmap_mode='r')
train_labels = train_labels["labels"]

# Load test dataset
test_dataset = np.load(TEST_DATASET_PATH, allow_pickle=True, mmap_mode = 'r')
test_dataset = test_dataset["data"] # This allows us to access the actual np array from the loaded npz file object

# Generate random prediction
prediction = np.random.randint(
    low = 1,
    high = 6,
    size = test_dataset.shape
)

assert prediction.shape == test_dataset.shape, "The shape of the prediction file does not match that of the test dataset."

#### Write predictions files
#
# Note : we use numpy.savez_compressed to ensure the file sizes are not over bloated
np.savez_compressed(
    OUTPUT_FILE_PATH,
    prediction=prediction
)