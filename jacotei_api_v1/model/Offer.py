#!/usr/bin/env python


class Offer:

    def __init__(self):
        self.swaggerTypes = {
            'available': 'bool',
            'barcode': 'str',
            'images': 'list[str]',
            'categories': 'list[str]',
            'isbn': 'str',
            'link': 'str',
            'prices': 'list[OfferPrice]',
            'sku': 'str',
            'title': 'str'
            
        }

        self.attributeMap = {
            'available': 'available',
            'barcode': 'barcode',
            'images': 'images',
            'categories': 'categories',
            'isbn': 'isbn',
            'link': 'link',
            'prices': 'prices',
            'sku': 'sku',
            'title': 'title'
            
        }

        
        #Produto disponÃ­vel
        
        self.available = None # bool
        
        #cÃ³digo de barras do produto da oferta
        
        self.barcode = None # str
        
        #Imagens dos produtos da oferta
        
        self.images = None # list[str]

        #Categorias dos produtos da oferta
        
        self.categories = None # list[str]
        
        #cÃ³digo de barras do livro
        
        self.isbn = None # str
        
        #link para a pÃ¡gina da oferta
        
        self.link = None # str
        
        #preÃ§os da oferta
        
        self.prices = None # list[OfferPrice]
        
        #CÃ³digo de identificaÃ§Ã£o da oferta
        
        self.sku = None # str
        
        #DescriÃ§Ã£o da oferta
        
        self.title = None # str
        
