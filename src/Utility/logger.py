import logging


##import config


# The different levels of logging, from highest urgency to lowest urgency, are:
#     CRITICAL                  logger.critical('')          critical message
#     ERROR                     logger.error('')            error message
#     WARNING                   logger.warning('')           warning message
#     INFO                      logger.info('')             informative message
#     DEBUG                     logger.debug('')             low-level debug message
#

# setLevel() call sets the minimum log level of messages it actually logs


# Task you want to perform 	The best tool for the task
# Display console output for ordinary usage of a command line script or program 	print()
# Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation) 	logging.info() (or logging.debug() for very detailed output for diagnostic purposes)
# Issue a warning regarding a particular runtime event
#
# warnings.warn() in library code if the issue is avoidable and the client application should be modified to eliminate the warning
#
# logging.warning() if there is nothing the client application can do about the situation, but the event should still be noted
# Report an error regarding a particular runtime event 	Raise an exception
# Report suppression of an error without raising an exception (e.g. error handler in a long-running server process) 	logging.error(), logging.exception() or logging.critical() as appropriate for the specific error and application domain
#


# Level 	When it’s used
# DEBUG 	Detailed information, typically of interest only when diagnosing problems.
# INFO 	Confirmation that things are working as expected.
# WARNING 	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR 	Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL 	A serious error, indicating that the program itself may be unable to continue running.


# To log messages to a file AND printed to the screen, copy and paste the following:

def logger_setup():
    # logger = logging.getLogger()

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # todo : logger timestamp filename
    fh = logging.FileHandler('log_.txt')  # file handler
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()  # console handler
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info('logger_setup() successfully called')


#################################################################################################

# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')


def do_something():
    logging.info('Doing_something()')
    import time
    # print(time.clock())
