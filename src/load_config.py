import os
import yaml

class Load_config:
    def __init__(self, config_path):
        self.config = config_path
    
    def get_config(self):
        print(self.config)
        # data_folder = config['data_folder']
        # image_folder = config['image_folder']
        # path = os.path.join(data_folder, image_folder)
        # print(f"yaml path is{path}")
        with open(self.config, 'r') as yamlFile:
            config = yaml.load(yamlFile, Loader=yaml.SafeLoader)
        return config