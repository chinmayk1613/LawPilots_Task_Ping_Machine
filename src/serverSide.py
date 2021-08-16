try:
    import socket
    from datetime import datetime
    from uptime import uptime
    import time
    from flask import Flask, jsonify, request, render_template
    import json
    import sqlite3
except Exception as exe:
    print("Exception Occured {}".format(exe))
    # All header file declaration

machineStatus = Flask(__name__)
    # in above line flask application is created with name machineStatus


'''this is the route(API end point) declaration for status service in flask app.
 when request will created via HTTP request, this is the place where it lands to be process'''
@machineStatus.route('/status/')
def create_status(): # this function will be execute where request hit the flask application
    conn = sqlite3.connect('../lawPilotsDB_virtual.db') # connect to sqlite DB
    requestReceivedDateTime=datetime.now() # this will record the current time when the request is arrives
                                           # later to be stores in database to fetch for auditing purpose
    ck = conn.cursor()
    hostNmae=socket.gethostname()  # this line extract the hostname
    today = datetime.now() # this line print the current date and time
    uptime1=time.strftime('%H Hours, %M Minutes, %S Seconds', time.gmtime(uptime())) # this line prints the uptime
    ck.execute("insert into logData (request_received_on, machine_name, response_sent_on, uptime) values (?,?,?,?)"
               , (str(requestReceivedDateTime),str(hostNmae),str(today),str(uptime1)))
    # cursor.execute will insert the data that mention in values clause to the sqlite DB
    conn.commit()
    return json.dumps({"Machine_Name": str(hostNmae), "Date_And_Time": str(today), "Uptime": str(uptime1)})
    # above line send back the data to requestor by converting python object(dict) to JSON string

if __name__=='__main__':
    machineStatus.run(debug=True)
    ''' this is the place from where flask application gets initialized. here command is set to run flask app which
     is, in our case machineStatus with debuge mode ON. '''