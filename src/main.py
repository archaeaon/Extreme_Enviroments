####################
####################
##USED KEYWORS##
# TODO
# FIXME
# WARNING
# NOTE
####################
####################
# Begin by setting up the logging functions
# TODO::create logging level classification
# TODO::create logging for CL output
# TODO::create logging for file parsing
# TODO::finish logging setup and test
# TODO::add plot logging
# TODO:: add logging toggle functions
import os

if os.path.exists("log_.log"):
    os.remove("log_.log")
else:
    print("The file 'log_.log' does not exist")

import logging
##import config
from Utility import logger as log


def main():
    logging.basicConfig(filename='log_.log', level=logging.INFO)
    logging.info('Started')
    log.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()

##########################################################################################
# TODO::Finish logger setup
# logger = logging.getLogger()
# logging.basicConfig(filename='myapp.log', filemode='w', level=logging.INFO)
# log.logger_setup()

# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#
# fh = logging.FileHandler('log_.txt')    #file handler
# fh.setLevel(config.FH_LOG_LEVEL)
# fh.setFormatter(formatter)
# logger.addHandler(fh)
#
# ch = logging.StreamHandler()            #console handler
# ch.setLevel(config.CH_LOG_LEVEL)
# ch.setFormatter(formatter)
# logger.addHandler(ch)

# logging.debug('Logger debug')
#
# logging.info('Logger info')
#########################################################################################
#                                      Imports                                          #
#########################################################################################

##Start with the imports file since it is used over all files.
##Then run a test over all used import modules to ensure correct loading and versioning.
from Utility import imports as imp

imp.importTest()

# import libraries and set them up as desired
import copy
import datetime as dt

strptime = dt.datetime.strptime
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

# TODO::average time between measuring each data point
# import the DataSet classes that will hold the file information
import Data_Structures.DataSet_Abstract as ADS
import Data_Structures.DataSet_Cycle as CCDS
import Data_Structures.DataSet_Uniform as CUDS
import File.Groups as Groups

# TODO::add autoranging with error checking(use slopes??)
# import the plotting files
import Plot.plot_component as plt_comp
import Plot.plot_pressure as plt_pres
import Plot.plot_temperature as plt_temp

# import other
import to_finish as finish

#########################################################################################
#                                Command Line Functions                                 #
#########################################################################################

# TODO::write help functions for all functions
# Help functions can be run on all functions and objects like so:
# help(CCDS)

#########################################################################################
#                                       Cycles                                          #
#########################################################################################

##Define the cycles you wish to use here##
# Be sure to comment out cycles that you don't need to shorten total runtime

# CycleDataSet86 = CCDS.DataSet_Cycle(86)
# CycleDataSet92 = CCDS.DataSet_Cycle(92)
# CycleDataSet292 = CCDS.DataSet_Cycle(292)
# CycleDataSet359 = CCDS.DataSet_Cycle(359)
# CycleDataSet419 = CCDS.DataSet_Cycle(419)
# CycleDataSet446 = CCDS.DataSet_Cycle(446)
# CycleDataSet490 = CCDS.DataSet_Cycle(490)
# CycleDataSet500 = CCDS.DataSet_Cycle(500)
# CycleDataSet514 = CCDS.DataSet_Cycle(514)
# CycleDataSet678 = CCDS.DataSet_Cycle(678)
# CycleDataSet711 = CCDS.DataSet_Cycle(711)
# CycleDataSet724 = CCDS.DataSet_Cycle(724)
# CycleDataSet929 = CCDS.DataSet_Cycle(929)
# CycleDataSet945 = CCDS.DataSet_Cycle(945)
# CycleDataSet1014 = CCDS.DataSet_Cycle(1014)
# CycleDataSet1059 = CCDS.DataSet_Cycle(1059)

#########################################################################################
#                                  Component Lists                                      #
#########################################################################################

# This list is of all broken components on boards removed from the chamber at the end of cycle 1059
Broken_Board_Components = list()
Broken_Board_Components.extend(['R149', 'R162', 'R175', 'R208', 'R338', 'R351'])
Broken_Board_Components = [element + ":BP1" for element in Broken_Board_Components]

#########################################################################################
#                                 Component Groups                                      #
#########################################################################################

# These are the function calls for each board. Use this call as the component list passed to functions.

