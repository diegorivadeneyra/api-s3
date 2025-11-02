import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event["body"])
    bucket = body["bucket"]
    directory = body["directory"]

    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=f"{directory}/")

    return {"statusCode": 200, "body": f"Directorio {directory} creado en {bucket}"}
