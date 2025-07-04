import boto3
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):
    body = event["body"]
    if isinstance(body, str):
        body = json.loads(body)

    curso_id = body["cliente_id"]

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("tf_cliente")

    response = table.query(
        KeyConditionExpression=Key("cliente_id").eq(curso_id)
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"])
    }
