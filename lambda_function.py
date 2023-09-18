import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
<<<<<<< HEAD
        'body': json.dumps('Hello from Lambda!!!, git changes 2nd time')
        'body': json.dumps('Hello from Lambda!!!, dev1 changes')
=======
        'body': json.dumps('Hello from Lambda!!!, master changes')
>>>>>>> 4e978ae (master changes)
    }
