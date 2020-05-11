import sys

import numpy as np
import pandas as pd

import File.file

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import Data_Structures.DataSet_Abstract as ADS
import Data_Structures.DataSet_Cycle as CCDS
import Data_Structures.DataSet_Uniform as CUDS
import File.Groups


def plot_Temperatures(CycleDataSet, itemList):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    fig, (ax) = plt.subplots(nrows=1, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])

    title = " "
    for itemString in itemList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(0, 300), ax=ax)
        title = title + str(itemString) + ", "
    else:
        title = title[:-2]
    # ax.set_title(str(title))
    plt.legend()

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ': Temperatures', fontsize='large')
