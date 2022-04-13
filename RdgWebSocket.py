import json
import websocket
from websocket import create_connection

websocket.enableTrace(True)


class RdgWebSocket:

    def connect(self, ip_address):
        ws = create_connection('ws://' + ip_address + ':4101')
        return ws

    def register_listner(self, ws):
        register_listner_query = json.dumps({'COMMAND': 'REGISTER_LISTENER', 'PARAM': 'MOD_INFO'})
        ws.send(register_listner_query)
        print('Sent: {}'.format(register_listner_query))
        result = ws.recv()
        print('Result: {}'.format(result))

    def get_mod_info(self, ws):
        result = ws.recv()
        # deserializing the data
        data = json.loads(result)
        if (data['COMMAND'] == 'MOD_INFO'):
            print('Active Platform: ' + str(data['RECORD']['ActivePlatformIndex'] + 1))
            print('Date: ' + data['RECORD']['Date'])
            print(
                'Mass: ' + data['RECORD']['Mass'][0]['NetAct']['Value'] + ' ' + data['RECORD']['Mass'][0]['NetAct'][
                    'Unit'])
            print('Stability: ' + str(data['RECORD']['Mass'][0]['IsStab']))
            print('IsTared: ' + str(data['RECORD']['Mass'][0]['IsTare']))
            print('IsZeroed: ' + str(data['RECORD']['Mass'][0]['IsZero']))

    def change_platform(self, ws):
        query = json.dumps({'COMMAND': 'EXECUTE_ACTION', 'PARAM': 'ActionChangePlatform'})
        ws.send(query)
        ws.recv()

    def taring_scale(self, ws):
        query = json.dumps({'COMMAND': 'EXECUTE_ACTION', 'PARAM': 'ActionTarring'})
        ws.send(query)
        ws.recv()

    def zeroing_scale(self, ws):
        query = json.dumps({'COMMAND': 'EXECUTE_ACTION', 'PARAM': 'ActionZeroing'})
        ws.send(query)
        ws.recv()
