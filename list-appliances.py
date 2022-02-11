import requests
import json
import warnings
#from .modelsimport Device
#from .modelsimport Organisation
# from demonstrator.models import Device
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
######## Warning suppression ########
warnings.simplefilter('ignore',InsecureRequestWarning)
######## IP of system to which to send API requests #########
apiIP= '185.74.26.33'
######## EM7 user credentials########
apiUsername= 'api_access'
apiPassword= 'Clock?W1nd3r!'
######## Base url for api request ########
base_url= "https://%s/api/"% (apiIP)
org_id=182
#variable
url="%sappliance?limit=2000"% (base_url)
a=requests.get (url, auth = HTTPBasicAuth(apiUsername,apiPassword),verify=False)
jresults= json.loads(a.content)
dresults= json.loads(a.text)
jset=jresults['result_set']
textfile = open("appliances.txt", "w")
for x in jset:
    desc = x.get("description")

    url = "%s/device?filter.0.name.eq=%s"% (base_url,desc)
    devices=requests.get (url, auth = HTTPBasicAuth(apiUsername,apiPassword),verify=False)
    deviceresult = json.loads(devices.text)
    inddevice =deviceresult['result_set']
    if inddevice == []:
        print(desc, inddevice)
        textfile.write("appliance:%s  device result:%s\n"% (desc, inddevice))
    
textfile.close()



