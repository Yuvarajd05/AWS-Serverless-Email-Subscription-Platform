☁️ AWS Serverless Email Subscription Platform

A fully serverless cloud application that enables users to subscribe to newsletters through a secure REST API.
This system leverages AWS Lambda, API Gateway, SNS, and IAM to deliver a scalable, event-driven architecture for automated email subscriptions and notifications.
Built with simplicity and scalability in mind, it connects seamlessly with any web frontend.

📌 Key Highlights

🌐 RESTful API with end-to-end email subscription flow

⚙️ Powered by AWS Lambda (Python) for backend logic

📬 Subscription confirmation via Amazon SNS

🔒 Secure access control with AWS IAM roles and policies

🚀 Fully serverless and auto-scaling (no EC2 or servers)

🔁 CORS-enabled for frontend integration

🧩 Simple HTML frontend connection supported

🧠 Architecture Overview

Workflow:
HTML Form → API Gateway → AWS Lambda → SNS → Email Confirmation

AWS Services Used:

AWS Lambda: Executes backend logic and triggers email subscriptions

Amazon API Gateway: Handles REST API requests securely

Amazon SNS: Sends subscription confirmation emails to users

AWS IAM: Manages access control and permissions between services

📂 Structure Overview

Repository Includes:

Lambda configuration and event handler files

Basic HTML frontend for API integration

Deployment and setup documentation

API Gateway configuration details

README for quick setup

⚙️ Setup & Deployment Steps

1️⃣ Create SNS Topic:

Set up a Standard Topic named NewsletterSubscription

Copy and use the Topic ARN in your backend configuration

2️⃣ Set Up IAM Role:

Create a role for Lambda with necessary permissions

Attach AmazonSNSFullAccess and AWSLambdaBasicExecutionRole

3️⃣ Deploy Lambda Function:

Create a Lambda function in Python

Assign the IAM role and configure environment variables

4️⃣ Create API Gateway:

Build a REST API with a /subscribe POST method

Integrate it with the Lambda function

Enable CORS and deploy to production

5️⃣ Connect HTML Frontend:

Create a simple form to collect user emails

Send the form data to the API endpoint using POST requests

6️⃣ Test Using Postman:

Test the endpoint with JSON input to confirm email functionality

🧪 Expected Functionality

When a user submits their email:

The API Gateway receives the request

Lambda function processes the email and triggers SNS

🧾 Tech Stack

Backend: AWS Lambda (Python)

API Management: Amazon API Gateway

Messaging: Amazon SNS

Access Control: AWS IAM

Frontend: Static HTML / JavaScript

🤝 Acknowledgements

Amazon Web Services (AWS)

AWS Developer Documentation

Serverless Architecture Community

Python Developer Ecosystem

SNS sends a subscription confirmation email

The user confirms via email to complete the subscription
