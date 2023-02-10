import os
import logging
import requests

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def proxy(event, context):
    log.info(event)
    return request_rest_apigateway()


def request_rest_apigateway():
    url = os.getenv("REST_API_GATEWAY_URL")
    log.info("request rest api gateway %s", url)
    r = requests.get(url)
    return {"statusCode": r.status_code, "body": r.content}
