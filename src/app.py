import json

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent

LOGGER = Logger()


def lambda_handler(event: APIGatewayProxyEvent, context: LambdaContext):

    LOGGER.info(event["body"])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
