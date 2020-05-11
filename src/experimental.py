# This file contains various pieces of old/experimental code. Don't use it unless you know what you are doing.
######################################
######################################
######################################

# https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html


##machine learning cont.
# https://jakevdp.github.io/PythonDataScienceHandbook/05.00-machine-learning.html

##error bars
# https://jakevdp.github.io/PythonDataScienceHandbook/04.03-errorbars.html

##histograms, bins, and density
# https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html

##texts and annotations
# https://jakevdp.github.io/PythonDataScienceHandbook/04.09-text-and-annotation.html

##improving visuals
# https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html

##seaborn package
# https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html

##plot ticks
# https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html

##plotting examples
# https://matplotlib.org/gallery.html
#####################################################################

# TODO::go through excel spreadsheet of modified cycle and redo column header implementation ...
# change the implementation appropriately in the cycles and file files, among others

# print('Median value of preTestScore')
# print(df['R159:BP1'].median())
#
# print('Sample variance of preTestScore values')
# print(df['R159:BP1'].var())
#
# print('Sample standard deviation of preTestScore values')
# print(df['R159:BP1'].std())
#
# print('Skewness of preTestScore values')
# print(df['R159:BP1'].skew())

##Cycle500 = file.CycleDataSet(const.FNAME499,500)
# df = Cycle500.cycleDataFrame
# Info500 = Cycle500.cycleInfo
#
# print(Cycle500.cycleDataFrame.groupby('Stage').Stage.count())
# print(Cycle500.cycleDataFrame['Stage'].value_counts())
#
# print("df description")
# print(df.describe())
##print(df)
#
# print("df where resistor is 999 method 1")
# print(df.loc[df['R159:BP1'] == 999, ['R98:BP1']])
# print('\n')
# print("df where resistor is 999 method 2")
# print(df.loc[(lambda df: df['R98:BP1'] == 999),('R98:BP1')])
#
# print("normalized value counts")
# print(Cycle500.cycleDataFrame['R159:BP1'].value_counts(normalize=True,dropna=False))
#
# print("\n")
# print("nlargest values")
# print(Cycle500.cycleDataFrame['R159:BP1'].nlargest())
#
# print("qcut")
# print(pd.qcut(df['R159:BP1'], 4, duplicates='drop').value_counts())
#
#
# print('Count the number of non-NA values')
# print(df['R159:BP1'].count())
#
# print('Minimum value of preTestScore')
# print(df['R159:BP1'].min())
#
# print('Maximum value of preTestScore')
# print(df['R159:BP1'].max())
#
#
# print('Kurtosis of preTestScore values')
# print(df['R159:BP1'].kurt())
#
# print('Correlation Matrix Of Values')
# print(df.corr())
#
# print("covariance of matrix values")
# print(df.cov())
#####################################################################
#####################################################################
# df.head(n) | First n rows of the DataFrame
# df.tail(n) | Last n rows of the DataFrame
# df.shape() | Number of rows and columns
# df.info() | Index, Datatype and Memory information
# df.describe() | Summary statistics for numerical columns
# df.value_counts(dropna=False) | View unique values and counts
# df.apply(pd.Series.value_counts) | Unique values and counts for all columns
#
# Selection
# df[col] | Returns column with label col as Series
# df[[col1, col2]] | Returns columns as a new DataFrame
# df.iloc[0] | Selection by position
# df.loc['index_one'] | Selection by index
# df.iloc[0,:] | First row
# df.iloc[0,0] | First element of first column
#
# Data Cleaning
# df.columns = ['a','b','c'] | Rename columns
# pd.isnull() | Checks for null Values, Returns Boolean Arrray
# pd.notnull() | Opposite of pd.isnull()
# df.dropna() | Drop all rows that contain null values
# df.dropna(axis=1) | Drop all columns that contain null values
# df.dropna(axis=1,thresh=n) | Drop all rows have have less than n non null values
# df.fillna(x) | Replace all null values with x
# df.fillna(df.mean()) | Replace all null values with the mean (mean can be replaced with almost any function from the statistics section)
# df.astype(float) | Convert the datatype of the series to float
# df.replace(1,'one') | Replace all values equal to 1 with 'one'
# df.replace([1,3],['one','three']) | Replace all 1 with 'one' and 3 with 'three'
# df.rename(columns=lambda x: x + 1) | Mass renaming of columns
# df.rename(columns={'old_name': 'new_ name'}) | Selective renaming
# df.set_index('column_one') | Change the index
# df.rename(index=lambda x: x + 1) | Mass renaming of index
#
# Filter, Sort, and Groupby
# df[df[col] > 0.5] | Rows where the column col is greater than 0.5
# df[(df[col] > 0.5) & (df[col] < 0.7)] | Rows where 0.7 > col > 0.5
# df.sort_values(col1) | Sort values by col1 in ascending order
# df.sort_values(col2,ascending=False) | Sort values by col2 in descending order
# df.sort_values([col1,col2],ascending=[True,False]) | Sort values by col1 in ascending order then col2 in descending order
# df.groupby(col) | Returns a groupby object for values from one column
# df.groupby([col1,col2]) | Returns groupby object for values from multiple columns
# df.groupby(col1)[col2] | Returns the mean of the values in col2, grouped by the values in col1 (mean can be replaced with almost any function from the statistics section)
# df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) | Create a pivot table that groups by col1 and calculates the mean of col2 and col3
# df.groupby(col1).agg(np.mean) | Find the average across all columns for every unique col1 group
# df.apply(np.mean) | Apply the function np.mean() across each column
# nf.apply(np.max,axis=1) | Apply the function np.max() across each row
#
# Join/Combine
# df1.append(df2) | Add the rows in df1 to the end of df2 (columns should be identical)
# pd.concat([df1, df2],axis=1) | Add the columns in df1 to the end of df2 (rows should be identical)
# df1.join(df2,on=col1,how='inner') | SQL-style join the columns in df1 with the columns on df2 where the rows for col have identical values. how can be one of 'left', 'right', 'outer', 'inner'
#
# Statistics
# df.describe() | Summary statistics for numerical columns
# df.mean() | Returns the mean of all columns
# df.corr() | Returns the correlation between columns in a DataFrame
# df.count() | Returns the number of non-null values in each DataFrame column
# df.max() | Returns the highest value in each column
# df.min() | Returns the lowest value in each column
# df.median() | Returns the median of each column
# df.std() | Returns the standard deviation of each column
##########################################################
###from sklearn.gaussian_process import GaussianProcess
###
#### define the model and draw some data
###model = lambda x: x * np.sin(x)
###xdata = np.array([1, 3, 5, 6, 8])
###ydata = model(xdata)
###
#### Compute the Gaussian process fit
###gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
###                     random_start=100)
###gp.fit(xdata[:, np.newaxis], ydata)
###
###xfit = np.linspace(0, 10, 1000)
###yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
###dyfit = 2 * np.sqrt(MSE)  # 2*sigma ~ 95% confidence region
###We now have xfit, yfit, and dyfit, which sample the continuous fit to our data. We could pass these to the plt.errorbar function as above, but we don't really want to plot 1,000 points with 1,000 errorbars. Instead, we can use the plt.fill_between function with a light color to visualize this continuous error:
###
#### Visualize the result
###plt.plot(xdata, ydata, 'or')
###plt.plot(xfit, yfit, '-', color='gray')
###
###plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
###                 color='gray', alpha=0.2)
###plt.xlim(0, 10);
###########################################################


