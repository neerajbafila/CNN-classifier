import os
from datetime import datetime

class My_logger:
    def __init__(self):
        pass
    
    def write_log(self, log_file, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        log_file.write(f"{self.date}/{self.current_time}\t\t{log_message}\n")