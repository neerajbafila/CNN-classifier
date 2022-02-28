import os
import imghdr
from tkinter.tix import IMAGE
from PIL import Image
import shutil
from src.load_config import Load_config
from src.my_logger import My_logger
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
class Validate_raw_data:
    def __init__(self, config_path):
        self.ob_load_config = Load_config(config_path)
        self.config = self.ob_load_config.get_config()
        self.logger = My_logger()
    
    def validate_data(self):
        log_file = open("Logs/validate_raw_data.txt", "a+")
        self.logger.write_log(log_file, f"Validate_raw_data.validate_data started")
        self.data_folder = self.config['data_folder']
        self.image_folder = self.config['image_folder']
        self.Bad_data_folder = self.config['Bad_data_folder']
        bad_data_path = os.path.join(self.data_folder, self.Bad_data_folder)
        os.makedirs(bad_data_path, exist_ok=True)
        bad_data_path_dog = os.path.join(bad_data_path, "Dog")
        bad_data_path_cat = os.path.join(bad_data_path, "Cat")
        os.makedirs(bad_data_path_dog, exist_ok=True)
        os.makedirs(bad_data_path_cat, exist_ok=True)
        path = os.path.join(self.data_folder, self.image_folder)
        dirs = [i for i in os.listdir(path)]
        for d in dirs:
            path_dir = os.path.join(path, d)
            for fi in os.listdir(path_dir):
                full_path_of_img = os.path.join(path_dir, fi)
            
                try:
                    ImageFile.LOAD_TRUNCATED_IMAGES = True
                    with Image.open(full_path_of_img) as img:

                    # img = Image.open(full_path_of_img)
                        if img.verify():
                            if (len(img.getbands()) !=3) or (imghdr.what(full_path_of_img) not in ['jpeg', 'png']):
                                print(f"{full_path_of_img} is not a valid image")
                                self.logger.write_log(log_file, f"{full_path_of_img} is not a valid image")
                                try:
                                    if d == "Dog":
                                        shutil.move(full_path_of_img, bad_data_path_dog)
                                        print(f'{full_path_of_img} moved to {bad_data_path_dog}')
                                        self.logger.write_log(log_file, f'{full_path_of_img} moved to {bad_data_path_dog}')
                                    if d == "Cat":
                                        shutil.move(full_path_of_img, bad_data_path_cat)
                                        print(f'{full_path_of_img} moved to {bad_data_path_cat}')
                                        self.logger.write_log(log_file, f'{full_path_of_img} moved to {bad_data_path_cat}')
                                    
                                    continue
                        
                                except Exception as e:
                                    print(e)
                                    self.logger.write_log(log_file, f"exception occured {e}")
                            else:
                                pass

                        # else: 
                        #     shutil.move(full_path_of_img, bad_data_path)
                        #     print(f'{full_path_of_img} moved to {bad_data_path}')
                        #     self.logger(log_file, f'{full_path_of_img} moved to {bad_data_path}')
                except Exception as e:
                    shutil.move(full_path_of_img, bad_data_path + "/" + d)
                    print(f'{full_path_of_img} moved to {bad_data_path + "/" + d}')
                    self.logger.write_log(log_file, f'{full_path_of_img} moved to {bad_data_path + "/" + d}')
                    self.logger.write_log(log_file, f"exception occured {e}")
                    print(e)