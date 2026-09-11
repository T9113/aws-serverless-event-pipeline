# aws-serverless-event-pipeline

Event-driven serverless data processing architecture.

## Flow
SNS Topic -> SQS FIFO Queue -> AWS Lambda Consumer -> DynamoDB Table

- Zero server management
- Built-in dead letter queue (DLQ) retry logic