##### Side A Components #####
# Groups.Board_A1_Components())
# Groups.Board_A2_Components())
# Groups.Board_A3_Components())
# Groups.Board_A4_Components())
# Groups.Board_A5_Components())
# Groups.Board_A6_Components())
# Groups.Board_A7_Components())
# Groups.Board_A8_Components())
# Groups.Board_A9_Components())
# Groups.Board_A10_Components())
# Groups.Board_A11_Components())
# Groups.Board_A12_Components())
# Groups.Board_A13_Components())
# Groups.Board_A14_Components())
# Groups.Board_A15_Components())
# Groups.Board_A16_Components())
# Groups.Board_A22_Components())

##### Side B Components #####
# Groups.Board_B1_Components())
# Groups.Board_B2_Components())
# Groups.Board_B3_Components())
# Groups.Board_B4_Components())
# Groups.Board_B5_Components())
# Groups.Board_B6_Components())
# Groups.Board_B7_Components())
# Groups.Board_B8_Components())
# Groups.Board_B9_Components())
# Groups.Board_B10_Components())
# Groups.Board_B11_Components())
# Groups.Board_B12_Components())
# Groups.Board_B13_Components())
# Groups.Board_B14_Components())
# Groups.Board_B15_Components())
# Groups.Board_B16_Components())
# Groups.Board_B21_Components())
# Groups.Board_B22_Components())

#########################################################################################
#                                     TEMPERATURE                                       #
#########################################################################################
# TODO::Finish this. This list should be automatically called by all temperature list users.
# TODO:: If a user wishes to be able to define custom lists for different cycles, they should be able to pass them into temperature functions.
# Use this list to define temperature diodes that you wish to plotted. If you wish to use all available diodes, use the second list instead.
# Additionally, note that the diode labels beginning with '2' are actually Side B diodes and do not begin with '2' in the LabVIEW files.

# TODO::The ability to plot temperature on a graph should be easy to toggle for any type of graph.
# This variable determines whether a temperature axis is automatically added to plots
Add_Temperature_Axis = True

# TODO:: Bad diodes should be auto filtered out on a cycle by cycle basis.
# List of Desired Diodes
Temperature_Diodes_List = ["A", "B", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "2B", "2C", "2D1", "2D2",
                           "2D3", "2D4", "2D5"]

# List of ALL diodes
# Temperature_Diodes_List = ["A","B","C2","C3","C4","C5","D1","D2","D3","D4","D5","2B","2C","2D1","2D2","2D3","2D4","2D5"]

# TODO::Create a funcion to average all temperatures in the list and then use the average for plots

#########################################################################################

##Prototypes for various plotting functions##

##function to look at the behavour of all components for a single cycle
# plt_comp.plot_Cycle(~put DataSet here~)

##function to look at the behavoir of the MUX Resistors
# plt_comp.plot_MUX_Resistors(~put DataSet here~)

##function to look at the behavoir of a specific component for a single cycle
# plt_comp.plot_Component(~put DataSet here~,~put Component here~)

##function to look at the change of a component's behavior between two cycles
# plt_comp.plot_Difference(~put Minuend DataSet here~,~put Subtrahend DataSet here~,~put Component here~)

##function to plot a graph of the temperatures over a single cycle
# plt_temp.plot_Temperatures(~put_DataSet_here~, ~put_diode_list_here~):


