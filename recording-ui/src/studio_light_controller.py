
import serial

class StudioLightController(object):
    """
    An actual controller for the lighting connected to the arduino
    """
    def __init__(self):
        self._serial = serial.Serial('/dev/ttyACM0', 9600, bytesize=8, parity='N', stopbits=1, timeout=1)

    @staticmethod
    def connect():
        """
        Attempt to connect to the studio lights via the usb serial.
        
        Returns::
        True -- if a valid connection is possible
        False -- otherwise
        """
        try:
            serial.Serial('/dev/ttyACM0', 9600, bytesize=8, parity='N', stopbits=1, timeout=1)
            return True
        except:
            return False

    def on(self):
        """ Switch the lights on """
        try:
            self._serial.write('1')
        except:
            pass

    def off(self):
        """ Switch the lights off """
        try:
            self._serial.write('0')
        except:
            pass


