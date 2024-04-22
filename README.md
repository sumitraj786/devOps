#dependencies
python should be installed in your computer

#how to run the script
1->create a file with .py extension
2->copy the code from log_analysis_script.py file 
3-> use any IDE for python like VScode, pycharm ,jupyter notebook,spyder etc
    or open terminal then direct to the file path and enter command "python filename.py".

after that you will getting output on console then enter while getting log messages on console "ctrl+c" for interruption or to get the log analysis report

here is the glimpse of output from the execution of script
2024-04-22 23:26:28,702 - DEBUG - DEBUG message
2024-04-22 23:26:29,703 - ERROR - ERROR message
2024-04-22 23:26:30,705 - INFO - INFO message
2024-04-22 23:26:31,707 - DEBUG - DEBUG message
2024-04-22 23:26:32,707 - DEBUG - DEBUG message
2024-04-22 23:26:33,708 - DEBUG - DEBUG message
2024-04-22 23:26:34,710 - INFO - INFO message
2024-04-22 23:26:35,711 - DEBUG - DEBUG message

Logging interrupted. Exiting.

Log Analysis Summary:
---------------------
---------------------
Total log entries: 8
DEBUG count: 5
INFO count: 2
ERROR count: 1

#added extra functionalities other than requirements
1-> Log File Rotation:-
Functionality: RotatingFileHandler from the logging.handlers module was used to implement log file rotation. Up to five backup log files are retained, and the log file rotates when it reaches a specific size (1MB in this example).
Benefits:
keeps the log file's size within reasonable bounds by stopping it from expanding endlessly.
saves earlier log entries in backup log files so that, in case historical analysis is required, it can be done.
helps preserve disc space by putting a cap on the log file's size.

2->Customized Logging Format:
Functionality: Using the Formatter object, customised the logging format to include log levels, log messages, and timestamps.
Benefits: Offers flexibility in customising the logging format to meet unique needs.
includes crucial data, like timestamps and log levels, to improve the legibility and clarity of log entries.
maintains a standard format, making it easier to parse and analyse log files.

