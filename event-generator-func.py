# Event generator function
def api_event_generator(funct_base_url,funct_apiUsername,funct_apiPassword,api_event_message,api_event_deviceid):
    data = json.dumps({
    "message": api_event_message,
    "message_time":"0",
    "aligned_resource":"/api/device/"+api_event_deviceid
})
r = requests.post(funct_base_url+"alert", data, auth = HTTPBasicAuth(funct_apiUsername,funct_apiPassword),verify=False)