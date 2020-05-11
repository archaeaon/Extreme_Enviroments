# perform a test over every library to be used
# print the version and ensure that the libraries were loaded correctly
def importTest():
    print()

    try:
        import sys
        print("sys imported.")

        import copy
        print("copy imported")

        import abc
        print("abc imported")

        import datetime as dt
        print("datetime imported")

        # import numpy as np
        # print("NumPy version:" + np.__version__ + " imported.")

        import pandas as pd
        print("Pandas version:" + pd.__version__ + " imported.")

        import matplotlib as mpl
        print("Matplotlib version:" + mpl.__version__ + " imported.")

        import seaborn as sns
        print("Seaborn version:" + sns.__version__ + " imported.")

    except:
        print("Error loading modules.")

    else:
        # datetime customization
        strptime = dt.datetime.strptime

        # NumPy customization
        # np.set_printoptions(linewidth=100, edgeitems=1000000, threshold=np.nan)

        # MatPlotLib customization
        import matplotlib.pyplot as plt
        plt.style.use('classic')
        plt.style.use('seaborn-whitegrid')

####################
####################

# import SciPy
