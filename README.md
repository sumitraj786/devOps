# Dependencies
- Python should be installed on your computer.

# How to Run the Script
1. Create a file with a `.py` extension.
2. Copy the code from `log_analysis_script.py` file.
3. Use any Python IDE such as VScode, PyCharm, Jupyter Notebook, Spyder, etc., or open a terminal and navigate to the file path. Then enter the command:
   ```bash
   python filename.py

**Here is the glimpse of output after the execution of the script:**

2024-04-22 23:26:28,702 - DEBUG - DEBUG message  
2024-04-22 23:26:29,703 - ERROR - ERROR message  
2024-04-22 23:26:30,705 - INFO - INFO message  
2024-04-22 23:26:31,707 - DEBUG - DEBUG message  
2024-04-22 23:26:32,707 - DEBUG - DEBUG message  
2024-04-22 23:26:33,708 - DEBUG - DEBUG message  
2024-04-22 23:26:34,710 - INFO - INFO message  
2024-04-22 23:26:35,711 - DEBUG - DEBUG message  

Logging interrupted. Exiting.

# Log Analysis Summary
---------------------
Total log entries: 8
DEBUG count: 5
INFO count: 2
ERROR count: 1

# Added Extra Functionalities
1. **Log File Rotation:**
   - **Functionality:** Implemented log file rotation using `RotatingFileHandler` from the `logging.handlers` module.
   - **Benefits:**
     - Keeps the log file's size within reasonable bounds by stopping it from expanding endlessly.
     - Saves earlier log entries in backup log files so that, in case historical analysis is required, it can be done.
     - Helps preserve disk space by putting a cap on the log file's size.

2. **Customized Logging Format:**
   - **Functionality:** Using the `Formatter` object, customized the logging format to include log levels, log messages, and         timestamps.
   - **Benefits:**
     - Offers flexibility in customizing the logging format to meet unique needs.
     - Includes crucial data, like timestamps and log levels, to improve the legibility and clarity of log entries.
     - Maintains a standard format, making it easier to parse and analyze log files.
