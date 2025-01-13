from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong'

@app.route('/XMII/Runner', methods=['GET'])
def startApi():
    transaction = request.args.get('Transaction')  # Get the 'sfc' parameter from the query string
    if 'MultipleStartSFCAPI' in transaction:
        inputJson = request.args.get('InputJSON')
        operation = request.args.get('Operation')
        username = request.args.get('Username')
        outputParameter = request.args.get('Output')
        contentType = request.args.get('content-type')
    elif 'assembleComponentTrx' in transaction:
        sfc = request.args.get('SFC')
        component = request.args.get('Component')
        assyDataType = request.args.get('Assy_DataType')
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
    app.run(debug=True,port=7001)