##################################
##################################
##################################
# Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.
#
# Examples:
# >>>
#
# >>> sum(i*i for i in range(10))                 # sum of squares
# 285
#
# >>> xvec = [10, 20, 30]
# >>> yvec = [7, 5, 3]
# >>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
# 260
#
# >>> from math import pi, sin
# >>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
#
# >>> unique_words = set(word  for line in page  for word in line.split())
#
# >>> valedictorian = max((student.gpa, student.name) for student in graduates)
#
# >>> data = 'golf'
# >>> list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']
#
#################################
#################################
#################################


######################################################################################

# TODO::redo x axis when its time so that it shows zeroed timescale

# plt.hist(resistBP1openList,histtype='step')

####################################################################
# plt.axis('tight');
# plt.axis('equal');


# plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
# plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
# plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
# plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
# plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
# plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
##If no color is specified, Matplotlib will
##automatically cycle through a set of default
##colors for multiple lines.

##Similarly, the line style can be adjusted using the
##linestyle keyword:
# plt.plot(x, x + 0, linestyle='solid')
# plt.plot(x, x + 1, linestyle='dashed')
# plt.plot(x, x + 2, linestyle='dashdot')
# plt.plot(x, x + 3, linestyle='dotted');

## For short, you can use the following codes:
# plt.plot(x, x + 4, linestyle='-')  # solid
# plt.plot(x, x + 5, linestyle='--') # dashed
# plt.plot(x, x + 6, linestyle='-.') # dashdot
# plt.plot(x, x + 7, linestyle=':');  # dotted

