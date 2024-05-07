import logging

def setup_logging(is_logging_enabled):
    if is_logging_enabled:
        # Configure logging to write to a file, including the level and format of the logs
        logging.basicConfig(
            filename='app.log',  # Log output will go to app.log file
            filemode='a',  # Append to the log file if it exists, create it otherwise
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    else:
        # Disable all logging calls of severity 'CRITICAL' and below
        logging.disable(logging.CRITICAL)