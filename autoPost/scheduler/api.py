__author__ = 'sharvija'

from util import REST_METHODS, FREQUENCIES
from apscheduler.schedulers.background import BackgroundScheduler
from twitter.util import InvalidValue
import models
from twitter import util
from scheduler import util as sch_util
import requests
import json
import ast

import logging
log = logging.getLogger(__name__)

default_sch= BackgroundScheduler()
default_sch.start()
class RestSchedulerApi:

    def createScheduler(self, data):
        required = ['uuid', 'name', 'frequency', 'every', 'uri', 'method']
        util.validate_mandatory_params(required, data.keys())
        name=data.get('name', None)
        uuid=data.get('uuid', None)
        job= None
        frequency = data.get('frequency')
        every = data.get("every", 1)
        if name is None or uuid is None:
            raise InvalidValue(detail="Scheduler is not able to construct name")
        elif frequency not in sch_util.valid_frequencies:
            raise InvalidValue(detail="Assigned frequency is not valid", frequency=frequency)
        sch_id=str(uuid)
        r = RestCall(data.get('uri', None), method=data.get('method', None), requestBody=data.get(
            'requestBody'), headers=data.get('headers'))
        if frequency.lower() == FREQUENCIES[0][0]:
            job= default_sch.add_job(r.call, trigger='interval', id = sch_id, hours=every, replace_existing=True)
        elif frequency.lower() == FREQUENCIES[1][0]:
            job= default_sch.add_job(r.call, trigger='interval', id = sch_id, weeks=every,
                                     replace_existing=True)
        elif frequency.lower() == FREQUENCIES[2][0]:
            job= default_sch.add_job(r.call, trigger='interval', id = sch_id, minutes=every,
                                     replace_existing=True)
        elif frequency.lower() == FREQUENCIES[3][0]:
            job= default_sch.add_job(r.call, trigger='interval', id = sch_id, days=every,
                                     replace_existing=True)
        elif frequency.lower() == FREQUENCIES[4][0]:
            job= default_sch.add_job(r.call, trigger='interval', id = sch_id, years=every,
                                     replace_existing=True)
        all = len(default_sch.get_jobs())
        print("all jobs: "+str(default_sch.get_jobs()))
        return {"jobId": str(uuid), "noOfJobs": all}

    def deleteScheduler(self, id):
        print "removing sch"
        j = default_sch.get_job(id)
        j.remove()
        print("all jobs: "+str(default_sch.get_jobs()))

    def updateScheduler(self):
        pass

class RestCall:
    def __init__(self, uri, method=REST_METHODS[0][0], requestBody=None, headers=None):
        self.method=method
        self.uri=uri
        self.requestBody=None
        if requestBody:
            #print "data: "+str(requestBody)
            #d=ast.literal_eval(requestBody)
            #print ("type, d: "+str(type(d)))
            self.requestBody = json.dumps(ast.literal_eval(requestBody))
            #print "type after : "+str(type(self.requestBody))
        self.responseBody=None
        self.responseCode=200
        if headers:
           self.headers = headers
        else:
            self.headers= {'Content-type': 'application/json'}
    def getResponse(self):
        return self.responseBody
    def getResponseCode(self):
        return self.responseCode
    def call(self):
        try:
            res=None
            print "URI: "+self.uri+" method: "+self.method
            if self.method==REST_METHODS[0][0]:
                print("Method is GET")
                res=requests.get(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                print str(res.status_code)
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[1][0]:
                print("Method is POST")
                res=requests.post(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[2][0]:
                print("Method is PUT")
                res=requests.put(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[3][0]:
                print("Method is DELETE")
                res=requests.delete(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[4][0]:
                print("Method is HEAD")
                res=requests.head(self.uri)
                self.responseBody=res.json()
                self.responseCode=res.status_code
        except Exception as e:
            print "status code: "+str(res.status_code)
            print("An error occured "+str(e))

def sch_startup():
    all = models.RestScheduler.objects.all()
    sch_api=RestSchedulerApi()
    for one in all:
        sch_api.createScheduler(one.toDict())