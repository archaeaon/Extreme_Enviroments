#########################################################################################
#                                        Imports                                        #
#########################################################################################

import datetime as dt

strptime = dt.datetime.strptime

#########################################################################################
#                                    Path Variable                                      #
#########################################################################################

path = "/media/kronos/UNSORTED 2/Extreme_Enviroments_Data/"


#########################################################################################
#                                  Plotting Functions                                   #
#########################################################################################

# TODO::Cycle fail reasons for cycles 0-1059
def cycleFile(cycleNumber):
    if 1 <= cycleNumber <= 18:
        # TODO::fix formatting; doesn't have headers
        # TODO::check values(suspicous) and take account of program stop reason
        fname = path + '2018-01-17 173248.txt'
        reason = "Test1 shut down because issues with the MUX board micro controller. I was moving some wires and it stopped working. Issue fixed. Opened the can to attach Tin Pest samples to the backplane"

    elif 19 <= cycleNumber <= 84:
        # TODO::fix formatting; doesn't have headers
        # TODO::investigate effect of reason on data
        fname = path + '2018-01-25 080226.txt'
        reason = "Test2 shut down because SMT board 16 on backplane A was not accounted for. Reset the program to include board 16; some bugs were fixed such as adding the component's value to the temporary file."
    ##NOTE::Test2a files ignored, not sure what they were
    ##contain enoguh info to be data, but were missing many desired fields
    ##copy in rawDATA for later analysis
    ##cycle 85 failed in RampUp

    elif 86 <= cycleNumber <= 91:
        # TODO::fix formatting; doesn't have headers
        # TODO::investigate effect of reason on data gathered from this test and previous tests
        fname = path + '2018-02-15 235737.txt'
        reason = "Test3 was shut down since all the MUX board's were reading in parallel."

    elif 92 <= cycleNumber <= 96:
        # TODO::fix formatting; incomplete header list
        fname = path + '2018-02-17 230322.txt'
        reason = ""

    else:
        # TODO::fix this to raise an error and clean up rest of function given ELSE limitation
        print("Cycle not specified anywhere")
        reason = "NULL reason"

    if 292 <= cycleNumber <= 307:
        fname = path + '2018-05-07 004334.txt'
        reason = ""

    if 309 <= cycleNumber <= 337:
        fname = path + '2018-05-12 141809.txt'
        reason = ""

    if 340 <= cycleNumber <= 359:
        fname = path + '2018-05-22 200724.txt'
        reason = ""

    elif cycleNumber == 360:
        fname = path + '2018-05-29 185432.txt'
        reason = ""

    if 419 <= cycleNumber <= 434:
        fname = path + '2018-06-19 091637.txt'
        reason = ""

    if 446 <= cycleNumber <= 465:
        fname = path + '2018-07-03 093711.txt'
        reason = ""

    # if 467 <= cycleNumber <= 468:
    #     fname = path + '2018-07-10 092536.txt'
    #     reason = ""

    elif 468 <= cycleNumber <= 470:
        fname = path + '2018-07-11 125059.txt'
        reason = ""


    elif 472 <= cycleNumber <= 478:
        fname = path + '2018-07-14 070926.txt'
        reason = ""

    # if cycleNumber == 479:
    #     fname = path + '2018-07-16 195552.txt'
    #     reason = ""

    elif 480 <= cycleNumber <= 500:
        fname = path + '2018-07-17 094742.txt'
        reason = ""

    if cycleNumber == 501:
        fname = path + '2018-07-24 095820.txt'
        reason = ""

    elif cycleNumber == 503:
        fname = path + '2018-11-02 111451.txt'
        reason = ""

    elif cycleNumber == 504:
        fname = path + '2018-11-05 203204.txt'
        reason = ""

    elif cycleNumber == 506:
        fname = path + '2018-11-12 132458.txt'
        reason = ""

    elif 510 <= cycleNumber <= 511:
        fname = path + '2018-12-02 162736.txt'
        reason = ""

    elif 511 <= cycleNumber <= 513:
        fname = path + '2018-12-11 124817.txt'
        reason = ""

    elif 514 <= cycleNumber <= 537:
        fname = path + '2018-12-12 222822.txt'
        reason = ""

    elif 540 <= cycleNumber <= 579:
        fname = path + '2019-01-07 003005.txt'
        reason = ""

    elif 581 <= cycleNumber <= 592:  ##duplicate at 593 check this
        fname = path + '2019-01-20 164421.txt'
        reason = ""

    elif 593 <= cycleNumber <= 611:
        fname = path + '2019-01-25 124041.txt'
        reason = ""

    elif 613 <= cycleNumber <= 671:
        fname = path + '2019-01-31 235718.txt'
        reason = ""

    elif 672 <= cycleNumber <= 735:
        fname = path + '2019-02-20 162730.txt'
        reason = ""

    elif cycleNumber == 929:
        fname = path + '2019-06-28 151520.txt'
        reason = ""

    elif 936 <= cycleNumber <= 939:
        fname = path + '2019-07-09 132624.txt'
        reason = ""

    elif 941 <= cycleNumber <= 945:
        fname = path + '2019-07-14 161206.txt'
        reason = ""

    elif 1014 <= cycleNumber <= 1022:
        fname = path + '2019-08-19 122750.txt'
        reason = ""

    elif 1024 <= cycleNumber <= 1059:
        fname = path + '2019-08-22 194934.txt'
        reason = ""

    elif cycleNumber == 1236:
        fname = path + '2020-02-24 141307.txt'
        reason = ""

    reason = ""
    print("File for cycle " + str(cycleNumber) + " is " + fname)
    print(reason)
    return fname, reason

####################

# TODO::finish and double check this
##total off numbers:
##cycle 85 never completed, error in rampup
##cycle

################################################################
