import os
import requests


def proxy(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    return request_rest_apigateway()


def request_rest_apigateway():
    url = os.getenv("REST_API_GATEWAY_URL")
    r = requests.get(url)
    return {"statusCode": r.status_code, "body": r.content}
