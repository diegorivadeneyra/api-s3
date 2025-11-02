import json
import boto3
import base64

def lambda_handler(event, context):
    body = json.loads(event["body"])

    bucket = body["bucket"]
    directory = body["directory"]
    filename = body["filename"]
    content = body["content"]  # texto o base64

    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=bucket,
        Key=f"{directory}/{filename}",
        Body=content.encode("utf-8")
    )

    return {"statusCode": 200, "body": f"Archivo {filename} subido a {bucket}/{directory}"}
