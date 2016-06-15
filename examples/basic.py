import json

from jacotei_api_v1 import client

apiClient = client.ApiClient({  
                'client_id':'xxxxx',
                'access_token':'xxxx'},
                'https://webapisb.jacotei.com.br/publisher/v1')

offers_api = client.OffersApi.OffersApi(apiClient)
offer_request = client.OfferRequest.OfferRequest()
offer_request.offers = []

for i in range(0,  1000):
    offer = client.Offer.Offer()
    offer.sku = i
    offer.available = True;
    offer.title = 'Produto '+str(i)
    offer.link = 'http://aasdfaf.com/asdflasdf'
    offer.images = ['http://aasdfaf.com/asdflasdf.jpg']
    price = client.OfferPrice.OfferPrice()
    price.price = 1.99
    price.installment = 1
    price.installment_value = 1.99
    offer.prices  = [price]
    offer_request.offers.append(offer)

try:
    offers_result = offers_api.update_offers_using_post(offers = offer_request)
    print (vars(offers_result))
except BaseException as e:
    print(e.msg)
