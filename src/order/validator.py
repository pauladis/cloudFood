from schema import Schema

schema = Schema(
    {
        "userId": str,
        "paymentMethod": str,
        "total": str,
        "product": [{"id": str, "type": str, "name": str, "price": str}],
    },
    ignore_extra_keys=True,
)

def validate(event):
    return schema.validate(event)