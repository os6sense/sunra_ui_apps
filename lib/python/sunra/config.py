# File:: sunra_config.py
# Loads the sunra global config

import yaml

class Global:
    """
    Simple config wrapper to parse the sunra config file
    """
    def __init__(self, fn='/etc/sunra/config.yml'):
        conf_file = open(fn)
        config = yaml.safe_load(conf_file)

        self.studio_id = config['studio_id']
        self.api_key = config['api_key']
        self.studio_name = config['studio_name']
        self.recording_formats = config['recording_formats']
        self.project_rest_api_url = config['project_rest_api_url']
        self.recording_service_rest_api_url = config['recording_service_rest_api_url']
        self.ui_hash = config['ui_hash']

        conf_file.close()

class Uploader(object):
    """
    Simple config wrapper to parse the sunra config file
    """
    def __init__(self, fn='/etc/sunra/uploader.yml'):
        conf_file = open(fn)
        config = yaml.safe_load(conf_file)

        self.uploader_service_url = config['uploader_service_url']
        self.archive_server_address = config['archive_server_address']
        self.archive_server_port = config['archive_server_port']
        self.sftp_ssl_key = config['sftp_ssl_key']
        self.sftp_username = config['sftp_username']
        self.sftp_password = config['sftp_password']
        self.archive_base_directory = config['archive_base_directory']
        self.start_time = config['start_time']
