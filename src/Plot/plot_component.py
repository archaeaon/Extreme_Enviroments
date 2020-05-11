#########################################################################################
#                                      Imports                                          #
#########################################################################################
import sys
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})
plt.style.use('seaborn-whitegrid')

import Data_Structures.DataSet_Abstract as ADS
import Data_Structures.DataSet_Cycle as CCDS
import Data_Structures.DataSet_Uniform as CUDS
import File.Groups
import File.file

import datetime as dt

strptime = dt.datetime.strptime
import math


#########################################################################################
#                                  Plotting Functions                                   #
#########################################################################################
# TODO::Are there capacitors of multiple types in the Capacitor files?

def plot_BP_Resistors(abstract_DataSet):
    print("top of BP resistor plot function in plot_components")

    if isinstance(abstract_DataSet, CCDS.DataSet_Cycle):
        print("a cycle was passed in")
        df = abstract_DataSet.DataFrame  # ADS.DataSet_Abstract.DataFrame
        cycleDict = abstract_DataSet.DataSetDict  # ADS.DataSet_Abstract.DataSetDict

        fig, ((ax1), (ax2)) = plt.subplots(nrows=2, ncols=1, sharex=True)
        cycleTime = list(cycleDict["CorrectedTimes"])

        tempList = list(cycleDict["resistBP1List"])
        for item in tempList:
            df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 200), ax=ax1)
        ax1.set_title("BackPlane 1 Resistors")

        tempList = list(cycleDict["resistBP2List"])
        for item in tempList:
            df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 200), ax=ax2)
        ax2.set_title("Backplane 2 Resistors")

        cycleNumber = cycleDict.get('Cycle')
        fig.suptitle('Cycle ' + str(cycleNumber) + ' Resistors', fontsize='large')

    if isinstance(ADS.DataSet_Abstract, CUDS.DataSet_Uniform):
        print("a non-cycle constant was passed in")


