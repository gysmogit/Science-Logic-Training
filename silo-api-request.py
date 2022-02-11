
import requests
import json
import warnings
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
class api_request:
    def apilocation(ip):
        api_ip = ip
        api_base_url = "https://%s/api/"% (api_ip)
        return(api_base_url)
    def credentials():
        credentials = {'api_username' : 'api_access' , 'api_password' : 'Clock?W1nd3r!'}
        return(credentials)
    def url_builder(type, filter):
        app_type = type
        app_filter = filter
        if filter !='':
            app_filter = "&filter.0.name.eq=%s"% (filter)
        else:
            app_filter = ''     
        org_id=182
        limit=2000
        base_url = api_request.apilocation('185.74.26.33')
        url="%s%s?limit=%s%s"% (base_url,app_type,limit,app_filter)
        return(url)
    def data_request(type, filter):
        app_filter = filter
        api_type = type
        warnings.simplefilter('ignore',InsecureRequestWarning)
        a=requests.get(api_request.url_builder(api_type, app_filter), auth = HTTPBasicAuth(api_request.credentials()["api_username"],api_request.credentials()["api_password"]),verify=False)
        return(a)
appliances = api_request.data_request('appliance','')    
print(appliances)
jresults= json.loads(appliances.content)
#dresults= json.loads(appliances)
jset=jresults['result_set']
count =0
for result in jset:   
    devices = api_request.data_request('device',result['description'])
    dresults = json.loads(devices.content)
    dset=dresults['result_set']
    if dset['name'] != "":
        count = count +1
    else:    
        print(result['description'])

        
    
