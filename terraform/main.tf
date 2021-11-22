provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "policy_attachment_1" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole"
}

resource "aws_iam_role_policy_attachment" "policy_attachment_2" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}

resource "aws_sqs_queue" "urls_queue" {
  name = "urls-queue"
}

resource "aws_lambda_function" "lambda_function" {
  filename         = "../lambda-code/build/build.zip"
  function_name    = "make-requests"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.handler"
  source_code_hash = filebase64sha256("../lambda-code/build/build.zip")
  runtime          = "python3.9"
  memory_size      = 128
}

resource "aws_lambda_event_source_mapping" "lambda_function_event_source" {
  event_source_arn = aws_sqs_queue.urls_queue.arn
  enabled          = true
  function_name    = aws_lambda_function.lambda_function.arn
  batch_size       = 1
}