from dateutil.parser import parse

# LJ 05/05/15 - added in, seems it was missing causing QTimePresenter to fail.
from datetime import datetime

from PyQt4.QtCore import QTime

class DatePresenter(str):
    """
    Given a string that contains date/time information, attempt
    to parse it and return formated as %d/%m/%YY.
    """
    def __new__(cls, dt_str):
        try:
            if not hasattr(dt_str, 'read'): # parse operates on a string
                dt_str = str(dt_str)
            return str.__new__(cls, parse(dt_str).strftime("%d/%m/%Y"))
        except Exception, e:
            print e
            return str.__new__(cls, "??/??/???? ")

class TimePresenter(str):
    """
    Given a string that contains date/time information, attempt
    to parse it and return formated as %H:%M %p.
    """
    def __new__(cls, dt_str, inc_meridian=True):
        try:
            if not hasattr(dt_str, 'read'): # parse operates on a string
                dt_str = str(dt_str)

            if inc_meridian:
                return str.__new__(cls, parse(dt_str).strftime("%H:%M %p"))

            return str.__new__(cls, parse(dt_str).strftime("%H:%M"))
        except Exception:
            return str.__new__(cls, "--:-- ")

class TimerPresenter(str):
    """
    Given a string that contains date/time information, attempt
    to parse it and return formated as %H:%M:%S %p.
    """
    def __new__(cls, dt_str):
        try:
            if not hasattr(dt_str, 'read'): # parse operates on a string
                dt_str = str(dt_str)
            return str.__new__(cls, parse(dt_str).strftime("%H:%M:%S %p"))
        except Exception:
            return str.__new__(cls, "--:--:--")

class QTimePresenter(QTime):
    """
    Attempts to create a new QTime object given either a datetime, or string.
    """
    def __new__(cls, value):
        """
        Helper. Takes a date like value and attempts to convert
        it to a simple QTime type.
        """
        if isinstance(value, QTime):
            return value
        if isinstance(value, datetime):
            return QTime.__new__(value.hour, value.minute)
        if isinstance(value, unicode):
            return QTime.__new__(parse(value).hour, parse(value).minute)
        if isinstance(value, str):
            return QTime.__new__(parse(value).hour, parse(value).minute)

