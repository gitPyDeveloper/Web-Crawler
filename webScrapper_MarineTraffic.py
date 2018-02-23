#######################################################################################
# Web Crawling - To get vessel location from marrine traffic website
#######################################################################################


import requests
import urllib2
from BeautifulSoup import BeautifulSoup



class MarineTracker():    
    
    def getLocation(self,IMO):
        
        #IMO = 9636395       
        
        url = "https://www.marinetraffic.com/en/ais/details/ships/imo:" + str(IMO)
        
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        
        
        req = urllib2.Request(url, headers=hdr)
        page = urllib2.urlopen(req)
        
        soup = BeautifulSoup(page)
        #print(soup.prettify())
        print soup.title.text
        
        tempString = None
        lat = None
        lng = None
                
        for eachTag in soup.findAll("a", attrs ={'class':"details_data_link"}):    
            tempString = str(eachTag.text)
            if '&deg;' in tempString:
                #print tempString
                break
            
        
        if tempString is not None:
            tempString = tempString.split('/')
            
            lat = tempString[0].replace('&deg;','').strip()
            lat = float(lat)
            
            lng = tempString[1].replace('&deg;','').strip()
            lng = float(lng)    
        
        
        print 'Latitude : ' , lat
        print 'Longitude : ' , lng
        
        return lat , lng
        
        
        
xObject = MarineTracker()
Latitude , Longitude = xObject.getLocation(9636395)            
        
