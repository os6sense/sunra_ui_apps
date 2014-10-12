"""
File:: recording_proxy.py

Provides methods to access the Rails REST Api and provide the
json response.

"""
#import requests
#import json

#from sunra.presenters import TimePresenter, DatePresenter

#class BookingDetail(object):
    #"""
        #Simple container class for booking detail.
    #"""
    #def __init__(self, b_date, start_time, end_time, studio_id):
        #"""
        #Params::
            #b_date -- date of the booking
            #start_time -- start_time of the booking
            #end_time -- end time for the booking.
        #"""
        #self.facility_studio = studio_id
        #self.date = b_date
        #self.start_time = start_time
        #self.end_time = end_time

    #def to_json(self):
        #"""
        #return a json representation.
        #"""
        #return json.dumps(self, default=lambda o: o.__dict__,
                #sort_keys=True, indent=4)

    #def to_dict(self):
        #"""
        #return a dictionary representation.
        #"""
        #return {'facility_studio': self.facility_studio,
                #'date': self.date,
                #'start_time': self.start_time,
                #'end_time': self.end_time}


