import boto3
import json



# Initialize the DynamoDB resource once
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
cloudresume_table = dynamodb.Table('cloud-resume')


def put_visitor_count(event, context, dynamoTable=cloudresume_table):
    # Define the update parameters
    update_params = {
        'TableName': 'cloud-resume',
        'Key': {
            'Id':  'Visitors'   
        },
        'UpdateExpression': 'ADD Visitors :inc',
        'ExpressionAttributeValues': {
            ':inc': 1
        },
        'ReturnValues': 'UPDATED_NEW' 
    }

    response = dynamoTable.update_item(**update_params)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # Allow all origins
            "Access-Control-Allow-Methods": "PUT, POST, GET, DELETE, OPTIONS",  # Allow specific methods
            "Access-Control-Allow-Headers": "Content-Type"  # Allow specific headers
        },
        "body": json.dumps({
            "visitor_count": str(response['Attributes']['Visitors']),
        }),
    }

def get_visitor_count(event, context, dynamoTable=cloudresume_table):
    # Retrieve the current visitor count
    response = dynamoTable.get_item(
        Key={
            'Id': 'Visitors'
        }
    )

    # Check if the item exists in the table
    if 'Item' in response:
        visitor_count = response['Item'].get('Visitors', 0)
        visitor_count = str(visitor_count)
    else:
        visitor_count = 0  # Default to 0 if item not found

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # Allow all origins
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT",  # Allow specific methods
            "Access-Control-Allow-Headers": "Content-Type"  # Allow specific headers
        },
        "body": json.dumps({
            "visitor_count": visitor_count,
        }),
    }