def plot_MUX_Resistors(CycleDataSet):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    fig, ((ax1)) = plt.subplots(nrows=1, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])
    cycleNumber = cycleDict.get('Cycle')

    color = 'tab:blue'
    tempList = list(cycleDict["resistMUXList"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(9, 123), ax=ax1)
    ax1.set_ylabel('Resistance', color=color, fontsize=20)
    ax1.set_title('Cycle ' + str(cycleNumber) + ' MUX Resistors')
    ax1.set_xlabel('Time', fontsize=18)

    color = 'tab:red'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    tempString = df.columns.get_loc("C3")
    df.iloc[:, tempString].plot(x=cycleTime, y=df.iloc[:, item], ylim=(9, 310), ax=ax2, color=color, linewidth=3.3)
    ax2.grid(False)


def plot_ALL_Resistors(CycleDataSet):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    fig, ((ax1), (ax2), (ax3)) = plt.subplots(nrows=3, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])

    tempList = list(cycleDict["resistBP1List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-1.75, 40), ax=ax1)
    ax1.set_title("BackPlane 1 Resistors")

    tempList = list(cycleDict["resistBP2List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-1.75, 10), ax=ax2)
    ax2.set_title("Backplane 2 Resistors")

    tempList = list(cycleDict["resistMUXList"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(15, 65), ax=ax3)
    ax3.set_title("MUX Resistors")

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ' Resistors', fontsize='large')


def plot_Capacitors(CycleDataSet):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    fig, ((ax1), (ax2)) = plt.subplots(nrows=2, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])

    tempList = list(cycleDict["capBP1List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 7200), ax=ax1)
    ax1.set_title("BackPlane 1 Capacitors")

    tempList = list(cycleDict["capBP2List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(1.75, 7100), ax=ax2)
    ax2.set_title("Backplane 2 Capacitors")

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ' Capacitors', fontsize='large')


def plot_SMT_Capacitors(CycleDataSet):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    fig, ((ax1), (ax2)) = plt.subplots(nrows=2, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])

    tempList = list(cycleDict["capBP1List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 65), ax=ax1)
    ax1.set_title("BackPlane 1 Capacitors")

    tempList = list(cycleDict["capBP2List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 65), ax=ax2)
    ax2.set_title("Backplane 2 Capacitors")

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ' Capacitors', fontsize='large')


def plot_Cycle(CycleDataSet):
    df = CycleDataSet.DataFrame
    Info500 = CycleDataSet.DataSetDict
    fig, ((ax1, ax2, ax3, ax4, ax5)) = plt.subplots(nrows=5, ncols=1, sharex=True)  # ,sharey=True,figsize=(10,5))
    cycleTime = list(Info500["CorrectedTimes"])

    tempList = list(Info500["resistBP1List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 90), ax=ax1)
    ax1 = plt.gca()
    # ax1.set_title("Resistors: BackPlane 1")

    tempList = list(Info500["resistBP2List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 1.6), ax=ax2)
    ax2 = plt.gca()
    # ax2.set_title("Resistors: BackPlane 2")

    tempList = list(Info500["capBP1List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ax=ax3)
    ax3 = plt.gca()
    # ax3.set_title("Capacitors: BackPlane 1")

    tempList = list(Info500["capBP2List"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ax=ax4)
    ax4 = plt.gca()
    # ax4.set_title("Capacitors: BackPlane 2")

    tempList = list(Info500["resistMUXList"])
    for item in tempList:
        df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ax=ax5)
    ax5 = plt.gca()
    # ax5.set_title("Resistors: MUX")


def plot_Component(CycleDataSet, itemString):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict
    item = df.columns.get_loc(str(itemString))

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    cycleTime = list(cycleDict["CorrectedTimes"])

    color = 'tab:blue'
    df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-.5, 30), ax=ax1, color=color, linewidth=2.5)
    ax1.set_xlabel('Time', fontsize=18)
    ax1.set_ylabel('Resistance', color=color, fontsize=20)

    color = 'tab:red'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    tempString = df.columns.get_loc("C3")
    df.iloc[:, tempString].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 310), ax=ax2, color=color, linewidth=3.3)
    ax2.grid(False)

    # ax.set_title(str(itemString))

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ": " + str(itemString), fontsize='large')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


def plot_Components(CycleDataSet, itemList):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict

    fig, (ax) = plt.subplots(nrows=1, ncols=1, sharex=True)
    cycleTime = list(cycleDict["CorrectedTimes"])

    title = " "
    for itemString in itemList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(-1, 30), ax=ax)
        title = title + str(itemString) + ", "
    else:
        title = title[:-2]
    # ax.set_title(str(title))
    plt.legend()

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ': Selected Components', fontsize='large')


def plot_Group(CycleDataSet, Component_Group):
    df = CycleDataSet.DataFrame
    Info500 = CycleDataSet.DataSetDict
    fig, ((ax1, ax2)) = plt.subplots(nrows=2, ncols=1, sharex=True)  # ,sharey=True,figsize=(10,5))
    cycleTime = list(Info500["CorrectedTimes"])

    itemList = list(Component_Group)
    resistorList = [element for element in itemList if "R" in element]
    capacitorList = [element for element in itemList if "C" in element]

    for itemString in resistorList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(-.1, 15), ax=ax1)
    ax1.set_title("Resistors: Group")
    ax1 = plt.gca()
    for itemString in capacitorList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(50, 60), ax=ax2)
    ax2.set_title("Capacitors: Group")
    ax2 = plt.gca()

    cycleNumber = Info500.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ': Selected Components', fontsize='large')


def plot_resistor_Group(CycleDataSet, Component_Group):
    df = CycleDataSet.DataFrame
    Info500 = CycleDataSet.DataSetDict
    fig, ((ax1)) = plt.subplots(nrows=1, ncols=1, sharex=True)  # ,sharey=True,figsize=(10,5))
    cycleTime = list(Info500["CorrectedTimes"])

    itemList = list(Component_Group)
    resistorList = [element for element in itemList if "R" in element]

    for itemString in resistorList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(-2, 6), ax=ax1)  # -.1,2
    ax1.set_xlabel('Time', fontsize=18)
    ax1.set_ylabel('Resistance: Group', fontsize=20)

    color = 'tab:red'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    tempString = df.columns.get_loc("C3")
    item = df.columns.get_loc(str(itemString))
    df.iloc[:, tempString].plot(x=cycleTime, y=df.iloc[:, item], ylim=(0, 310), ax=ax2, color=color, linewidth=3.3)
    ax2.grid(False)

    cycleNumber = Info500.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ': Selected Components', fontsize='large')


def plot_capacitor_Group(CycleDataSet, Component_Group):
    df = CycleDataSet.DataFrame
    Info500 = CycleDataSet.DataSetDict
    fig, ((ax)) = plt.subplots(nrows=1, ncols=1, sharex=True)  # ,sharey=True,figsize=(10,5))
    cycleTime = list(Info500["CorrectedTimes"])

    itemList = list(Component_Group)
    capacitorList = [element for element in itemList if "C" in element]

    for itemString in capacitorList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(0, 10000), ax=ax)  # -.1,2
    ax.set_title("Capacitors: Group")
    ax = plt.gca()

    cycleNumber = Info500.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ': Selected Components', fontsize='large')


