from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong'

@app.route('/XMII/Runner', methods=['GET'])
def startApi():
    transaction = request.args.get('Transaction')
    outputParameter = request.args.get('Output')
    contentType = request.args.get('content-type')
    if 'MultipleStartSFCAPI' in transaction:
        inputJson = request.args.get('InputJSON')
        inputJson = json.loads(inputJson)
        operation = request.args.get('Operation')
        username = request.args.get('Username')
        xmlResponse = f'''<?xml version="1.0" encoding="UTF-8"?><Rowsets DateCreated="2024-11-12T14:48:45" EndDate="2023-10-09T19:03:28" StartDate="2023-10-09T19:03:28" Version="15.5 SP0 Patch 39 (Jun 24, 2024)">
                            <Rowset>
                                <Columns>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="Status" SQLDataType="1" SourceColumn="Status"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="Code" SQLDataType="1" SourceColumn="Code"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="Log" SQLDataType="1" SourceColumn="Log"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="SFC" SQLDataType="1" SourceColumn="SFC"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="SHOP_ORDER" SQLDataType="1" SourceColumn="SHOP_ORDER"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="OPERATION" SQLDataType="1" SourceColumn="OPERATION"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="STATUS_DESCRIPTION" SQLDataType="1" SourceColumn="STATUS_DESCRIPTION"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="MATERIAL_DESCRIPTION" SQLDataType="1" SourceColumn="MATERIAL_DESCRIPTION"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="QTY" SQLDataType="1" SourceColumn="QTY"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="ITEM" SQLDataType="1" SourceColumn="ITEM"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="SITE" SQLDataType="1" SourceColumn="SITE"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="SFCBO" SQLDataType="1" SourceColumn="SFCBO"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="SHOP_ORDER_BO" SQLDataType="1" SourceColumn="SHOP_ORDER_BO"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="INSPECTION_LOT" SQLDataType="1" SourceColumn="INSPECTION_LOT"/>
                                    <Column Description="" MaxRange="1" MinRange="0" Name="OPERATIONBO" SQLDataType="1" SourceColumn="OPERATIONBO"/>
                                </Columns>
                                <Row>
                                    <Status>1</Status>
                                    <Code>Success</Code>
                                    <Log>The Selected SFCs Started at the Operation {operation} Successfully</Log>
                                    <SFC>{inputJson[0]['SFC']}</SFC>
                                    <SHOP_ORDER>Dummy</SHOP_ORDER>
                                    <OPERATION>{operation}</OPERATION>
                                    <STATUS_DESCRIPTION>Active</STATUS_DESCRIPTION>
                                    <MATERIAL_DESCRIPTION>DUMMY</MATERIAL_DESCRIPTION>
                                    <QTY>1</QTY>
                                    <ITEM>Dummy/1</ITEM>
                                    <SITE>Dummy</SITE>
                                    <SFCBO/>
                                    <SHOP_ORDER_BO/>
                                    <INSPECTION_LOT/>
                                    <OPERATIONBO/>
                                </Row>
                            </Rowset>
                        </Rowsets>'''
    elif 'assembleComponentTrx' in transaction:
        sfc = request.args.get('SFC')
        component = request.args.get('Component')
        assyDataType = request.args.get('Assy_DataType')
        batchNoValue = request.args.get('BatchNoValue')
        xmlResponse = f'''Component {component} has been successfully assembled for the {assyDataType} {sfc} on the operation '''
    elif 'MultipleCompleteSFC' in transaction:
        inputJson = request.args.get('InputJSON')
        operation = request.args.get('operation')
        xmlResponse = f'''<?xml version="1.0" encoding="UTF-8"?><Rowsets DateCreated="2024-11-12T14:49:21" EndDate="2023-11-29T19:27:06" StartDate="2023-11-29T19:27:06" Version="15.5 SP0 Patch 39 (Jun 24, 2024)">
                        <Rowset>
                            <Columns>
                                <Column Description="" MaxRange="1" MinRange="0" Name="Status" SQLDataType="1" SourceColumn="Status"/>
                                <Column Description="" MaxRange="1" MinRange="0" Name="Code" SQLDataType="1" SourceColumn="Code"/>
                                <Column Description="" MaxRange="1" MinRange="0" Name="Log" SQLDataType="1" SourceColumn="Log"/>
                            </Columns>
                            <Row>
                                <Status>1</Status>
                                <Code>Success</Code>
                                <Log>The selected SFC's is completely done</Log>
                            </Row>
                        </Rowset>
                    </Rowsets>
                    '''
    
    return Response(xmlResponse, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True,port=7001)
