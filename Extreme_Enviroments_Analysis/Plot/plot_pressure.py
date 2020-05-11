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


def plot_Pressures(CycleDataSet):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    rightguage_String = "RightGauge(mBar)"
    rightItem = df.columns.get_loc(str(rightguage_String))
    middleguage_String = "MiddleGauge(mBar)"
    middleItem = df.columns.get_loc(str(middleguage_String))
    leftguage_String = "LeftGauge(mBar)"
    leftItem = df.columns.get_loc(str(leftguage_String))
    turbopump_String = "TurboPump(mBar)"
    turboItem = df.columns.get_loc(str(turbopump_String))
    rightcompressor_String = "RightCompressor"
    rightcompressorItem = df.columns.get_loc(str(rightcompressor_String))
    leftcompressor_String = "LeftCompressor"
    leftcompressorItem = df.columns.get_loc(str(leftcompressor_String))

    fig, ((ax1, ax2, ax3, ax4, ax5, ax6)) = plt.subplots(nrows=6, ncols=1,
                                                         sharex=True)  # , ax4, ax5, ax6)) = plt.subplots(nrows=6, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])

    color = 'tab:blue'
    df.iloc[:, rightItem].plot(x=cycleTime, y=df.iloc[:, rightItem], ax=ax1, color=color, linewidth=3.3)
    ax1.set_title('RightGauge (mBar)', fontsize=16)
    # ax1.set_xlabel('Time', fontsize=16)
    # ax1.set_ylabel('RightGauge (mBar) Pressure', color=color, fontsize=18)
    ax1 = plt.gca()

    color = 'tab:green'
    df.iloc[:, middleItem].plot(x=cycleTime, y=df.iloc[:, middleItem], ax=ax2, color=color, linewidth=3.3)
    ax2.set_title('MiddleGauge (mBar)', fontsize=16)
    # ax2.set_xlabel('Time', fontsize=14)
    # ax2.set_ylabel('MiddleGauge (mBar) Pressure', color=color, fontsize=18)
    ax2 = plt.gca()

    color = 'tab:purple'
    df.iloc[:, leftItem].plot(x=cycleTime, y=df.iloc[:, leftItem], ax=ax3, color=color, linewidth=3.3)
    ax3.set_title('LeftGauge (mBar)', fontsize=16)
    # ax3.set_xlabel('Time', fontsize=14)
    # ax3.set_ylabel('LeftGauge (mBar) Pressure', color=color, fontsize=18)
    ax3 = plt.gca()

    color = 'tab:blue'
    df.iloc[:, turboItem].plot(x=cycleTime, y=df.iloc[:, turboItem], ax=ax4, color=color, linewidth=3.3)
    ax4.set_title('TurboPump (mBar)', fontsize=16)
    # ax3.set_xlabel('Time', fontsize=14)
    # ax3.set_ylabel('LeftGauge (mBar) Pressure', color=color, fontsize=18)
    ax4 = plt.gca()

    color = 'tab:green'
    df.iloc[:, rightcompressorItem].plot(x=cycleTime, y=df.iloc[:, rightcompressorItem], ax=ax5, color=color,
                                         linewidth=3.3)
    ax5.set_title('Right Compressor', fontsize=16)
    ax5 = plt.gca()

    color = 'tab:purple'
    df.iloc[:, leftcompressorItem].plot(x=cycleTime, y=df.iloc[:, leftcompressorItem], ax=ax6, color=color,
                                        linewidth=3.3)
    ax6.set_title('Left Compressor', fontsize=16)
    ax6 = plt.gca()

    # color = 'tab:red'
    # ax7 = ax2.twinx()  # instantiate a second axes that shares the same x-axis
    # ax7.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    # ax7.tick_params(axis='y', labelcolor=color)
    # tempString = df.columns.get_loc("C2")
    # df.iloc[:, tempString].plot(x=cycleTime, y=df.iloc[:, middleItem], ylim=(0, 310), ax=ax7, color=color,
    #                             linewidth=3.3)
    # ax7.grid(False)

    # ax.set_title(str(itemString))

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ": Pessures", fontsize='large')
    # fig.suptitle('CVBGA97: Cycle 500', fontsize=21)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

# def plot_Pressure(CycleDataSet, itemString):
#     df = CycleDataSet.cycleDataFrame
#     cycleDict = CycleDataSet.cycleInfo
#     item = df.columns.get_loc(str(itemString))
#
#     fig,(ax) = plt.subplots(nrows=1,ncols=1)
#     cycleTime = list(cycleDict["CorrectedTimes"])
#
#     df.iloc[:,item].plot(x=cycleTime,y=df.iloc[:,item],ylim=(-.25,890),ax=ax)
#     #ax.set_title(str(itemString))
#
#     cycleNumber = cycleDict.get('Cycle')
#     fig.suptitle('Cycle '+str(cycleNumber)+": "+str(itemString),fontsize='large')
############
# def plot_Pressures(CycleDataSet, itemList):
#     df = CycleDataSet.cycleDataFrame
#     cycleDict = CycleDataSet.cycleInfo
#
#     fig,(ax) = plt.subplots(nrows=1,ncols=1,sharex=True)
#     cycleTime = list(cycleDict["CorrectedTimes"])
#
#     for itemString in itemList:
#         itemColumn = df.columns.get_loc(str(itemString))
#         df.iloc[:,itemColumn].plot(x=cycleTime,y=df.iloc[:,itemColumn],ylim=(-.25,890),ax=ax)
#     plt.legend()
#
#     cycleNumber = cycleDict.get('Cycle')
#     fig.suptitle('Cycle '+str(cycleNumber)+' Pressures (mBar)',fontsize='large')
#
# plot_Pressure(Cycle500, "RightGauge(mBar)")
#
# tempList = list()
# tempList.append("RightGauge(mBar)")
# tempList.append("MiddleGauge(mBar)")
# tempList.append("LeftGauge(mBar)")
# tempList.append("TurboPump(mBar)")
# tempList.append("TubePressure(mBar)")
# tempList.append("ChamberPressure(mBar)")
# plot_Pressures(Cycle500, tempList)
# print("Success!!!")