def plot_mux_Group(CycleDataSet, Component_Group):
    df = CycleDataSet.DataFrame
    Info500 = CycleDataSet.DataSetDict
    fig, ((ax)) = plt.subplots(nrows=1, ncols=1, sharex=True)  # ,sharey=True,figsize=(10,5))
    cycleTime = list(Info500["CorrectedTimes"])

    itemList = list(Component_Group)
    muxList = [element for element in itemList if "MUX" in element]

    for itemString in muxList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(0, 55), ax=ax)  # -.1,2
    ax.set_title("MUX: Group")
    ax = plt.gca()

    cycleNumber = Info500.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ': Selected Components', fontsize='large')


######################################################################################

def plot_Difference(Minuend, Subtrahend, itemString):
    df_minuend = Minuend.DataFrame
    cycleDict_minuend = Minuend.DataSetDict
    item_minuend = df_minuend.columns.get_loc(str(itemString))

    df_subtrahend = Subtrahend.DataFrame
    cycleDict_subtrahend = Subtrahend.DataSetDict
    item = df_subtrahend.columns.get_loc(str(itemString))

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    cycleTime = list(cycleDict_minuend["CorrectedTimes"])

    df_minuend['difference'] = 0
    print(df_minuend)
    print("after subtracting")
    df_minuend['difference'] = df_minuend[str(itemString)] - df_subtrahend[str(itemString)]
    print(df_minuend)
    diff_string = "difference"
    difference = df_minuend.columns.get_loc(str(diff_string))

    color = 'tab:blue'
    # df_minuend.iloc[:,item].plot(x=cycleTime,y=df_minuend.iloc[:,item],ylim=(1.65,15),ax=ax1,color=color, linewidth=3.3)
    df_minuend.iloc[:, difference].plot(x=cycleTime, y=df_minuend.iloc[:, difference], ylim=(0, 25), ax=ax1,
                                        color=color,
                                        linewidth=3.3)
    ax1.set_xlabel('Time', fontsize=18)
    ax1.set_ylabel('Resistance', color=color, fontsize=20)

    color = 'tab:red'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    tempString = df_subtrahend.columns.get_loc("C3")
    df_subtrahend.iloc[:, tempString].plot(x=cycleTime, y=df_subtrahend.iloc[:, item], ylim=(0, 310), ax=ax2,
                                           color=color, linewidth=3.3)
    ax2.grid(False)

    cycleNumberMinuend = cycleDict_minuend.get('Cycle')
    cycleNumberSubtrahend = cycleDict_subtrahend.get('Cycle')
    fig.suptitle(itemString + ': Cycle ' + str(cycleNumberSubtrahend) + ' versus ' + str(cycleNumberMinuend),
                 fontsize=21)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


import numpy as np


