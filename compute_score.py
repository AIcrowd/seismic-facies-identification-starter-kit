import numpy as np
from sklearn.metrics import multilabel_confusion_matrix

import time
import os

def _prf_divide(numerator, denominator, ):
    """Performs division and handles divide-by-zero.
    On zero-division, sets the corresponding result elements equal to
    0 or 1 (according to ``zero_division``). 
    """
    mask = denominator == 0.0
    denominator = denominator.copy()
    denominator[mask] = 1  # avoid infs/nans
    result = numerator / denominator

    return result

def compute_scores(y_true, y_pred, class_weights=[1, 1, 1, 1, 20, 20]):
    """
    Computes the weighted & unweighted f1_score and accuracy

    Using the standard F1-Score and class-wise accuracy computations were quite 
    slow as we were doing a lot of redundant work across all score computations,
    hence we have implemented this from the base principles.

    Please refer to the inline comments.
    """

    # Initial Housekeeping Taks
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()
    class_weights = np.array(class_weights)

    # Computing Multilabel Confusion Matrix
    print("--------- Computing MCM... ")
    begin_time = time.time()
    MCM = multilabel_confusion_matrix(y_true, y_pred)
    print("MCM computation time  : ", time.time() - begin_time)
    
    """
    Gather True Positives, True Negatives, False Positives, False Negatives
    """
    tp_sum = MCM[:, 1, 1]
    tn_sum = MCM[:, 0, 0]
    fn_sum = MCM[:, 1, 0]
    fp_sum = MCM[:, 0, 1]
    
    print("--------- Computing per class instances... ")
    per_class_instances = np.bincount(y_true) # Helps keep a track of total number of instances per class
    per_class_instances = per_class_instances[1:] # as the class names in the dataset are NOT zero-indexed

    assert class_weights.shape == per_class_instances.shape
    
    print("--------- Computing precision... ")
    # precision : tp / (tp + fp)
    precision = _prf_divide(
                    tp_sum,
                    (tp_sum + fp_sum)
                )
    print("--------- Computing recall... ")                        
    # recall : tp / (tp + fn)
    recall = _prf_divide(
                    tp_sum,
                    (tp_sum + fn_sum)
                )

    print("--------- Computing F1 score... ")
    # f1 : 2 * (recall * precision) / (recall + precision)
    f1_score = _prf_divide(
                    2 * precision * recall,
                    precision + recall
                )
    print("--------- Computing Accuracy... ")
    # accuracy = tp_sum / instances_per_class
    # NOTE: we are computing the accuracy independently for all the class specific subgroups
    accuracy = _prf_divide(
                    tp_sum,
                    per_class_instances
                )

    f1_score_weighted = np.dot(class_weights, f1_score) / np.sum(class_weights)
    f1_score_unweighted = f1_score.mean()

    accuracy_weighted = np.dot(class_weights, accuracy) / np.sum(class_weights)
    accuracy_unweighted = accuracy.mean()

    return f1_score_weighted, accuracy_weighted, f1_score_unweighted, accuracy_unweighted


if __name__ == "__main__":

    TRAIN_DATASET_PATH = os.getenv("TRAIN_DATASET_PATH", "data/data_train.npz") 
    TRAIN_LABELS_PATH = os.getenv("TRAIN_LABELS_PATH", "data/labels_train.npz") 


    # Load train dataset
    train_dataset = np.load(TRAIN_DATASET_PATH, allow_pickle=True, mmap_mode='r')
    train_dataset = train_dataset["data"]

    # Load train labels
    train_labels = np.load(TRAIN_LABELS_PATH, allow_pickle=True, mmap_mode='r')
    train_labels = train_labels["labels"]


    # Create a small slice of train dataset
    val_dataset = train_dataset[:500, :300, :250]
    val_labels = train_labels[:500, :300, :250]

    # Generate a set of random predictions
    prediction = np.random.randint(
        low = 1,
        high = 6,
        size = val_labels.shape
    )

    # Compute Scores

    class_weights = [1, 1, 1, 1, 20, 20]
    f1_score_weighted, accuracy_weighted, f1_score_unweighted, accuracy_unweighted \
        = compute_scores(val_labels, prediction, class_weights=class_weights)


    print("""

    F1-Score (Weighted) : {}
    F1-Score (Unweighted) : {}
    Accuracy (Weighted) : {}
    Accuracy (Unweighted) : {}
    """.format(f1_score_weighted, f1_score_unweighted, accuracy_weighted, accuracy_unweighted))