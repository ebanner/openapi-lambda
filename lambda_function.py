import json

from openai import OpenAI

import boto3
from botocore.exceptions import ClientError


def get_openai_api_key():

    secret_name = "OPENAI_API_KEY"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    result = json.loads(secret)
    return result[secret_name]


def lambda_handler(event, context):
    openai_api_key = get_openai_api_key()
    client = OpenAI(api_key=openai_api_key)

    body_json = event['body']
    body = json.loads(body_json)

    system = body['system']
    user = body['user']

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    )

    output = completion.choices[0].message.content

    return {
        'statusCode': 200,
        'body': output,
    }

