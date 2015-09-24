import sys
import json
import urllib2

if __name__=='__main__':
    # mykey=bf2e26d8-4233-43e8-b9a6-378b4b2a8b59
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    SD = data['Siri']['ServiceDelivery']
    VMD = SD['VehicleMonitoringDelivery']
    VA = VMD[0]['VehicleActivity']
    
    busline = sys.argv[2]
    #busline
    print 'Bus Line : ',busline
    #number of buses
    print 'Number of Active Buses : ',len(VA)
    
    a = -1
    for s in VA:
        a += 1
        stationLat  = s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        stationLon  = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        
        print 'Bus %s is at latitude %s and longitude %s' % (a,stationLat,stationLon)
    
    
    
    
    
    
    
    