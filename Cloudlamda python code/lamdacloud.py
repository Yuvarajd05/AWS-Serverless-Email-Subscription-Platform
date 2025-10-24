import json
import boto3

sns = boto3.client('sns')
TOPIC_ARN = "arn:aws:sns:ap-southeast-2:XXXXXXXXXXXX:NewsletterSubscription"

def lambda_handler(event, context):
    try:
        if 'body' not in event or not event['body']:
            return response(400, {'message': 'Missing request body'})

        body = json.loads(event['body'])
        email = body.get('email')

        if not email:
            return response(400, {'message': 'Email is required'})

        sns.subscribe(
            TopicArn=TOPIC_ARN,
            Protocol='email',
            Endpoint=email
        )

        return response(200, {'message': f'Subscription email sent to {email}'})
    except Exception as e:
        return response(500, {'error': str(e)})

def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, X-Amz-Date, Authorization, X-Api-Key"
        },
        "body": json.dumps(body)
    }
