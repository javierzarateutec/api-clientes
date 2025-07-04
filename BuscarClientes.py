import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (cliente_id esperado en body como JSON string)
    cliente_id = event['body']['cliente_id']
    
    # Inicializa DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tf_clientes')  # Usa el nombre correcto de tu tabla

    # Query por la clave de partición (cliente_id)
    response = table.query(
        KeyConditionExpression=Key('cliente_id').eq(cliente_id)
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'body': items
    }
