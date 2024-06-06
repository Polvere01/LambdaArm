resource "aws_lambda_function" "example" {
  function_name = "ARQUITETURA"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.11"
  role          = aws_iam_role.lambda_role.arn
  filename      = "lambda_function.zip"

  source_code_hash = filebase64sha256("lambda_function.zip")

  architectures = [var.architecture]

  environment {
    variables = {
      EXAMPLE_VARIABLE = "Environment Test"
    }
  }

  timeout           = 900  
}
