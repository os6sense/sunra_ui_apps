
from nose.tools import *
from config import Config

def setup():
    pass

def teardown():
    pass

def test_config():
    config = Config('test/test.yml')
    assert config.studio_id == 99
    assert config.studio_name == "TEST_NAME"
    assert config.api_key == "aabbccdd"
    assert config.project_rest_api_url == "http://localhost:3000"
    assert config.recording_formats == "mp4, mp3"
    
