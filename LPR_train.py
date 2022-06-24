#import torch
import argparse
from pathlib import Path
import sys
import os


def get_root_path():
    """Get relative root dir"""
    curr_file = Path(__file__).resolve()
    root_dir = curr_file.parents[0]
    if str(root_dir) not in sys.path:
        sys.path.append(str(root_dir))
    root_dir = Path(os.path.relpath(root_dir, Path.cwd()))
    return root_dir


def sparsed_tuple_for_ctc(predicted_length: int, gt_lengths: list[int]):
    """Construct matched tuples for ctc loss calculation
 
    Args:
        predicted_length (int): LPRNet output shape (The initially defined length of the predicted sequence)
        target_length (list[int]): list of ground truth labels length for current batch in LPRNet dataloader

    Returns:
        input_lengths (tuple): tuple, each element of which corresponds to the length of LPRNet output
        target_lengths (tuple): tuple, each element of which corresponds ground truth label length 
    """
    input_lengths = []
    target_lengths = []

    for gt_len in gt_lengths:
        input_lengths.append(predicted_length)
        target_lengths.append(gt_len)

    return tuple(input_lengths), tuple(target_lengths)


def create_parser():
    parser = argparse.ArgumentParser(descriprion='Parameters to train LPRNet with ST module')


print(get_root_path())