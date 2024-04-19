import http.client

def loadAllGenerators(token):
    cxn = http.client.HTTPSConnection("generator.campaign-logger.com")
    cxn.request("GET", "/api2/generators", headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
        })
    response = cxn.getresponse()

    print(response.status, response.reason)
    print(response.read().decode('utf-8'))

loadAllGenerators("your_token_here")
