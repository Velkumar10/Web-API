from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong'

@app.route('/startApi', methods=['GET'])
def startApi():
    sfcNo = request.args.get('sfc')  # Get the 'sfc' parameter from the query string
    if not sfcNo:  # Handle missing 'sfc' parameter
        return Response("<response><status>Failure</status><message>'sfc' parameter is missing.</message></response>", mimetype='application/xml')
    
    # Return the XML response
    xmlResponse = f'''<?xml version="1.0" encoding="UTF-8"?>
    <response>
        <status>Success</status>
        <message>{sfcNo} Started Successfully !!</message>
    </response>
    '''
    return Response(xmlResponse, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
