import re
import string
import shopify
import urllib
import json

def getOrders():
    #start connection
    API_KEY = ''
    PASSWORD = ''
    WEBSITE = ''
    shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, WEBSITE)
    shopify.ShopifyResource.set_site(shop_url)
    shop = shopify.Shop.current()#end connection
    prefix = ''
    #print (prefix)
    filein = open('lastnum.txt','r')
    for line in filein:
        starting = line.split(prefix)
        number = int(starting[1])
    filein.close()
    recorder = shopify.Order.find(status=open)
    recName = recorder[0].name
    recNum = recName.split(prefix)
    recVal = int(recNum[1])
    name = prefix + str(number)
    more = True
    misfire = 0
    while (number <= recVal):
      try:
        order = shopify.Order.find(name=name)
        ordernum = (order[0].id,'')[order[0].id==None]
        Order_ID = name
        oDate = oda = (order[0].created_at,'')[order[0].created_at==None]
        Email = (order[0].email,'')[order[0].email==None]
        Shipping_Method = (order[0].shipping_lines[0].code,'')[order[0].shipping_lines[0].code==None]
        Product_Total = (order[0].total_price_usd,'')[order[0].total_price_usd==None]
        Tax_Total = (order[0].total_tax,'')[order[0].total_tax==None]
        Shipping_Total = (order[0].shipping_lines[0].price,'')[order[0].shipping_lines[0].price==None]
        Shipping_Total = '0'
        Discount_Total = ''
        Order_Total = (order[0].total_price_usd,'')[order[0].total_price_usd==None]
        Payment_Type = ''
        cc_number_masked = ''
        processor_response = ''
        IP_Address = ''
        Shipping_First_Name = (order[0].shipping_address.first_name,'')[order[0].shipping_address.first_name==None]
        Shipping_Last_Name = (order[0].shipping_address.last_name,'')[order[0].shipping_address.last_name==None]
        Shipping_Company = (order[0].shipping_address.company,'')[order[0].shipping_address.company==None]
        Shipping_Company = Shipping_Company.replace(',','')
        Shipping_Address_1 = (order[0].shipping_address.address1,'')[order[0].shipping_address.address1==None]
        Shipping_Address_2 = (order[0].shipping_address.address2,'')[order[0].shipping_address.address2==None]
        Shipping_Address_3 = ''
        Shipping_Address_4 = ''
        Shipping_City = (order[0].shipping_address.city,'')[order[0].shipping_address.city==None]
        Shipping_State = (order[0].shipping_address.province_code,'')[order[0].shipping_address.province_code==None]
        Shipping_Postal_Code = (order[0].shipping_address.zip,'')[order[0].shipping_address.zip==None]
        Shipping_Country = (order[0].shipping_address.country_code,'')[order[0].shipping_address.country_code==None]
        Shipping_Phone = (order[0].shipping_address.phone,'')[order[0].shipping_address.phone==None]
        Customer_First_Name = (order[0].billing_address.first_name,'')[order[0].billing_address.first_name==None]
        Customer_Last_Name = (order[0].billing_address.last_name,'')[order[0].billing_address.last_name==None]
        Customer_Company = (order[0].billing_address.company,'')[order[0].billing_address.company==None]
        Customer_Company = Customer_Company.replace(',','')
        Customer_Address_1 = (order[0].billing_address.address1,'')[order[0].billing_address.address1==None]
        Customer_Address_2 = (order[0].billing_address.address2,'')[order[0].billing_address.address2==None]
        Customer_City = (order[0].billing_address.city,'')[order[0].billing_address.city==None]
        Customer_State = (order[0].billing_address.province_code,'')[order[0].billing_address.province_code==None]
        Customer_Postal_Code = (order[0].billing_address.zip,'')[order[0].billing_address.zip==None]
        Customer_Country = (order[0].billing_address.country_code,'')[order[0].billing_address.country_code==None]
        Customer_Phone = (order[0].billing_address.phone,'')[order[0].billing_address.phone==None]
        p1 = Order_ID + ',' + oDate + ',' + Email + ',' + Shipping_Method + ',' + Product_Total + ',' + Tax_Total + ',' + Shipping_Total + ',' + Discount_Total + ','
        p2 = Order_Total + ',' + Payment_Type + ',' + cc_number_masked + ',' + processor_response + ',' + IP_Address + ',' + Shipping_First_Name + ','
        p3 = Shipping_Last_Name + ',' + Shipping_Company + ',' + Shipping_Address_1 + ',' + Shipping_Address_2 + ',' + Shipping_Address_3 + ',' + Shipping_Address_4 + ','
        p4 = Shipping_City + ',' + Shipping_State + ',' + Shipping_Postal_Code + ',' + Shipping_Country + ','
        p5 = Shipping_Phone + ',' + Customer_First_Name + ',' + Customer_Last_Name + ',' + Customer_Company + ',' + Customer_Address_1 + ',' + Customer_Address_2 + ','
        p6 = Customer_City + ',' + Customer_State + ',' + Customer_Postal_Code + ',' + Customer_Country + ',' + Customer_Phone + '\n'
        pAll = p1 + p2 + p3 + p4 + p5 + p6
        f2 = open('order-export.csv','a')
        f2.write(pAll)
        f2.close()
        fileout = open('lastnum.txt','w')
        fileout.write(name)
        fileout.close()
        number += 1
        name = prefix + str(number)
      except:
        fLog = open('misf.txt','a')
        fLog.write(name)
        fLog.close()
        number += 1
        name = prefix + str(number)

#getOrders()
