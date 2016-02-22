# aws-python-sandbox

## setup

```
$ tree .aws
.aws
├── config
└── credentials
```

```txt:config
[default]
region = ap-northeast-1
output = json
[profile shiraco]
region = ap-northeast-1
output = json
```

```txt:credential
[default]
aws_access_key_id = *******
aws_secret_access_key = *************************************
[shiraco]
aws_access_key_id = *******
aws_secret_access_key = *************************************
```

## Run

Use python-lambda-local

```
python-lambda-local -f lambda_handler lambda_function.py event.json
```

## References
* [DynamoDB — Boto 3 Docs 1.2.4 documentation](http://boto3.readthedocs.org/en/latest/guide/dynamodb.html)