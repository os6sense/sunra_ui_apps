import requests
import json

class RecordingServiceProxy(object):
    """
    Calls the recording service via its rest api. The URL for the
    recording service is set in the config file.

    Start and Stop are obvious but it important to note that a booking
    MUST be scheduled for the studio at the date and time when the
    call to start is made.
    """
    def __init__(self, config):
        self.api_key = config.api_key
        self.recording_service_url = config.recording_service_rest_api_url

    def get(self, action):
        """ simple get method to dry up params """
        url = "%s/%s/" % (self.recording_service_url, action)

        params = {'api_key': self.api_key}
        return requests.get(url, params=params).json()

    def start(self):
        """
        It takes your dog for a walk. What do you think it does?!

        Returns::
        The status after the recording service rest api has received a
        start command.
        """
        return self.get("start")

    def stop(self):
        """
        Really?

        Returns::
        The status after the recording service rest api has received a
        stop command.
        """
        return self.get("stop")

    def status(self):
        """
        Returns the current status of the recording service.
        """
        return self.get("status")
