import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!!!, git changes 2nd time')
        'body': json.dumps('Hello from Lambda!!!, dev1 changes')
    }
