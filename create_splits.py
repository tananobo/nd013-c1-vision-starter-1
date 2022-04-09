import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    dataset = os.listdir(data_dir + 'training_and_validation')
    print("dataset_length is", len(dataset))
    random.shuffle(dataset)
    traindata = dataset[:int(len(dataset)*0.8)]
    valdata = dataset[int(len(dataset)*0.8):]
    
    for name in traindata:
        dirname = os.path.join(data_dir,'training_and_validation',name)
        distdirname = os.path.join(data_dir, 'train')
        shutil.move(dirname, distdirname)
    
    for name in valdata:
        dirname = os.path.join(data_dir,'training_and_validation',name)
        distdirname = os.path.join(data_dir, 'val')
        shutil.move(dirname, distdirname)
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)