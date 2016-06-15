#!/usr/bin/env python


class OfferRejected:

    def __init__(self):
        self.swaggerTypes = {
            'offer': 'Offer',
            'validation_errors': 'list[Error]'
            
        }

        self.attributeMap = {
            'offer': 'offer',
            'validation_errors': 'validationErrors'
            
        }

        
        
        self.offer = None # Offer
        
        
        self.validation_errors = None # list[Error]
        
