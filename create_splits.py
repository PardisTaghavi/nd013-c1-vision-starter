import argparse
import glob
import os
import random

import numpy as np

import shutil
from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    #files=glob.glob(source)
    #dir=glob.glob(source)
    files=os.listdir(source)
    number=len(files)
    #print(files)
    random.shuffle(files)
    print(files)
    for n in range(number):
        path=os.path.join(source, files[n])
        #print("path is" , path ,"\n")
        if n<=0.8*number:
            shutil.copy(path, os.path.join(destination, "train"))
            #print(os.path.join(destination, "train"),"\n")
        elif ((n<=0.9*number) and (n>0.8*number)):
            shutil.copy(path, os.path.join(destination, "val"))
            #print(os.path.join(destination, "val"),"\n")

        else:
            shutil.copy(path, os.path.join(destination, "test"))
            #print(os.path.join(destination, "test"),"\n")

     
        
    # There are different cross validation methods such as 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)