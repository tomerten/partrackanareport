# -*- coding: utf-8 -*-

"""
Module partrackanareport.nafftools 
=================================================================

A module

"""

# your imports here ...
import multiprocessing
from collections import ChainMap
from typing import Generator

import dask.delayed as delay
import numpy as np
import PyNAFF as pnf
from dask import dataframe as dd
from joblib import Parallel, delayed
from tqdm import tqdm


def divide_list_in_n_equal_chunks(_list: list, n: int) -> Generator:
    """Method to divide a list in n equal chuncks.

    Parameters
    ----------
    _list : list
            list to divide
    n : int
            number of chuncks

    Yields
    -------
    Generator
            chunk generator
    """
    for i in range(0, len(_list), n):
        yield _list[i : i + n]