##Matplotlib does a decent job of choosing default axes limits
##for your plot, but sometimes it's nice to have finer
##control. The most basic way to adjust axis limits is
##to use the plt.xlim() and plt.ylim() methods:
# plt.plot(x, np.sin(x))
# plt.xlim(-1, 11)
# plt.ylim(-1.5, 1.5);

##If for some reason you'd like either axis to be
##displayed in reverse, you can simply reverse the
##order of the arguments:
# plt.plot(x, np.sin(x))
# plt.xlim(10, 0)
# plt.ylim(1.2, -1.2);

##A useful related method is plt.axis(). The plt.axis()
##method allows you to set the x and y limits with a
##single call, by passing a list which specifies
##[xmin, xmax, ymin, ymax]:
# plt.plot(x, np.sin(x))
# plt.axis([-1, 11, -1.5, 1.5]);
##The plt.axis() method goes even beyond this,
##allowing you to do things like automatically
##tighten the bounds around the current plot:
# plt.plot(x, np.sin(x))
# plt.axis('tight');
##It allows even higher-level specifications, such as
##ensuring an equal aspect ratio so that on your
##screen, one unit in x is equal to one unit in y:
# plt.plot(x, np.sin(x))
# plt.axis('equal');

##Titles and axis labels are the simplest such
##labels—there are methods that can be used to
##quickly set them:
# plt.plot(x, np.sin(x))
# plt.title("A Sine Curve")
# plt.xlabel("x")
# plt.ylabel("sin(x)");
##The position, size, and style of these labels can
##be adjusted using optional arguments to the function. For more information, see the Matplotlib documentation and the docstrings of each of these functions.
##When multiple lines are being shown within a single
##axes, it can be useful to create a plot legend that
##labels each line type. Again, Matplotlib has a
##built-in way of quickly creating such a legend. It
##is done via the (you guessed it) plt.legend() method. Though there are several valid ways of using this, I find it easiest to specify the label of each line using the label keyword of the plot function:
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.axis('equal')
# plt.legend();

# For transitioning between MATLAB-style functions and
# object-oriented methods, make the following changes:
# plt.xlabel() → ax.set_xlabel()
# plt.ylabel() → ax.set_ylabel()
# plt.xlim() → ax.set_xlim()
# plt.ylim() → ax.set_ylim()
# plt.title() → ax.set_title()
##In the object-oriented interface to plotting, rather
##than calling these functions individually, it is
##often more convenient to use the ax.set() method to
##set all these properties at once:
# ax = plt.axes()
# ax.plot(x, np.sin(x))
# ax.set(xlim=(0, 10), ylim=(-2, 2),
#       xlabel='x', ylabel='sin(x)',
#       title='A Simple Plot');

##The command plt.subplots_adjust can be used to adjust
##the spacing between these plots.
# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
# for i in range(1, 7):
#    ax = fig.add_subplot(2, 3, i)
#    ax.text(0.5, 0.5, str((2, 3, i)),
#           fontsize=18, ha='center')
##The hspace and wspace arguments of plt.subplots_adjust
##specify the spacing along the height and width of the
##figure, in units of the subplot size

# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
##Note that by specifying sharex and sharey, we've
##automatically removed inner labels on the grid to make
##the plot cleaner. The resulting grid of axes instances
##is returned within a NumPy array, allowing for
##convenient specification of the desired axes using
##standard array indexing notation:
## axes are in a two-dimensional array, indexed by [row, col]
# for i in range(2):
#    for j in range(3):
#        ax[i, j].text(0.5, 0.5, str((i, j)),
#                      fontsize=18, ha='center')
# fig

##To go beyond a regular grid to subplots that span
##multiple rows and columns, plt.GridSpec() is the best
##tool. The plt.GridSpec() object does not create a plot
##by itself; it is simply a convenient interface that is
##recognized by the plt.subplot() command.
# grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
# From this we can specify subplot locations and extents using the familiary Python slicing syntax:
# plt.subplot(grid[0, 0])
# plt.subplot(grid[0, 1:])
# plt.subplot(grid[1, :2])
# plt.subplot(grid[1, 2])
##########################################################
