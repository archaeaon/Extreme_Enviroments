# IMPORTS#
##library imports
from abc import ABCMeta, abstractmethod, ABC, abstractproperty


####################
####################

class DataSet_Abstract(object):
    """
    The abstract class for the various Panda DataFrame model data sets.

    Numerous concrete classes exist to deal with different versions of the
    program, each used for a different iteration of the data text file fields format.

    NOTE:The attributes in this list exist concretely i the cncrete classes, and not as an abstraction in the abstract class
    TODO::add these to the abstract class

    Attributes:
        DataFrame (pandas.DataFrame): Frame containing all of the data from
                                        the cycle with the exception of the date.
        DataSetDict (Dictionary): Dictionary of basic useful information that can be
                                  obtained from every cycle. See __parse_cycle for a
                                  complete list.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, cycleNumber):
        """Uses the cycleNumber to parse the correct file and fill the DataFrame and DataSetDict"""

    @abstractmethod
    def summary(self):
        """Prints several pieces of useful information about the DataSet."""
