import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event["body"])
    bucket = body["bucket"]

    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)

    return {"statusCode": 200, "body": f"Bucket {bucket} creado"}
