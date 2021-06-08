import boto3
from botocore.exceptions import ClientError



class Orderdatabase():

    table_name = "orders"

    def __init__(self, dynamodb=None):
        if not dynamodb:
            self.dynamodb = boto3.resource('dynamodb')


    def save_order(self, data):
        table = self.dynamodb.Table(self.table_name)
        response = table.put_item(Item=data)
        return response


    def get_order(self, orderID):
        table = self.dynamodb.Table(self.table_name)
        try:
            response = table.get_item(Key={'orderID': orderID})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']