def plot_Component_temp_function(CycleDataSet, itemString):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict
    item = df.columns.get_loc(str(itemString))

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    cycleTime = list(cycleDict["CorrectedTimes"])
    print(cycleTime)

    color = 'tab:blue'
    df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-1, 10), ax=ax1, color=color, linewidth=3.3)
    ax1.set_ylabel('Resistance', color=color, fontsize=12)

    temp = df.columns.get_loc("A")
    tick_separation = list(range(0, len(df.index), 50))
    xticker = list(df.iloc[:, temp])

    xticker_1 = list()
    for i in tick_separation:
        xticker_1.append(xticker[i])

    xticker_1 = [round(element) for element in xticker_1]
    plt.xticks(tick_separation, xticker_1)
    plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=14)

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ": " + "R149:Drill_Pad", fontsize='large')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


def test_transform(CycleDataSet, itemString):
    df = CycleDataSet.DataFrame
    temperature_values = df['A'].round(decimals=0)
    print(temperature_values)

    Data_Frame = pd.DataFrame(index=np.arange(500), columns=np.arange(3))
    # , columns=np.arange(8)

    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict
    item = df.columns.get_loc(str(itemString))

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    cycleTime = list(cycleDict["CorrectedTimes"])

    color = 'tab:blue'
    df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-1, 10), ax=ax1, color=color, linewidth=3.3)
    ax1.set_ylabel('Resistance', color=color, fontsize=12)

    temp = df.columns.get_loc("A")
    tick_separation = list(range(0, len(df.index), 50))
    xticker = list(df.iloc[:, temp])

    xticker_1 = list()
    for i in tick_separation:
        xticker_1.append(xticker[i])

    xticker_1 = [round(element) for element in xticker_1]
    plt.xticks(tick_separation, xticker_1)
    plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=14)

    cycleNumber = cycleDict.get('Cycle')
    fig.suptitle('Cycle ' + str(cycleNumber) + ": " + "R149:Drill_Pad", fontsize='large')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def plot_Component_time_function(CycleDataSet, itemString):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict
    item = df.columns.get_loc(str(itemString))

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    cycleTime = list(cycleDict["CorrectedTimes"])
    print(cycleTime)

    color = 'tab:blue'
    df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-1, 50), ax=ax1, color=color, linewidth=3.3)
    ax1.set_ylabel('Resistance', color=color, fontsize=20)

    format = '%H:%M:%S'
    for time in cycleTime:
        temp_time_list = strptime(time, format)
    desired_time = strptime("04:00:00", format)

    hours = list()
    hours.append(dt.datetime.strptime("01:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("02:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("03:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("04:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("05:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("06:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("07:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("08:00:00", "%H:%M:%S"))

    times_list = list()
    temp_thing = list()
    temp_thing.append(0)
    for hour in hours:
        times_list.append(min(cycleTime, key=lambda t: abs(hour - dt.datetime.strptime(t, "%H:%M:%S"))))
        print(df.loc[[cycleTime.index(min(cycleTime, key=lambda t: abs(hour - dt.datetime.strptime(t, "%H:%M:%S"))))]])
        temp_thing.append(
            cycleTime.index(min(cycleTime, key=lambda t: abs(hour - dt.datetime.strptime(t, "%H:%M:%S")))))

    print(times_list)
    print(temp_thing)

    color = 'tab:red'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    tempString = df.columns.get_loc("C3")
    df.iloc[:, tempString].plot(x=cycleTime, y=df.iloc[:, item], ylim=(9, 310), ax=ax2, color=color, linewidth=3.3)
    ax2.grid(False)

    yticker = list([0, 50, 100, 150, 200, 250, 300])
    plt.yticks(yticker)
    plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=14)

    foo = cycleTime[-1]
    foo = foo[:-3]
    # xticker_1 = list([ 0,1,2,3,4,5,6,7,8,foo ])#[round(element) for element in xticker_1]
    xticker_1 = list([0, 1, 2, 3, 4, 5, 6, 7, foo])  # [round(element) for element in xticker_1]
    tick_separation = temp_thing
    # tick_separation.append(9)
    plt.xticks(tick_separation, xticker_1)
    plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=14)

    # plt.xlabel("Time (Hours)")
    color = "black"
    ax1.set_xlabel('Time (Hours)', color=color, fontsize=18)

    cycleNumber = cycleDict.get('Cycle')
    # fig.suptitle('Cycle '+str(cycleNumber)+": "+"R149:Drill_Pad",fontsize='large')
    fig.suptitle('Cycle ' + str(cycleNumber) + ": " + "R208:CABGA 256", fontsize='large')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    df = CycleDataSet.DataFrame
    Info500 = CycleDataSet.DataSetDict
    fig, ((ax)) = plt.subplots(nrows=1, ncols=1, sharex=True)  # ,sharey=True,figsize=(10,5))
    cycleTime = list(Info500["CorrectedTimes"])


def plot_Components_time_function(CycleDataSet, Component_Group):
    df = CycleDataSet.DataFrame
    cycleDict = CycleDataSet.DataSetDict
    item = df.columns.get_loc("R223:BP2")

    fig, (ax1) = plt.subplots(nrows=1, ncols=1)
    cycleTime = list(cycleDict["CorrectedTimes"])
    print(cycleTime)

    color = 'tab:blue'
    # df.iloc[:, item].plot(x=cycleTime, y=df.iloc[:, item], ylim=(-1, 50), ax=ax1, color=color, linewidth=3.3)
    # ax1.set_ylabel('Resistance', color=color, fontsize=20)

    itemList = list(Component_Group)
    itemList = [element for element in itemList if "R" in element]

    for itemString in itemList:
        itemColumn = df.columns.get_loc(str(itemString))
        df.iloc[:, itemColumn].plot(x=cycleTime, y=df.iloc[:, itemColumn], ylim=(15, 65), ax=ax1)  # -.1,2
    ax1.set_ylabel('Resistance', fontsize=20)
    ax1 = plt.gca()

    format = '%H:%M:%S'
    for time in cycleTime:
        temp_time_list = strptime(time, format)
    desired_time = strptime("04:00:00", format)

    hours = list()
    hours.append(dt.datetime.strptime("01:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("02:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("03:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("04:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("05:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("06:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("07:00:00", "%H:%M:%S"))
    hours.append(dt.datetime.strptime("08:00:00", "%H:%M:%S"))
    # hours.append(dt.datetime.strptime("09:00:00", "%H:%M:%S"))
    # hours.append(dt.datetime.strptime("08:00:00", "%H:%M:%S"))

    times_list = list()
    temp_thing = list()
    temp_thing.append(0)
    for hour in hours:
        times_list.append(min(cycleTime, key=lambda t: abs(hour - dt.datetime.strptime(t, "%H:%M:%S"))))
        print(df.loc[
                  [cycleTime.index(min(cycleTime, key=lambda t: abs(hour - dt.datetime.strptime(t, "%H:%M:%S"))))]])
        temp_thing.append(
            cycleTime.index(min(cycleTime, key=lambda t: abs(hour - dt.datetime.strptime(t, "%H:%M:%S")))))

    print(times_list)
    print(temp_thing)

    color = 'tab:red'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Temperature', color=color, fontsize=20)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)
    tempString = df.columns.get_loc("C3")
    df.iloc[:, tempString].plot(x=cycleTime, y=df.iloc[:, item], ylim=(9, 310), ax=ax2, color=color, linewidth=3.3)
    ax2.grid(False)

    yticker = list([0, 50, 100, 150, 200, 250, 300])
    plt.yticks(yticker)
    plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=14)

    foo = cycleTime[-1]
    foo = foo[:-3]
    # xticker_1 = list([ 0,1,2,3,4,5,6,7,8,foo ])#[round(element) for element in xticker_1]
    xticker_1 = list([0, 1, 2, 3, 4, 5, 6, 7, foo])  # [round(element) for element in xticker_1]
    tick_separation = temp_thing
    # tick_separation.append(9)
    plt.xticks(tick_separation, xticker_1)
    plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=14)

    # plt.xlabel("Time (Hours)")
    color = "black"
    ax1.set_xlabel('Time (Hours)', color=color, fontsize=18)

    plt.margins(x=0)
    # ax1 = plt.gca()

    cycleNumber = cycleDict.get('Cycle')
    # fig.suptitle('Cycle '+str(cycleNumber)+": "+"R149:Drill_Pad",fontsize='large')
    fig.suptitle('Cycle ' + str(cycleNumber) + ": " + "MUX Modules", fontsize='large')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
