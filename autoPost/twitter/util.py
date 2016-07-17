__author__ = 'sharvija'

import time
from django.apps import AppConfig
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
#from twitter import api

TWEET_STATES = (
        ('new', 'New'),
        ('updated', 'Updated'),
        ('failed', 'Failed'),
        ('updating', 'Updating')
    )

def get_current_time_integer():
    t = time.time()*1000
    return long(t)

class TwAppConfig(AppConfig):
    name = "twitter",
    verbose_name = "my app"
    def ready(self):
        print "runnn"
        return True
       #api.twitter_startup()

def validate_allowed_params(allowed_params_list, params_list):
    for param in params_list:
        if param not in allowed_params_list:
           raise InvalidParam(message="Invalid parameter found",
                                          invalid_param_name = param)

def validate_mandatory_params(mandatory_params, input_list):
    for param in mandatory_params:
        if param not in input_list:
            raise RequiredParamNotFound(required_parameter = param)

#util




#Exception

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class BaseException(APIException):
    detail = "Something went wrong"
    status_code = 500

    def __init__(self, **kwargs):
        if not kwargs:
            kwargs = {}
        self.detail={"msg":kwargs.pop('message', self.detail), "details":
            kwargs}
        self.status_code=kwargs.get('code', kwargs.pop('code',self.status_code))


class Invalid(BaseException):
    detail = "Invalid request"
    status_code = 400

class NotFound(BaseException):
    detail =  "Not found"
    status_code = 404

class ScripNotFound(NotFound):
    detail = "No such scrip found"

class InvalidParam(Invalid):
    detail = "Invalid parameter given"
    status_code = 400

class InvalidValueType(Invalid):
    detail = "Invalid value type detected"
    status_code = 400

class InvalidValue(Invalid):
    detail = "Invalid value given."

class RequiredParamNotFound(Invalid):
    detail = "Required parameter not found"
    status_code = 400

class TSBadRequest(BaseException):
    status_code = 400
    detail= "Bad Request."

class InternalError(BaseException):
    status_code = 500
    detail = "Internal server error occurs."

class TwitterError(InternalError):
    detail = "Error while accessing twitter api."

class TwitterSearchError(TwitterError):
    detail = "Error while searching on twitter."

class TwitterApiNotAccessible(TwitterError):
    detail = "Twitter api not accessible."

class TweetError(TwitterError):
    detail = "Error while posting tweet."

class TwitterRateLimitExceed(TwitterError):
    detail = "Reached maximum limit for now, please try after some time. "

class NoSuchHandlerFound(TwitterError):
    detail = "No such handler registered"

class NoSearchResultFound(TwitterError):
    detail = "No search result found, pls search again."