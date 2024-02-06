# AWS Helpers
Repository for Boto3 wrapper class to interface with S3 bucket storage. Code from [boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Notes:
- before using, make sure authentication credentials are set up for your AWS account ([link to guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration))
- ensure keys are updated in `.env` file as specified by the `.env.template` file
- make sure to have boto3 installed (`pip install boto3`) in the selected Python environment
- [Loading Kaggle dataset to AWS S3 using Boto3](https://medium.com/@antonysruthy11/loading-kaggle-dataset-to-aws-s3-using-boto3-50af3e015fb2)