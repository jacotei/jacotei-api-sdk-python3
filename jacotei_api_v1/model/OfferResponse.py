#!/usr/bin/env python


class OfferResponse:

    def __init__(self):
        self.swaggerTypes = {
            'accepted_offers_count': 'int',
            'total_offers_count': 'int',
            'offers_rejected': 'list[OfferRejected]'
            
        }

        self.attributeMap = {
            'accepted_offers_count': 'acceptedOffersCount',
            'total_offers_count': 'totalOffersCount',
            'offers_rejected': 'offersRejected'
            
        }

        
        #quantidade de ofertas aceitas
        
        self.accepted_offers_count = None # int
        
        #quantidade total de ofertas enviadas
        
        self.total_offers_count = None # int
        
        #lista de ofertas rejeitadas
        
        self.offers_rejected = None # list[OfferRejected]
        
