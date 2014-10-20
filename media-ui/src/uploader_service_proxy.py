import requests

class UploaderServiceProxy(object):
    """
    A minimal proxy interface to the uploader service
    """
    JSON_HEADER = {'content-type': 'application/json'}

    def __init__(self, config):
        self.service_url = config.uploader_service_url

    def status(self):
        """
        """

        return requests.get(self.service_url + 'status').json()

    def manual_start(self):
        """
        """
        return requests.get(self.service_url + 'manual_start').json()

    def stop(self):
      pass

