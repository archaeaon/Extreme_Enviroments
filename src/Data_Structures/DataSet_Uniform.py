# IMPORTS#
##library imports
import copy
import pandas as pd

# import numpy as np
# np.set_printoptions(linewidth=100, edgeitems=1000000, threshold=np.nan)

import datetime as dt

strptime = dt.datetime.strptime

##program file imports
import Data_Structures.DataSet_Abstract as ADS

import File.file


####################
####################

# TODO::finish this
# TODO::document this
# TODO::add total time and number of samples information
class DataSet_Uniform(ADS.DataSet_Abstract):

    # cycleDataFrame  = 0
    # cycleInfo = 0

    def __init__(self, cycleNumber):
        # find appropriate filename and reason for that set
        fname, reason = file.cycleFile(cycleNumber)

        # parse the file and set cycleDataFrame
        self.DataFrame = DataSet_Uniform.__load_uniform(self, fname, cycleNumber)

        # use cycleDataFrame to get the cycle's information
        self.DataSetDict = DataSet_Uniform.__parse_uniform(self, fname, cycleNumber)

        # see the cycle's key info and ensure correct loading
        self.summary()
        ##this prints all info of the cycle in summarized form
        ##useful for debugging
        ##print(self.cycleDataFrame)

    def __load_uniform(self, fname, cycleNumber):
        fobj = open(fname, 'r', 1)

        # this block ensures that when an error is reached the file gets closed
        try:
            # read in the header line and ensure the newline character has been stripped
            headerList = fobj.readline().split('\t')
            headerList[-1] = headerList[-1].strip()

            # modify header list and create appropriate column list for the file format
            ##Formatting of the files via labview is inconsistent
            ##To avoid errors and simplify the first column
            ##of the file is ignored(the date part of the timestamp)
            elementset = list(range(1, len(headerList)))

            # The following commands ensure that the file data read in matches the
            # column headers; the labview files write data in the incorrect order.
            ##See appropriate excel spreadsheet analysis of file comparison before and after
            ######
            # correct the cycle header and stage header errors
            ##delete some unneccessary headers from header list and
            ##delete the columns under the cycles+stage headers before shifting
            # WARNING::DO NOT CHANGE THE ORDER OF OPERATIONS HERE OR IN LABVIEW WITHOUT CORRECTING THIS
            elementset.pop(headerList.index("Stage"))
            elementset.pop(headerList.index("Cycles"))
            headerList.remove("SetTubeTemp")
            headerList.remove("SetChamberTemp")
            headerList.remove("SetHeatSwitchTemp")

            # strip all extra whitespace from the header list
            ##prevents errors do to inconsistent formatting
            for i, element in enumerate(headerList):
                headerList[i] = element.replace(" ", "")
                print(headerList[i])
            ######

            # create the appropriate row list
            ##the row list ensures that when the file is read, only the
            ##apropriate data is put into the DataFrame. Unfortunately,
            ##this requires iterating through every line of the file.
            rowList = []
            i, numline = 0, 0
            for line in fobj:
                numline = numline + 1
                i = i + 1
                parts = line.split()
                tempint = headerList.index("Cycles") + 1
                if parts[tempint] == str(cycleNumber):
                    rowList.append(i)

            # create the rowSet by subtracting all rows not in rowlist from it
            ##the rowSet list is used to ensure that read_csv only reads in the correct lines
            tempList = list(range(0, numline + 1))
            rowSet = set(set(tempList) - set(rowList))

            # read in the data from the file and pd_frame it
            cycleDataFrame = pd.read_csv(fname, sep="\s+", skiprows=rowSet, usecols=elementset, names=headerList)

            # Now read the date part of the file into a pd.Series and stick it in cycleDataFrame
            tempSeries = pd.read_csv(fname, sep="\s+", skiprows=rowSet, usecols=[0], squeeze=True, header=None,
                                     infer_datetime_format=True)
            ##insert series into Frame at same location as in file
            cycleDataFrame.insert(0, 'Date', tempSeries)

        # deal with exception errors and else on try success
        except (IOError, EOFError, ValueError):
            print("There was an error parsing file " + str(fname) + " for cycle " + str(cycleNumber))
            if IOError:
                print(IOError)
            elif EOFError:
                print(EOFError)
            else:
                print(ValueError)
            raise
        # occurs on successful parsing
        else:
            print("Cycle " + str(cycleNumber) + " parsed successfully.")
            return cycleDataFrame
        finally:
            fobj.close()

    def __parse_uniform(self, fname, cycleNumber):
        # copy is used to ensure a shallow copy(pass by reference) of the object is passed
        df = copy.copy(self.cycleDataFrame)

        ###GENERIC###
        # get some simple data for the dict
        genKeys = ('File', 'Cycle')
        genValues = (fname, cycleNumber)
        fullDict = dict(zip(genKeys, genValues))

        # ###ROWS###
        # # get the total number of rows and rows for each stage of the cycle
        # totalRows = len(df.index) - 1
        # rampdownRows = df.loc[df['Stage'] == 2].index
        # soakdownRows = df.loc[df['Stage'] == 8].index
        # rampupRows = df.loc[df['Stage'] == 1].index
        # soakupRows = df.loc[df['Stage'] == 4].index
        #
        # rowKeys = ('totalRows', 'rampdownRows', 'soakdownRows', 'rampupRows', 'soakupRows')
        # rowValues = (totalRows, rampdownRows, soakdownRows, rampupRows, soakupRows)
        # rowDict = dict(zip(rowKeys, rowValues))
        # fullDict.update(rowDict)
        #
        # ###TIME###
        # # get the appropriate time data for the timeDict
        # format = '%Y-%m-%d %H:%M:%S'
        # ##NOTE::These times are slightly off. Uses the last recorded endtime;
        # ##Should first time of next cycle be used instead??
        # ##avg. time between recording is 1 min. 2 sec.
        #
        # # create the strings to be used in the creation of the Time types and do the math to find them
        # # then turn them into time variables and perform math to get the runtimes
        # ##StartTime
        # startString = df.loc[0]["Date"] + " " + df.loc[0]["Timestamp"]
        # StartTime = str(strptime(startString, format))
        #
        # ##EndTime
        # endString = df.loc[totalRows]["Date"] + " " + df.loc[totalRows]["Timestamp"]
        # EndTime = str(strptime(endString, format))
        #
        # ##SoakDownStartTime
        # soakdownstartString = df.loc[soakdownRows[0]]["Date"] + " " + df.loc[soakdownRows[0]]["Timestamp"]
        # SoakDownStartTime = str(strptime(soakdownstartString, format))
        #
        # ##RampUpStartTime
        # rampupstartString = df.loc[rampupRows[0]]["Date"] + " " + df.loc[rampupRows[0]]["Timestamp"]
        # RampUpStartTime = str(strptime(rampupstartString, format))
        #
        # ##SoakUpStartTime
        # soakupstartString = df.loc[soakupRows[0]]["Date"] + " " + df.loc[soakupRows[0]]["Timestamp"]
        # SoakUpStartTime = str(strptime(soakupstartString, format))
        #
        # ##RampUpTime = RampUpEnd/SoakUpStart - SoakDownEnd/RampUpStart
        # RampUpTime = str(strptime(SoakUpStartTime, format) - strptime(RampUpStartTime, format))
        #
        # ##SoakUpTime = End - RampUpEnd/SoakUpStart
        # SoakUpTime = str(strptime(EndTime, format) - strptime(SoakUpStartTime, format))
        #
        # ##RampDownTotal = RampDownEnd/SoakDownStart - Start
        # RampDownTime = str(strptime(SoakDownStartTime, format) - strptime(StartTime, format))
        #
        # ##SoakDownTotal = SoakDownEnd/RampUpStart - RampDownEnd/SoakDownStart
        # SoakDownTime = str(strptime(RampUpStartTime, format) - strptime(SoakDownStartTime, format))
        #
        # ##Total/RunTime = EndTime - StartTime
        # RunTime = str(strptime(EndTime, format) - strptime(StartTime, format))
        #
        # # Correct the timestamps so they start at 00:00:00
        # ##these are used when plotting so that the timestamp is zeroed
        # CorrectedTimes = list()
        # for index, row in df.iterrows():
        #     currentString = row["Date"] + " " + row["Timestamp"]
        #     CurrentTime = str(strptime(currentString, format))
        #     CorrectedTimes.append(str(strptime(CurrentTime, format) - strptime(StartTime, format)))
        #
        # timeKeys = (
        # 'Date', 'StartTime', 'RampDownTime', 'SoakDownTime', 'RampUpTime', 'SoakUpTime', 'EndTime', 'RunTime',
        # 'CorrectedTimes')
        # timeValues = (
        # 999, StartTime, RampDownTime, SoakDownTime, RampUpTime, SoakUpTime, EndTime, RunTime, CorrectedTimes)
        # timeDict = dict(zip(timeKeys, timeValues))
        # fullDict.update(timeDict)

        ###COMPONENT LISTS###
        # create the lists to be used in the for loop
        resistBP1List = list()
        resistBP2List = list()
        resistMUXList = list()
        capBP1List = list()
        capBP2List = list()
        otherList = list()

        # iterate through the columns and put components into the appropriate lists
        columnList = list(df.columns.values)
        for i, header in enumerate(columnList):
            if header[0] is 'R' and "BP1" in header:
                resistBP1List.append(i)
            elif header[0] is 'R' and "BP2" in header:
                resistBP2List.append(i)
            elif header[0] is 'R' and "MUX" in header:
                resistMUXList.append(i)
            elif header[0] is 'C' and "BP1" in header:
                capBP1List.append(i)
            elif header[0] is 'C' and "BP2" in header:
                capBP2List.append(i)
            else:
                otherList.append(i)

        componentKeys = ('resistBP1List', 'resistBP2List', 'resistMUXList', 'capBP1List', 'capBP2List', 'otherList')
        componentValues = (resistBP1List, resistBP2List, resistMUXList, capBP1List, capBP2List, otherList)
        componentDict = dict(zip(componentKeys, componentValues))
        fullDict.update(componentDict)

        ###TEMPERATURE###
        ##make sure to include average ramp down and ramp up rates
        ###PRESSURE###
        ###coldplate/coldfinger???###
        ###missing data number###
        ##DataFrame.isna()	Detect missing values
        ###FAILURE BY TYPE###
        ###gets counts of how many opens there are for each resistor###
        # the specific resistor can be identified by using the reistorBPList
        ###        resistBP1openList = list()
        ###        for resistor in resistBP1List:
        ###            tempList = df[df.columns[resistor]].value_counts()
        ###            print(tempList.iloc[0])
        ###            resistBP1openList.append(tempList.iloc[0])
        ###        print(resistBP1openList)

        ###MEAN,VAR,STD###

        ###print(df['R159:BP1'].value_counts(normalize=True,dropna=False))
        ###print(pd.qcut(df['R159:BP1'],4,duplicates='drop').value_counts())
        return fullDict

    def summary(self):
        print("\tFile: " + self.DataSetDict.get('File'))
        print("\tDate: " + str(self.DataSetDict.get('Date')))
        print("\tMeasurements: " + str(self.DataSetDict.get('totalRows')))
        # print("\tRunTime: " + self.DataSetDict.get('RunTime'))

####################
