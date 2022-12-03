#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def printall(cont):
    print ('Facility ID: ',cont.split('&lt;FacilityId&gt;')[1].split('&lt')[0])
    print ('Waterfront Port ID: ',cont.split('&lt;WaterfrontPortId&gt;')[1].split('&lt')[0])
    print ('Name: ', cont.split('&lt;Name&gt;')[1].split('&lt')[0])
    print ('Street: ',cont.split('&lt;FirstStreet&gt;')[1].split('&lt')[0])
    #print (str(response.content).split('&lt;SecondStreet&gt;')[1].split('&lt')[0])
    print ('City: ',cont.split('&lt;City&gt;')[1].split('&lt')[0])
    print ('State: ',cont.split('&lt;StateLookupName&gt;')[1].split('&lt')[0])
    print ('ZIP: ',cont.split('&lt;PostalCode&gt;')[1].split('&lt')[0])
    print ('Unit ID: ',cont.split('&lt;UnitId&gt;')[1].split('&lt')[0])
    print ('Port Name: ',cont.split('&lt;PortLookupName&gt;')[1].split('&lt')[0])
    print ('COPT ID: ',cont.split('&lt;CaptainOfThePortLookupId&gt;')[1].split('&lt')[0])
    print ('Captain of the Port: ',cont.split('&lt;CaptainOfThePortLookupName&gt;')[1].split('&lt')[0])
    print ('Phone: ',cont.split('&lt;PhoneNumber&gt;')[1].split('&lt')[0])
    print ('*********************************************')


# In[3]:


portsList = [95001509,91002101,91002283,100074975,91003901]


# In[4]:


for port in portsList:
    url="https://cgmix.uscg.mil/XML/MARPOLData.asmx"
    headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <MARPOLFacilityDetailsXMLStringGet xmlns="http://cgmix.uscg.mil/xml">
      <FacilityId>"""+str(port)+"""</FacilityId>
    </MARPOLFacilityDetailsXMLStringGet>
  </soap12:Body>
</soap12:Envelope>"""

    response = requests.post(url,data=body,headers=headers)
    printall(str(response.content))


# In[ ]:




