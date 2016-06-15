#!/usr/bin/env python

import sys
import os

from ..model import *


class OffersApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def update_offers_using_post(self, **kwargs):
        """MÃ©todo de atualizaÃ§Ã£o de ofertas
        

        Args:
            offers, OfferRequest: offerUpdateRequest (required)
            

        Returns: OfferResponse
        """

        allParams = ['offers']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update_offers_using_post" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/offers'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        

        

        

        postData = params['offers']

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'OfferResponse')
        return responseObject
        
        
        
    
    def get_offer_using_get(self, **kwargs):
        """Consulta de ofertas por sku
        

        Args:
            sku, str: sku (required)
            

        Returns: Offer
        """

        allParams = ['sku']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_offer_using_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/offers/{sku}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        

        
        if ('sku' in params):
            replacement = str(self.apiClient.toPathValue(params['sku']))
            resourcePath = resourcePath.replace('{' + 'sku' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Offer')
        return responseObject
        
        
        
    


