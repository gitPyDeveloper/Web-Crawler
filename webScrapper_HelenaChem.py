#######################################################################################
# Web Crawling - To get office locations within a state, using BeautifulSoup
#######################################################################################

import requests
from BeautifulSoup import BeautifulSoup

#######################################################################################
# The program finds the locations of each branch of helena chemical
# Input - stateCode
# Output - List of locations
#######################################################################################
class HelenaChemical():
    
    def getLocations(self,stateCode):

        #stateCode = "CA"
        
        link = "http://www.helenachemical.com/locations/?zip=&city=&state=" + str(stateCode)
        rawData = requests.get(link)
        data = rawData.text
        
        soup = BeautifulSoup(data)
        #print(soup.prettify())
        
        counter = 0
        tempString = ""
        locationList = []
        
        print stateCode
        print '-------------------------------'
        
        for eachTag in soup.findAll("span", attrs ={'class':["add-1","add-3"]}):
            
            counter += 1
            tempString = tempString  + eachTag.text + ","
            
            if counter == 2:
                tempString = tempString[:-1]
                locationList.append(tempString)
                tempString = ""
                counter = 0
                
            

        return locationList




xObject = HelenaChemical()
locationList = xObject.getLocations("CA")
print locationList

#######################################################################################
# Get latitude and longitude of each address, using google map api
#######################################################################################
for name in locationList:
    resp_json_payload = None
    name = name[:-5].strip()
    name = name.replace(' ','+')
    tempURL = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + name
    print tempURL
    response = requests.get(tempURL)
    
    resp_json_payload = response.json()
    
    try:
        print(resp_json_payload['results'][0]['geometry']['location'])
    except:
        continue

