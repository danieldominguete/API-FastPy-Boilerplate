import os
from dotenv import load_dotenv, find_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

# Environment variables
load_dotenv(find_dotenv())


class DatabaseSchema(Model):
    """
    Data from iphone sensorlog app
    """

    class Meta:
        table_name = os.environ.get("AWS_DYNAMODB_RAWDATA_TABLE")
        region = os.environ.get("AWS_SELECTED_REGION")
        aws_access_key_id = os.environ.get("AWS_ID")
        aws_secret_access_key = os.environ.get("AWS_KEY")

    id = UnicodeAttribute(hash_key=True)
    deviceID = UnicodeAttribute(range_key=True)
    datetimeRegister = UnicodeAttribute()
    accelerometerAccelerationX = NumberAttribute(null=True, default=0)

