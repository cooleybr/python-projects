import re
import string
import shopify
import urllib
import json
from datetime import datetime

def updateTracking():
    API_KEY = ''
    PASSWORD = ''
    WEBSTIE = ''
    shop_url = "https://%s:%s@.myshopify.com/admin" % (API_KEY, PASSWORD, WEBSITE)
    shopify.ShopifyResource.set_site(shop_url)
    shop = shopify.Shop.current()
    filein = open('tracking.txt', 'r')
    MHCOut = open('MHCTrack.txt', 'a')
    MDDOut = open('MDDTrack.txt', 'a')
    for line in filein:
        if (len(line) > 2):
            t = line.split(',')
            try:
                t[0] = t[0].replace('"','')
                print t[0]
                order = shopify.Order.find(name=t[0])
                ordernum = order[0].id
                new_fulfillment = shopify.Fulfillment({'order_id':ordernum,'tracking_number':t[1]})
                new_fulfillment.save()
            except:
                print 'Did not find order ' + t[0]
                pLog = open('pLog.txt','a')
                if 'MHC' in line:
                    MHCOut.write(line+'\n')
                if 'MDD' in line:
                    MDDOut.write(line+'\n')
                time = str(datetime.now())
                pLog.write(t[0] + ' ' + t[1] + ' ' + time + '\n')
                pLog.close()
    filein.close()
    MHCOut.close()
    MDDOut.close()
    fileout = open('tracking.txt','w')
    fileout.write('MME0000,1234567')
    fileout.close()
