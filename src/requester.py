try:
    import requests
    import time
except Exception as exe:
    print("Exception Occured {}".format(exe))
 # All header file declaration


SERVICE_ENDPOINT = 'http://localhost:5000/'
ROUTE_ENDPOINT = "{}status/".format(SERVICE_ENDPOINT)

'''above two lines define the service that needs to be called to get machine information
 so ROUTE_ENDPOINT will be http://localhost:5000/status/ '''


''' class will send the HTTP request using requests object to received response from targeted service '''
class pingMachine():
    def getResponse(self):
        for requestNumber in range(1,4): # for simulation I am sending request 3 times
            print("This is",requestNumber," request sent, and response is: \n")
            machineResponse = requests.get(ROUTE_ENDPOINT) # this line make single HTTP request to the API end point
            machineInfimation=machineResponse.json() # this will fetch the response in json format which of request that
                                                     # we sent
            # result display in suitable way from the json response that we received in above step
            print("Machine Name: ",machineInfimation['Machine_Name'])
            print("Current Date And Time: ", machineInfimation['Date_And_Time'])
            print("Uptime: ",machineInfimation['Uptime'])
            print("\n")
            time.sleep(5) # for simulation purpose next request will be triggered after 5 seconds.

'''calling of the methods that generate the request '''
PM=pingMachine()
PM.getResponse()