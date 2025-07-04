import boto3
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):
    # Parsear el body JSON que viene como string
    body = json.loads(event['body'])  # ✅ esto convierte el string en un dict
    cliente_id = body['cliente_id']   # ✅ ahora puedes acceder al campo

    # Consultar en DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tf_clientes')

    response = table.query(
        KeyConditionExpression=Key('cliente_id').eq(cliente_id)
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
