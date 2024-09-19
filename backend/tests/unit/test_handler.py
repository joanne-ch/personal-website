import json
import pytest
import boto3
from botocore.stub import Stubber
from backend import app
import moto
import os

@pytest.fixture()
def cloudresume_table():
    """Connects to local DynamoDB, and access the cloud-resume table"""
    kwargs = {'endpoint_url': 'http://dynamodb-local:8000'}
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1', **kwargs)
    cloudresume_table = dynamodb.Table('cloud-resume')

    return cloudresume_table

def test_put_visitors(cloudresume_table):
    cloudresume_table.put_item(
        Item={
            "Id": "Visitors",
            "Visitors": 100
        }
    )

    event = {"Id": "Visitors"}
    context = {}

    ret = app.put_visitor_count(event, context, dynamoTable=cloudresume_table)
    print(ret)
    data = json.loads(ret["body"])
    
    assert ret["statusCode"] == 200, "status code shoud be successful"
    assert "visitor_count" in ret["body"], "key visitor_count should exist"
    assert int(data["visitor_count"]) == 101

def test_get_visitors(cloudresume_table):
    print("inside test_get_visitors")
    print(cloudresume_table)

    cloudresume_table.put_item(
        Item={
            "Id": "Visitors",
            "Visitors": 100
        }
    )

    event = {"Id": "Visitors"}
    context = {}

    ret = app.get_visitor_count(event, context, dynamoTable=cloudresume_table)
    data = json.loads(ret["body"])
    
    assert ret["statusCode"] == 200, "status code shoud be successful"
    assert "visitor_count" in ret["body"], "key visitor_count should exist"
    assert int(data["visitor_count"]) == 100