# configure log format
import logging
"""
set up a logger for the healthcare application. The logger will write logs to a file named 'healthcare.log' and also output logs to the console.
"""

def setup_logger(log_file='healthcare.log'):
    """Get a logger with the specified name."""
    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)
    """Check if the logger already has handlers to avoid adding multiple handlers."""

    if logger.hasHandlers():
        return logger
    """
    Create a file handler to write logs to the configured log file and set the log level to DEBUG.
    """
    file_handler = logging.FileHandler(log_file)
    logger.setLevel(logging.DEBUG)
 
    """
    create formatter to specify the log format and date format. The log format includes the timestamp, logger name, log level, and message.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to file_handler
    file_handler.setFormatter(formatter)
    # add file_handler to logger
    logger.addHandler(file_handler)
    return logger
