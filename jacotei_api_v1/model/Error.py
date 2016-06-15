#!/usr/bin/env python


class Error:

    def __init__(self):
        self.swaggerTypes = {
            'code': 'int',
            'message': 'str'
            
        }

        self.attributeMap = {
            'code': 'code',
            'message': 'message'
            
        }

        
        #Codigo do erro
        
        self.code = None # int
        
        #Mensagem de erro
        
        self.message = None # str
        
