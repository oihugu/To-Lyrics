import json
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions

class Watson():

    def __init__(self, key, url):    
        authenticator = IAMAuthenticator(key)
        self.service = NaturalLanguageUnderstandingV1(authenticator=authenticator,version='2018-03-16')
        self.service.set_service_url(url)
    
    def nlu_line(self, line):
        response = self.service.analyze(
            text=line,
            features=Features(entities=EntitiesOptions(),
                            keywords=KeywordsOptions(),
                            sentiment=SentimentOptions())).get_result()

        return json.dumps(response)