# CycleDataSet292 = CCDS.DataSet_Cycle(292)
# CycleDataSet329 = CCDS.DataSet_Cycle(329)
# CycleDataSet331 = CCDS.DataSet_Cycle(331)
# CycleDataSet337 = CCDS.DataSet_Cycle(337)
# CycleDataSet340 = CCDS.DataSet_Cycle(340)
# CycleDataSet341 = CCDS.DataSet_Cycle(341)
# CycleDataSet344 = CCDS.DataSet_Cycle(344)
# CycleDataSet349 = CCDS.DataSet_Cycle(349)
# CycleDataSet353 = CCDS.DataSet_Cycle(353)
# CycleDataSet359 = CCDS.DataSet_Cycle(359)
# CycleDataSet360 = CCDS.DataSet_Cycle(360)
# CycleDataSet419 = CCDS.DataSet_Cycle(419)
# CycleDataSet421 = CCDS.DataSet_Cycle(421)
# CycleDataSet434 = CCDS.DataSet_Cycle(434)
# CycleDataSet445 = CCDS.DataSet_Cycle(445)
# CycleDataSet460 = CCDS.DataSet_Cycle(460)
# CycleDataSet480 = CCDS.DataSet_Cycle(480)
# CycleDataSet446 = CCDS.DataSet_Cycle(446)
# CycleDataSet490 = CCDS.DataSet_Cycle(490)
# CycleDataSet500 = CCDS.DataSet_Cycle(500)
# CycleDataSet469 = CCDS.DataSet_Cycle(469)
# CycleDataSet472 = CCDS.DataSet_Cycle(472)
# CycleDataSet478 = CCDS.DataSet_Cycle(478)
# CycleDataSet480 = CCDS.DataSet_Cycle(480)
# CycleDataSet484 = CCDS.DataSet_Cycle(484)
# CycleDataSet489 = CCDS.DataSet_Cycle(489)
# CycleDataSet496 = CCDS.DataSet_Cycle(496)
# CycleDataSet498 = CCDS.DataSet_Cycle(498)
# CycleDataSet499 = CCDS.DataSet_Cycle(499)
# CycleDataSet495 = CCDS.DataSet_Cycle(495)
# CycleDataSet500 = CCDS.DataSet_Cycle(500)
# CycleDataSet501 = CCDS.DataSet_Cycle(501)
# CycleDataSet503 = CCDS.DataSet_Cycle(503)
# CycleDataSet504 = CCDS.DataSet_Cycle(504)
# CycleDataSet506 = CCDS.DataSet_Cycle(506)
# CycleDataSet510 = CCDS.DataSet_Cycle(510)
# CycleDataSet512 = CCDS.DataSet_Cycle(512)
# CycleDataSet513 = CCDS.DataSet_Cycle(513)
# CycleDataSet514 = CCDS.DataSet_Cycle(514)
# CycleDataSet520 = CCDS.DataSet_Cycle(520)
# CycleDataSet536 = CCDS.DataSet_Cycle(536)
# CycleDataSet579 = CCDS.DataSet_Cycle(579)
# CycleDataSet592 = CCDS.DataSet_Cycle(592)
# CycleDataSet594 = CCDS.DataSet_Cycle(594)
# CycleDataSet610 = CCDS.DataSet_Cycle(610)
# CycleDataSet678 = CCDS.DataSet_Cycle(678)
# CycleDataSet711 = CCDS.DataSet_Cycle(711)
# CycleDataSet724 = CCDS.DataSet_Cycle(724)
# CycleDataSet929 = CCDS.DataSet_Cycle(929)
# CycleDataSet936 = CCDS.DataSet_Cycle(936)
# CycleDataSet944 = CCDS.DataSet_Cycle(944)
# CycleDataSet1014 = CCDS.DataSet_Cycle(1014)
# CycleDataSet1059 = CCDS.DataSet_Cycle(1059)


CycleDataSet1236 = CCDS.DataSet_Cycle(1236)
plt_comp.plot_Cycle(CycleDataSet1236)
# plt_comp.plot_BP_Resistors(CycleDataSet1236)
# plt_comp.plot_MUX_Resistors(CycleDataSet1236)


# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A1_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A2_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A3_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A4_Components())
plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A5_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A6_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A7_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A8_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A9_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A10_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A11_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A12_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A13_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A14_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A15_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A16_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A17_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A18_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A21_Components())
# plt_comp.plot_Components(CycleDataSet1236, Groups.Board_A22_Components())


plt_comp.plot_Component(CycleDataSet1236, "R79:BP1")

# def plot_BP_Resistors(abstract_DataSet):
# def plot_MUX_Resistors(CycleDataSet):
# def plot_ALL_Resistors(CycleDataSet):
# def plot_Capacitors(CycleDataSet):
# def plot_SMT_Capacitors(CycleDataSet):
# def plot_Cycle(CycleDataSet):
# def plot_Component(CycleDataSet, itemString):
# def plot_Components(CycleDataSet, itemList):
# def plot_Group(CycleDataSet, Component_Group):
# def plot_resistor_Group(CycleDataSet, Component_Group):
# def plot_capacitor_Group(CycleDataSet, Component_Group):
# def plot_mux_Group(CycleDataSet, Component_Group):
# def plot_Difference(Minuend, Subtrahend, itemString):
# def plot_Component_temp_function(CycleDataSet, itemString):
# def test_transform(CycleDataSet, itemString):
# def nearest(items, pivot)
# def plot_Component_time_function(CycleDataSet, itemString)
# def plot_Components_time_function(CycleDataSet, Component_Group)


plt.show()
