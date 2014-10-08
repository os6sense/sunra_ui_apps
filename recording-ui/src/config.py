# File:: Config.py 
# Loads the global config

import yaml

class Config:
    def __init__(self, fn='/etc/sunra/config.yml'):
        f = open(fn)
        config = yaml.safe_load(f)

        self.studio_id = config['studio_id']
        self.api_key = config['api_key']
        self.studio_name = config['studio_name']
        self.recording_formats = config['recording_formats']
        self.project_rest_api_url = config['project_rest_api_url']
        self.recording_service_rest_api_url = config['recording_service_rest_api_url']

        f.close()
