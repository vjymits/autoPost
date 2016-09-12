__author__ = 'sharvija'

from util import REST_METHODS, FREQUENCIES
from apscheduler.schedulers.background import BackgroundScheduler
from twitter import views, api
from twitter.util import InvalidValue
import models
from twitter import util
from scheduler import util as sch_util
import requests
import json
import ast

import logging
logging.basicConfig()
log = logging.getLogger(__name__)

default_sch= BackgroundScheduler()
default_sch.start()
class SchedulerApi:

    def createRestScheduler(self, data):
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
        log.info("all jobs: "+str(default_sch.get_jobs()))
        return {"jobId": str(uuid), "noOfJobs": all}

    def createActScheduler(self, data):
        required = ['uuid', 'name', 'frequency', 'every', 'action']
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
        action = data.get('action')
        req = data.get("requestBody", None)
        a= AutoPostAct(action, req)
        if frequency.lower() == FREQUENCIES[0][0]:
            job= default_sch.add_job(a.execute, trigger='interval', id = sch_id, hours=every, replace_existing=True)
        elif frequency.lower() == FREQUENCIES[1][0]:
            job= default_sch.add_job(a.execute, trigger='interval', id = sch_id, weeks=every,
                                     replace_existing=True)
        elif frequency.lower() == FREQUENCIES[2][0]:
            job= default_sch.add_job(a.execute, trigger='interval', id = sch_id, minutes=every,
                                     replace_existing=True)
        elif frequency.lower() == FREQUENCIES[3][0]:
            job= default_sch.add_job(a.execute, trigger='interval', id = sch_id, days=every,
                                     replace_existing=True)
        elif frequency.lower() == FREQUENCIES[4][0]:
            job= default_sch.add_job(a.execute, trigger='interval', id = sch_id, years=every,
                                     replace_existing=True)
        all = len(default_sch.get_jobs())
        log.info("all jobs: "+str(default_sch.get_jobs()))
        return {"jobId": str(uuid), "noOfJobs": all}

    def deleteScheduler(self, id):
        log.info("removing sch")
        j = default_sch.get_job(id)
        j.remove()
        log.info("all jobs: "+str(default_sch.get_jobs()))

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
            log.info("type after : "+str(type(self.requestBody)))
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
            log.info("URI: "+self.uri+" method: "+self.method)
            if self.method==REST_METHODS[0][0]:
                log.info("Method is GET")
                res=requests.get(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                #print str(res.status_code)
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[1][0]:
                log.info("Method is POST")
                res=requests.post(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[2][0]:
                log.info("Method is PUT")
                res=requests.put(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[3][0]:
                log.info("Method is DELETE")
                res=requests.delete(self.uri, data=self.requestBody, headers =self.headers)
                self.responseBody=res.json()
                self.responseCode=res.status_code

            elif self.method==REST_METHODS[4][0]:
                log.info("Method is HEAD")
                res=requests.head(self.uri)
                self.responseBody=res.json()
                self.responseCode=res.status_code
        except Exception as e:
            log.info("status code: "+str(res.status_code))
            log.info("An error occured "+str(e))

class AutoPostAct:
    def __init__(self, act, params):
        self.action= act
        self.inputData = params
    def execute(self):
        allowed_actions = ['tweet', 'follow', 'search']
        util.validate_allowed_params(allowed_actions, [self.action])
        d=ast.literal_eval(self.inputData)
        d['retain'] = int(d.get('retain',0))
        if self.action == 'tweet':
            api.TweetList().post(d)
        elif self.action == 'follow':
            api.AutoFollowApi().follow(d)
        elif self.action == 'search':
            api.Searching().post(d)
        else:
            raise util.InvalidValue(detail="Action is not allowed ", action=self.action)

def sch_startup():
    all = models.ActionScheduler.objects.all()
    sch_api=SchedulerApi()
    for one in all:
        sch_api.createActScheduler(one.toDict())
    start_trend_scheduler()

def start_trend_scheduler():
    trendFiller = api.TrendsApi()
    job= default_sch.add_job(trendFiller.fill_trends, trigger='interval', id = 'sch_trend_filler', minutes=5, replace_existing=True)
