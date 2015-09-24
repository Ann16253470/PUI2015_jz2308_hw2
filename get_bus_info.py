import csv
import json
import sys
import urllib2

if __name__=='__main__':
    # mykey=bf2e26d8-4233-43e8-b9a6-378b4b2a8b59
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    SD = data['Siri']['ServiceDelivery']
    VMD = SD['VehicleMonitoringDelivery']
    VA = VMD[0]['VehicleActivity']
    
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude','Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        
        for s in VA:
            Latitude  = s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Longitude  = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if s['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StopName = 'N/A'
                StopStatus = 'N/A'
            else:
                StopName = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                StopStatus = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            writer.writerow([Latitude,Longitude,StopName,StopStatus])
                     