import decimal
import json

from boto3.session import Session

# profile = '<YOUR_PROFILE_NAME>'
profile = 'shiraco'

session = Session(profile_name=profile)

# session = Session(aws_access_key_id='<YOUR ACCESS KEY ID>',
#                   aws_secret_access_key='<YOUR SECRET KEY>',
#                   region_name='<REGION NAME>')

event = {
    'operation': 'read',
    'tableName': 'hello-lambda-dynamodb',
    'payload': {'Key': {'id': 1}}
}

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError


print('Received event: ' + json.dumps(event, indent=2))

operation = event['operation']

if 'tableName' in event:
    dynamo = session.resource('dynamodb').Table(event['tableName'])

operations = {
    'create': lambda x: dynamo.put_item(**x),
    'read': lambda x: dynamo.get_item(**x),
    'update': lambda x: dynamo.update_item(**x),
    'delete': lambda x: dynamo.delete_item(**x),
    'list': lambda x: dynamo.scan(**x),
    'echo': lambda x: x,
    'ping': lambda x: 'pong'
}

if operation in operations:
    response = operations[operation](event.get('payload'))
    print('Response data: ' + json.dumps(response,
                                         indent=2, default=decimal_default))

else:
    raise ValueError('Unrecognized operation "{}"'.format(
        operation))  # response = dynamo.get_item(Key={"id": 2}
