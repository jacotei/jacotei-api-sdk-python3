#!/usr/bin/env python


class OfferPrice:

    def __init__(self):
        self.swaggerTypes = {
            'installment': 'int',
            'installment_value': 'float',
            'price': 'float',
            'type': 'str'
            
        }

        self.attributeMap = {
            'installment': 'installment',
            'installment_value': 'installmentValue',
            'price': 'price',
            'type': 'type'
            
        }

        
        #Quantidade de parcelas
        
        self.installment = None # int
        
        #valor de cada parcela
        
        self.installment_value = None # float
        
        #preÃ§o total do produto
        
        self.price = None # float
        
        #Forma de pagamento
        
        self.type = None # str
        
