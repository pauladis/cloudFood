import json
import uuid
from orderDatabase import Orderdatabase
from queueManager import QueueManager
from schema import SchemaError
from validator import validate


def handler(event, context):
    queue = QueueManager()
    msg = 'teste'
    if event['httpMethod'] == 'GET':
        #TODO
        msg = "hello world"
    elif event['httpMethod'] == 'POST':
        try:
            order = validate(json.loads(event['body']))
            order["orderID"] = str(uuid.uuid1())
            db = Orderdatabase()
            db.save_order(order)
            msg = "Order placed"
            queue.send_order(order)
        except SchemaError:
            msg = "invalid payload"
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": msg,
        }),
    }