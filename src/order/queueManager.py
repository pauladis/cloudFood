import boto3
import json
from datetime import date, timedelta

class QueueManager():

    def __init__(self):
        self.QName = "orders"
        self.region_name = "us-east-1"
        self.sqs_client = boto3.client("sqs", region_name=self.region_name)
        self.__create_queue()
        self.queueUrl = self.get_queue_url()
        #self.__purge_queue()


    def __create_queue(self, delaySeconds="0", visibilityTimeout="60"):
        self.sqs_client.create_queue(
            QueueName=self.QName,
            Attributes={
                "DelaySeconds": delaySeconds,
                "VisibilityTimeout": visibilityTimeout,
            }
        )

    def get_queue_url(self):
        response = self.sqs_client.get_queue_url(QueueName=self.QName)
        return response["QueueUrl"]


    def send_order(self, data):
        response = self.sqs_client.send_message(
            QueueUrl=self.queueUrl,
            MessageBody=json.dumps(data)
        )
        return response


    def delete_orders(self, receipt_handle):
        self.sqs_client.delete_message(
            QueueUrl=self.queueUrl,
            ReceiptHandle=receipt_handle
        )


    def receive_order(self):
        messages = []
        while True:
            response = self.sqs_client.receive_message(
                QueueUrl=self.queueUrl,
                MaxNumberOfMessages=5,
                WaitTimeSeconds=10,
            )

            if response.get("Messages", []) == []:
                break

            messages.append(response.get("Messages"))
            self.delete_orders(response.get("receipt_handle"))

        return messages


    def __purge_queue(self):
        response = self.sqs_client.purge_queue(
            QueueUrl=self.queueUrl
        )
        return response

