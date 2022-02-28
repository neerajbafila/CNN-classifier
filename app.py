from src.load_config import Load_config
from src.validate_raw_data import Validate_raw_data
from src.my_logger import My_logger
import os



ob = Validate_raw_data('config\config.yaml')
ob.validate_data()