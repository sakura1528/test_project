'''
@author:lsd
@time:15.08.2023 10:16
'''
import logging
import time
import os


class RotatingLogger:
    def __init__(self, log_directory):
        self.log_directory = log_directory
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        self._rotate_logs()
        self.current_log_file = self._create_log_file()

        file_handler = logging.FileHandler(self.current_log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def _rotate_logs(self):
        existing_logs = [f for f in os.listdir(self.log_directory) if f.endswith('.log')]
        if len(existing_logs) >= 4:
            existing_logs.sort()
            os.remove(os.path.join(self.log_directory, existing_logs[0]))

    def _create_log_file(self):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.log_directory, f"log_{timestamp}.log")

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    log_dir = "logs"
    logger = RotatingLogger(log_dir)

    logger.log_info("This is an informational message.")
    logger.log_warning("This is a warning message.")
    logger.log_error("This is an error message.")
    logger.log_critical("This is a critical message.")
