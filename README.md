# jacotei-api-sdk-python3

## Exemplos ##

Publicacao de 1000 ofertas

```Python 
#!/usr/bin/python3
	
import json

from jacotei_api_v1 import *
from jacotei_api_v1.api import *
from jacotei_api_v1.model import *
from jacotei_api_v1.client import ApiClient;

apiClient = client.ApiClient({	
                'client_id':'xxxxx',
				'access_token':'xxxx'},
				'https://webapisb.jacotei.com.br/publisher/v1')

offers_api = OffersApi.OffersApi(apiClient)
offer_request = OfferRequest.OfferRequest()
offer_request.offers = []

for i in range(0,  1000):
    offer = Offer.Offer()
    offer.sku = i
    offer.available = True;
    offer.title = 'Produto '+str(i)
    offer.link = 'http://aasdfaf.com/asdflasdf'
    offer.images = ['http://aasdfaf.com/asdflasdf.jpg']
    offer.categories = ['Categoria','Subcategoria','Sub subcategoria']
    price = OfferPrice.OfferPrice()
    price.price = 1.99
    price.installment = 1
    price.installment_value = 1.99
    offer.prices  = [price]
    offer_request.offers .append(offer)

try:
    offers_result = offers_api.update_offers_using_post(offers = offer_request)
    print (vars(offers_result))
except BaseException as e:
    print(e.msg)

```
