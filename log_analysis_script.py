#importing the required libraries
import logging
import logging.handlers
import time
import random
import signal
import sys

# implemented the mechanism to stop the monitoring loop by using ctrl+c button from keyboard
def signal_handler(signal, frame):
    print("\nLogging interrupted. Exiting.")
    analyze_log(log_data)
    sys.exit(0)

# here is the function for log analysis like counting the number of different types of log messages
def analyze_log(log_data):
    # First Counting the  occurrences of each log level like for debug , info and error
    debug_count = sum(1 for message in log_data if 'DEBUG' in message)
    info_count = sum(1 for message in log_data if 'INFO' in message)
    error_count = sum(1 for message in log_data if 'ERROR' in message)

    # now generating sumamry report for the counted messages with total number of log entries included
    print()
    print("Log Analysis Summary:")
    print("---------------------")
    print("---------------------")
    print(f"Total log entries: {len(log_data)}")
    print(f"DEBUG count: {debug_count}")
    print(f"INFO count: {info_count}")
    print(f"ERROR count: {error_count}")
    # here adding this  stdout to ensure immediate output (not required) but for good practice
    sys.stdout.flush()

# logging setup
#implementation of additional fucntionality of "log file rotation" feature which has been described completely in the README file 
#one more functionality "customized logging format" has been implemented which has allso been described inside the README file
log_file = 'app.log'
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') #for providing timestamp with each log message 
file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5) #log file rotation
file_handler.setFormatter(log_formatter)
console_handler = logging.StreamHandler(sys.stdout) #handling  streams using stream handler
# Set the log formatter for the console handler
console_handler.setFormatter(log_formatter)
# Get the root logger instance
root_logger = logging.getLogger()
# Add the file handler to the root logger
root_logger.addHandler(file_handler)
# Add the console handler to the root logger
root_logger.addHandler(console_handler)
# Set the logging level for the root logger to DEBUG
root_logger.setLevel(logging.DEBUG)
# defineng log levels to cycle through
log_levels = [logging.DEBUG, logging.INFO, logging.ERROR]
# setting up the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)

# createing List to store log data
log_data = []

# main loop to log messages
#using try except to handle the interruption from ctrl+c
try:
    while True:
        # first randomly select a log level
        log_level = random.choice(log_levels)
        # now get the log message format for the selected log level
        if log_level == logging.DEBUG:
            log_message = "DEBUG message"
        elif log_level == logging.INFO:
            log_message = "INFO message"
        else:
            log_message = "ERROR message"
        # log the message
        root_logger.log(log_level, log_message)
        # append log message to log data
        log_data.append(log_message)
        # flush stdout to ensure immediate output
        sys.stdout.flush()
        # sleep for a short interval
        time.sleep(1)

except KeyboardInterrupt:
    # here handling the  keyboard interrupt of (Ctrl+C)
    #printing a specific message after interruptin in order to detect the exiting from logging loop
    print("\nLogging interrupted")
    analyze_log(log_data)
